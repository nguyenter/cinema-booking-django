"""
Script để tạo các suất chiếu ngẫu nhiên cho từng phim
Chạy: python create_showtimes_script.py
"""
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_movie_ticket.settings')
django.setup()

from django.utils import timezone
from datetime import datetime, timedelta
import random
from book_movie_ticket_app.models import Movie, Room, Showtime


def create_showtimes(days=7, per_movie=5):
    """Tạo các suất chiếu ngẫu nhiên cho tất cả các phim"""
    
    # Các khung giờ chiếu phổ biến
    time_slots = [
        '09:00', '10:00', '11:00',  # Buổi sáng
        '13:00', '14:00', '15:00', '16:00',  # Buổi chiều
        '18:00', '19:00', '20:00', '21:00', '22:00',  # Buổi tối
    ]
    
    movies = Movie.objects.all()
    rooms = Room.objects.all()
    
    if not movies.exists():
        print('⚠ Không có phim nào trong database!')
        return
    
    if not rooms.exists():
        print('⚠ Không có phòng chiếu nào trong database!')
        return
    
    total_created = 0
    total_skipped = 0
    
    for movie in movies:
        print(f'\nĐang xử lý phim: {movie.title}')
        
        # Tạo ngẫu nhiên số suất chiếu cho phim này (từ 3 đến per_movie)
        num_showtimes = random.randint(3, per_movie)
        
        created_count = 0
        skipped_count = 0
        
        for _ in range(num_showtimes * 2):  # Thử nhiều lần để tránh trùng
            if created_count >= num_showtimes:
                break
            
            # Chọn ngẫu nhiên một phòng
            room = random.choice(rooms)
            
            # Chọn ngẫu nhiên một ngày trong tương lai
            days_ahead = random.randint(0, days)
            target_date = timezone.now().date() + timedelta(days=days_ahead)
            
            # Chọn ngẫu nhiên một khung giờ
            time_slot = random.choice(time_slots)
            
            # Tạo datetime từ date và time
            hour, minute = map(int, time_slot.split(':'))
            start_time = timezone.make_aware(
                datetime.combine(target_date, datetime.min.time().replace(hour=hour, minute=minute))
            )
            
            # Tính end_time dựa trên duration của phim (thêm 30 phút cho quảng cáo và dọn dẹp)
            end_time = start_time + timedelta(minutes=movie.duration + 30)
            
            # Kiểm tra xem showtime đã tồn tại chưa
            if Showtime.objects.filter(
                movie=movie,
                room=room,
                start_time=start_time
            ).exists():
                skipped_count += 1
                continue
            
            # Tạo showtime
            showtime = Showtime.objects.create(
                movie=movie,
                room=room,
                start_time=start_time,
                end_time=end_time,
                is_active=True
            )
            
            created_count += 1
            total_created += 1
            
            print(f'  ✓ Đã tạo: {room.name} - {start_time.strftime("%d/%m/%Y %H:%M")}')
        
        if skipped_count > 0:
            print(f'  ⚠ Đã bỏ qua {skipped_count} suất chiếu trùng lặp')
    
    print(f'\n\n✅ Hoàn thành! Đã tạo {total_created} suất chiếu cho {movies.count()} phim.')


if __name__ == '__main__':
    print('=' * 60)
    print('Tạo suất chiếu ngẫu nhiên cho các phim')
    print('=' * 60)
    
    # Có thể thay đổi các tham số này
    days = 14  # Số ngày trong tương lai
    per_movie = 6  # Số suất chiếu tối đa cho mỗi phim
    
    create_showtimes(days=days, per_movie=per_movie)

