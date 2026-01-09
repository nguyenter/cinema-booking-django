from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Movie, Ticket, CustomUser, Room, Seat, Showtime
from django import forms
from django.utils.html import format_html
from django.urls import reverse

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'name', 'age', 'get_status_badge', 'is_staff', 'last_login']
    list_filter = ['is_staff', 'is_active', 'is_superuser', 'last_login']
    fieldsets = (
        ('Thông tin tài khoản', {'fields': ('username', 'password')}),
        ('Thông tin cá nhân', {'fields': ('name', 'age')}),
        ('Quyền hạn', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    search_fields = ('username', 'name')
    ordering = ('-id',)
    list_per_page = 25
    date_hierarchy = 'last_login'
    
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'age', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    
    def get_status_badge(self, obj):
        if obj.is_active:
            return format_html(
                '<span style="background: #d4edda; color: #155724; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">Hoạt động</span>'
            )
        else:
            return format_html(
                '<span style="background: #f8d7da; color: #721c24; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">Vô hiệu</span>'
            )
    get_status_badge.short_description = 'Trạng thái'
    
class ShowtimeInline(admin.TabularInline):
    model = Showtime
    extra = 1
    fields = ['room', 'start_time', 'end_time', 'is_active']
    classes = ['collapse']
    
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_poster_thumbnail', 'title', 'genre', 'duration', 'director', 'release_date', 'get_showtimes_count']
    list_filter = ['genre', 'release_date', 'director']
    search_fields = ('title', 'genre', 'director', 'description')
    ordering = ('-id',)
    list_per_page = 20
    date_hierarchy = 'release_date'
    inlines = [ShowtimeInline]
    readonly_fields = ['get_poster_preview']
    
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('title', 'genre', 'director', 'release_date', 'duration')
        }),
        ('Mô tả', {
            'fields': ('description',)
        }),
        ('Ảnh bìa', {
            'fields': ('poster', 'get_poster_preview')
        }),
    )
    
    def get_poster_thumbnail(self, obj):
        if obj.poster:
            return format_html(
                '<img src="{}" style="width: 50px; height: 70px; object-fit: cover; border-radius: 4px;" />',
                obj.poster.url
            )
        return "Không có ảnh"
    get_poster_thumbnail.short_description = 'Ảnh'
    
    def get_poster_preview(self, obj):
        if obj.poster:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 400px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" />',
                obj.poster.url
            )
        return "Chưa có ảnh bìa"
    get_poster_preview.short_description = 'Xem trước'
    
    def get_showtimes_count(self, obj):
        count = obj.showtimes.count()
        if count > 0:
            url = reverse('admin:book_movie_ticket_app_showtime_changelist')
            return format_html(
                '<a href="{}?movie__id__exact={}" style="color: #667eea; font-weight: 600;">{} suất chiếu</a>',
                url, obj.id, count
            )
        return "0 suất chiếu"
    get_showtimes_count.short_description = 'Số suất chiếu'
    
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'room', 'get_formatted_start_time', 'get_formatted_end_time', 'get_status_badge', 'get_seats_info']
    list_filter = ['movie', 'room', 'is_active', 'start_time']
    search_fields = ('movie__title', 'room__name')
    ordering = ('-start_time',)
    list_per_page = 30
    date_hierarchy = 'start_time'
    readonly_fields = ['get_available_seats_count', 'get_booked_seats_count', 'get_seats_info']
    
    fieldsets = (
        ('Thông tin suất chiếu', {
            'fields': ('movie', 'room', 'start_time', 'end_time', 'is_active')
        }),
        ('Thống kê ghế', {
            'fields': ('get_available_seats_count', 'get_booked_seats_count', 'get_seats_info'),
            'classes': ('collapse',)
        }),
    )
    
    def get_formatted_start_time(self, obj):
        return obj.start_time.strftime('%d/%m/%Y %H:%M')
    get_formatted_start_time.short_description = 'Thời gian bắt đầu'
    get_formatted_start_time.admin_order_field = 'start_time'
    
    def get_formatted_end_time(self, obj):
        if obj.end_time:
            return obj.end_time.strftime('%d/%m/%Y %H:%M')
        return "-"
    get_formatted_end_time.short_description = 'Thời gian kết thúc'
    get_formatted_end_time.admin_order_field = 'end_time'
    
    def get_status_badge(self, obj):
        if obj.is_active:
            return format_html(
                '<span style="background: #d4edda; color: #155724; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">Đang hoạt động</span>'
            )
        else:
            return format_html(
                '<span style="background: #f8d7da; color: #721c24; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">Tạm dừng</span>'
            )
    get_status_badge.short_description = 'Trạng thái'
    
    def get_available_seats_count(self, obj):
        count = obj.get_available_seats_count()
        return format_html(
            '<span style="color: #48bb78; font-weight: 600; font-size: 16px;">{}</span>',
            count
        )
    get_available_seats_count.short_description = 'Ghế còn trống'
    
    def get_booked_seats_count(self, obj):
        count = obj.get_booked_seats_count()
        return format_html(
            '<span style="color: #f56565; font-weight: 600; font-size: 16px;">{}</span>',
            count
        )
    get_booked_seats_count.short_description = 'Ghế đã đặt'
    
    def get_seats_info(self, obj):
        available = obj.get_available_seats_count()
        booked = obj.get_booked_seats_count()
        total = obj.room.capacity
        percentage = (booked / total * 100) if total > 0 else 0
        
        return format_html(
            '<div style="margin-top: 10px;">'
            '<div style="background: #e0e0e0; height: 20px; border-radius: 10px; overflow: hidden; position: relative;">'
            '<div style="background: linear-gradient(90deg, #48bb78 0%, #38a169 100%); height: 100%; width: {}%; transition: width 0.3s;"></div>'
            '</div>'
            '<div style="margin-top: 5px; font-size: 12px; color: #6c757d;">'
            'Đã đặt: <strong>{}</strong> / Tổng: <strong>{}</strong> ({:.1f}%)'
            '</div>'
            '</div>',
            percentage, booked, total, percentage
        )
    get_seats_info.short_description = 'Biểu đồ ghế'
    
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'capacity', 'get_seats_count', 'get_available_seats_count']
    list_filter = ['capacity']
    search_fields = ('name',)
    ordering = ('id',)
    list_per_page = 25
    
    def get_seats_count(self, obj):
        count = Seat.objects.filter(room=obj).count()
        url = reverse('admin:book_movie_ticket_app_seat_changelist')
        return format_html(
            '<a href="{}?room__id__exact={}" style="color: #667eea; font-weight: 600;">{} ghế</a>',
            url, obj.id, count
        )
    get_seats_count.short_description = 'Tổng số ghế'
    
    def get_available_seats_count(self, obj):
        available = Seat.objects.filter(room=obj, is_available=True).count()
        total = Seat.objects.filter(room=obj).count()
        if total > 0:
            percentage = (available / total * 100)
            color = '#48bb78' if percentage > 50 else '#ed8936' if percentage > 20 else '#f56565'
            return format_html(
                '<span style="color: {}; font-weight: 600;">{} / {} ({:.1f}%)</span>',
                color, available, total, percentage
            )
        return "0"
    get_available_seats_count.short_description = 'Ghế còn trống'
    
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'movie', 'room', 'seat', 'showtime', 'get_price_formatted', 'get_type_badge', 'get_formatted_date_time']
    list_filter = ['type', 'movie', 'room', 'showtime', 'date_time']
    search_fields = ('user__username', 'user__name', 'movie__title', 'room__name', 'seat__seat_number')
    ordering = ('-id',)
    list_per_page = 30
    date_hierarchy = 'date_time'
    readonly_fields = ['get_price_formatted']
    
    fieldsets = (
        ('Thông tin vé', {
            'fields': ('user', 'movie', 'room', 'seat', 'showtime')
        }),
        ('Chi tiết thanh toán', {
            'fields': ('price', 'get_price_formatted', 'type', 'date_time')
        }),
    )
    
    def get_price_formatted(self, obj):
        if obj.price:
            return format_html(
                '<span style="color: #48bb78; font-weight: 600; font-size: 16px;">{:,} VNĐ</span>',
                obj.price
            )
        return "-"
    get_price_formatted.short_description = 'Giá (đã định dạng)'
    
    def get_type_badge(self, obj):
        if obj.type == 'Adult':
            return format_html(
                '<span style="background: #667eea; color: #fff; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">Người lớn</span>'
            )
        else:
            return format_html(
                '<span style="background: #ed8936; color: #fff; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">Trẻ em</span>'
            )
    get_type_badge.short_description = 'Loại vé'
    
    def get_formatted_date_time(self, obj):
        if obj.date_time:
            return obj.date_time.strftime('%d/%m/%Y %H:%M')
        return "-"
    get_formatted_date_time.short_description = 'Ngày giờ chiếu'
    get_formatted_date_time.admin_order_field = 'date_time'
    
class SeatAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'seat_number', 'get_status_badge']
    list_filter = ['room', 'is_available']
    search_fields = ('room__name', 'seat_number')
    ordering = ('room', 'seat_number')
    list_per_page = 50
    
    def get_status_badge(self, obj):
        if obj.is_available:
            return format_html(
                '<span style="background: #d4edda; color: #155724; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">Còn trống</span>'
            )
        else:
            return format_html(
                '<span style="background: #f8d7da; color: #721c24; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">Đã đặt</span>'
            )
    get_status_badge.short_description = 'Trạng thái'

admin.site.register(Movie, MovieAdmin)
admin.site.register(Showtime, ShowtimeAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Seat, SeatAdmin)
