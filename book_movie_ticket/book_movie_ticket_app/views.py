from .models import *
from .forms import *
from .models import Showtime
from .vnpay import vnpay
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from datetime import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.conf import settings
import json

def homepage(request):
    if request.user.is_anonymous:
        return render(request, 'home.html') 
    # return HttpResponse(request.user)
    return book_ticket(request) # if user is logged in, redirect to book_ticket page
    
@login_required
def book_ticket(request):
    username = request.user.username
    name = request.user.name
    age = request.user.age
    user_tickets = Ticket.objects.filter(user=request.user).select_related('showtime', 'movie', 'room')
    for ticket in user_tickets:
        # Sử dụng showtime.start_time nếu có, nếu không thì dùng date_time
        if ticket.showtime:
            ticket.display_time = ticket.showtime.start_time.strftime('%d/%m/%Y %H:%M:%S')
        elif ticket.date_time:
            ticket.display_time = datetime.strptime(str(ticket.date_time).split('+')[0], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
        else:
            ticket.display_time = 'N/A'
    return render(request, 'book_ticket.html', {'username': username, 'name': name, 'age': age, 'user_tickets': user_tickets})
   
def user_login(request):
    show_login_form = True # to show login form 
    if request.method != 'POST':
        messages.error(request,"Vui lòng đăng nhập hoặc đăng ký để đặt vé")
        return render(request, 'home.html', {'show_login_form': show_login_form})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('rememberMe')
        
        if remember_me == 'on':
            request.session.set_expiry(1209600) # remember user account for 14 days
        
        if not username or not password:
            messages.error(request, "Vui lòng nhập tên tài khoản và mật khẩu!")
            return render(request, 'home.html', {'show_login_form': show_login_form})
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff == True:
                return redirect('/admin/')
            return book_ticket(request)
        else:
            messages.error(request, "Tên tài khoản hoặc mật khẩu không đúng!")
            return render(request, 'home.html', {'show_login_form': show_login_form})
        
def user_logout(request):
    logout(request)
    return homepage(request)
    
def user_register(request):
    show_register_form = True # to show register form
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        name = request.POST.get('name')
        age = request.POST.get('age')
        if not username or not password or not name or not age:
            messages.error(request, "Vui lòng điền đầy đủ thông tin!")
            return render(request, 'home.html', {'show_register_form': show_register_form})
                
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Tên đăng nhập đã tồn tại! Vui lòng chọn tên đăng nhập khác!")
            return render(request, 'home.html', {'show_register_form': show_register_form})
        
        if password != password_confirm:
            messages.error(request, "Mật khẩu không trùng khớp!")
            return render(request, 'home.html', {'show_register_form': show_register_form})
        
        age = int(age)
        if age < 0 or age > 100:
            messages.error(request, "Tuổi không hợp lệ!")
            return render(request, 'home.html', {'show_register_form': show_register_form})
        
        user = CustomUser.objects.create_user(username=username, password=password, name=name, age=age)
        user.save()
        register_sucess = True # to show register success message
        show_register_form = False
        messages.success(request, "Đăng ký tài khoản thành công!")
        return render(request, 'home.html', {'register_sucess': register_sucess, 'show_register_form': show_register_form})
    else:
        return render(request, 'home.html', {'show_register_form': show_register_form})

def movie_schedule(request):
    return render(request, 'movie_schedule.html')

def contact(request):
    return render(request, 'contact.html')

def movie_list(request):
    movies = Movie.objects.all()
    # Tạo form cho mỗi phim với showtime của phim đó
    movies_with_forms = []
    for movie in movies:
        form = BookTicketForm(movie=movie)
        showtimes = Showtime.objects.filter(movie=movie, is_active=True).order_by('start_time')
        movies_with_forms.append({
            'movie': movie,
            'form': form,
            'showtimes': showtimes
        })
    return render(request, 'movie_list.html', {'movies_with_forms': movies_with_forms})

def get_seats(request):
    showtime_id = request.GET.get('showtime_id')
    if not showtime_id:
        return render(request, 'book_ticket/seat_selection.html', {'seats': [], 'booked_seat_ids': []})
    try:
        showtime = get_object_or_404(Showtime, id=showtime_id)
        room = showtime.room
        # Lấy tất cả ghế của phòng
        seats = Seat.objects.filter(room=room).order_by('seat_number')
        # Lấy danh sách ghế đã được đặt cho suất chiếu này
        booked_tickets = Ticket.objects.filter(showtime=showtime)
        booked_seat_ids = [ticket.seat.id for ticket in booked_tickets]
        return render(request, 'book_ticket/seat_selection.html', {
            'seats': seats, 
            'booked_seat_ids': booked_seat_ids,
            'showtime': showtime
        })
    except Exception as e:
        return render(request, 'book_ticket/seat_selection.html', {'seats': [], 'booked_seat_ids': []})

@login_required
def prepare_payment(request):
    """Lưu thông tin đặt vé vào session và chuyển sang trang thanh toán"""
    if request.method == 'POST':
        try:
            showtime_id = request.POST.get('showtime_id')
            if not showtime_id:
                return JsonResponse({'status': 'error', 'message': 'Vui lòng chọn suất chiếu'})
            
            showtime = get_object_or_404(Showtime, id=showtime_id)
            movie = showtime.movie
            room = showtime.room
            type = request.POST.get('type')
            
            # Nhận danh sách ghế đã chọn
            selected_seats = request.POST.getlist('selected_seats[]')
            if not selected_seats:
                return JsonResponse({'status': 'error', 'message': 'Vui lòng chọn ghế'})
            
            # Loại bỏ trùng lặp
            selected_seats = [str(s) for s in selected_seats if s]
            selected_seats = list(set(selected_seats))
            
            if not selected_seats:
                return JsonResponse({'status': 'error', 'message': 'Vui lòng chọn ghế'})
            
            quantity = int(request.POST.get('quantity', 1))
            if len(selected_seats) != quantity:
                return JsonResponse({'status': 'error', 'message': f'Số lượng ghế ({len(selected_seats)}) không khớp với số lượng vé ({quantity})'})
            
            # Kiểm tra ghế có còn trống không
            for seat_id in selected_seats:
                seat = get_object_or_404(Seat, id=seat_id)
                if Ticket.objects.filter(showtime=showtime, seat=seat).exists():
                    return JsonResponse({'status': 'error', 'message': f'Ghế {seat.seat_number} đã được đặt'})
            
            # Tính tổng tiền
            price_per_ticket = 100000 if type == 'Adult' else 50000
            total_amount = price_per_ticket * quantity
            
            # Lưu thông tin vào session
            booking_data = {
                'showtime_id': showtime_id,
                'movie_id': movie.id,
                'movie_title': movie.title,
                'room_id': room.id,
                'room_name': room.name,
                'type': type,
                'selected_seats': selected_seats,
                'quantity': quantity,
                'price_per_ticket': price_per_ticket,
                'total_amount': total_amount,
                'showtime_start': showtime.start_time.isoformat(),
            }
            request.session['booking_data'] = booking_data
            
            # Chuyển sang trang thanh toán
            return JsonResponse({
                'status': 'success',
                'redirect_url': '/payment/'
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


@login_required
def payment(request):
    """Trang thanh toán VNPay"""
    booking_data = request.session.get('booking_data')
    
    if not booking_data:
        messages.error(request, 'Không tìm thấy thông tin đặt vé. Vui lòng đặt lại.')
        return redirect('movie_list')
    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            order_type = form.cleaned_data['order_type']
            order_id = form.cleaned_data['order_id']
            amount = form.cleaned_data['amount']
            order_desc = form.cleaned_data['order_desc']
            bank_code = form.cleaned_data['bank_code']
            language = form.cleaned_data['language']
            
            # Lấy IP của client
            ipaddr = get_client_ip(request)
            
            # Build URL Payment
            vnp = vnpay()
            vnp.requestData['vnp_Version'] = '2.1.0'
            vnp.requestData['vnp_Command'] = 'pay'
            vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
            # VNPay yêu cầu amount là số nguyên (đơn vị: xu)
            vnp.requestData['vnp_Amount'] = int(amount * 100)
            vnp.requestData['vnp_CurrCode'] = 'VND'
            vnp.requestData['vnp_TxnRef'] = order_id
            vnp.requestData['vnp_OrderInfo'] = order_desc
            vnp.requestData['vnp_OrderType'] = order_type
            
            if language and language != '':
                vnp.requestData['vnp_Locale'] = language
            else:
                vnp.requestData['vnp_Locale'] = 'vn'
            
            if bank_code and bank_code != "":
                vnp.requestData['vnp_BankCode'] = bank_code
            
            vnp.requestData['vnp_CreateDate'] = datetime.now().strftime('%Y%m%d%H%M%S')
            vnp.requestData['vnp_IpAddr'] = ipaddr
            vnp.requestData['vnp_ReturnUrl'] = settings.VNPAY_RETURN_URL
            vnp.requestData['vnp_IpNUrl'] = settings.VNPAY_IPN_URL  # IPN URL (server call server)
            
            # Debug: In ra thông tin để kiểm tra
            print("=" * 60)
            print("VNPay Request Data:")
            for key, val in sorted(vnp.requestData.items()):
                print(f"  {key}: {val}")
            print("=" * 60)
            
            vnpay_payment_url = vnp.get_payment_url(settings.VNPAY_PAYMENT_URL, settings.VNPAY_HASH_SECRET_KEY)
            
            print("VNPay Payment URL:", vnpay_payment_url)
            print("=" * 60)
            
            # Redirect to VNPAY
            return redirect(vnpay_payment_url)
        else:
            messages.error(request, 'Dữ liệu thanh toán không hợp lệ')
    else:
        # Tạo order_id từ timestamp và user_id (tối đa 15 ký tự theo VNPay)
        timestamp = int(datetime.now().timestamp())
        order_id = f"{request.user.id}{timestamp}"[-15:]  # Giới hạn 15 ký tự
        # order_desc không dấu để tránh lỗi encoding
        order_desc = f"Dat ve xem phim: {booking_data['movie_title']} - {booking_data['quantity']} ve"
        amount = booking_data['total_amount']
        
        form = PaymentForm(initial={
            'order_type': 'other',
            'order_id': order_id,
            'amount': amount,
            'order_desc': order_desc,
            'language': 'vn'
        })
        
        # Lưu order_id vào session
        request.session['order_id'] = order_id
    
    context = {
        'form': form,
        'booking_data': booking_data,
        'title': 'Thanh toán'
    }
    return render(request, 'payment.html', context)


@login_required
def payment_return(request):
    """Xử lý kết quả thanh toán từ VNPay"""
    booking_data = request.session.get('booking_data')
    order_id = request.session.get('order_id')
    
    if not booking_data:
        messages.error(request, 'Không tìm thấy thông tin đặt vé.')
        return redirect('movie_list')
    
    vnp_Params = request.GET.dict()
    
    if 'vnp_SecureHash' in vnp_Params:
        vnp_Params.pop('vnp_SecureHash', None)
        vnp_Params.pop('vnp_SecureHashType', None)
        
        vnp = vnpay()
        if vnp.validate_response(vnp_Params, settings.VNPAY_HASH_SECRET_KEY):
            response_code = vnp_Params.get('vnp_ResponseCode', '')
            
            if response_code == '00':  # Thanh toán thành công
                try:
                    # Tạo vé
                    showtime = get_object_or_404(Showtime, id=booking_data['showtime_id'])
                    movie = get_object_or_404(Movie, id=booking_data['movie_id'])
                    room = get_object_or_404(Room, id=booking_data['room_id'])
                    user = request.user
                    
                    tickets = []
                    for seat_id in booking_data['selected_seats']:
                        seat = get_object_or_404(Seat, id=seat_id)
                        # Kiểm tra lại lần nữa
                        if Ticket.objects.filter(showtime=showtime, seat=seat).exists():
                            continue
                        
                        ticket = Ticket(
                            movie=movie,
                            user=user,
                            room=room,
                            seat=seat,
                            showtime=showtime,
                            price=booking_data['price_per_ticket'],
                            type=booking_data['type'],
                            date_time=showtime.start_time,
                        )
                        tickets.append(ticket)
                    
                    if tickets:
                        Ticket.objects.bulk_create(tickets)
                        # Xóa booking_data khỏi session
                        del request.session['booking_data']
                        del request.session['order_id']
                        
                        messages.success(request, f'Thanh toán thành công! Đã đặt {len(tickets)} vé.')
                        return redirect('homepage')
                    else:
                        messages.error(request, 'Không thể tạo vé. Vui lòng liên hệ hỗ trợ.')
                except Exception as e:
                    messages.error(request, f'Lỗi khi tạo vé: {str(e)}')
            else:
                messages.error(request, f'Thanh toán thất bại. Mã lỗi: {response_code}')
        else:
            messages.error(request, 'Chữ ký không hợp lệ.')
    else:
        messages.error(request, 'Thiếu thông tin xác thực.')
    
    return redirect('movie_list')


@csrf_exempt
def payment_ipn(request):
    """
    IPN (Instant Payment Notification) URL
    VNPay sẽ gọi URL này để cập nhật trạng thái thanh toán (server call server)
    VNPay thường gửi dữ liệu qua GET với query string
    """
    # Debug: In ra thông tin request
    print("=" * 60)
    print("IPN Request received:")
    print(f"Method: {request.method}")
    print(f"GET params: {request.GET.dict()}")
    print(f"POST params: {request.POST.dict()}")
    print("=" * 60)
    
    # VNPay thường gửi qua GET với query string
    if request.method == 'GET':
        vnp_Params = request.GET.dict()
    elif request.method == 'POST':
        vnp_Params = request.POST.dict()
    else:
        print("IPN: Invalid request method")
        return HttpResponse('Invalid method', status=405)
    
    # Kiểm tra xem có dữ liệu không
    if not vnp_Params:
        print("IPN: No parameters received")
        return HttpResponse('No parameters', status=400)
    
    print(f"IPN Parameters: {vnp_Params}")
    
    order_id = vnp_Params.get('vnp_TxnRef')
    response_code = vnp_Params.get('vnp_ResponseCode')
    transaction_status = vnp_Params.get('vnp_TransactionStatus')
    
    print(f"IPN - Order ID: {order_id}, Response Code: {response_code}, Transaction Status: {transaction_status}")
    
    # Validate checksum
    vnp = vnpay()
    if vnp.validate_response(vnp_Params, settings.VNPAY_HASH_SECRET_KEY):
        print("IPN: Checksum validated successfully")
        if response_code == '00' and transaction_status == '00':
            # Thanh toán thành công
            # Có thể cập nhật trạng thái đơn hàng ở đây nếu cần
            # Hoặc đã xử lý ở payment_return rồi
            print("IPN: Payment successful")
            return HttpResponse('success', status=200)
        else:
            # Thanh toán thất bại
            print(f"IPN: Payment failed - Response Code: {response_code}, Transaction Status: {transaction_status}")
            return HttpResponse('failed', status=200)
    else:
        # Checksum không hợp lệ
        print("IPN: Invalid checksum")
        return HttpResponse('invalid_checksum', status=400)


def get_client_ip(request):
    """Lấy IP address của client"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@login_required
def user_booking(request):
    """Giữ lại để tương thích, nhưng không dùng nữa"""
    return HttpResponse('Please use payment flow')
    
