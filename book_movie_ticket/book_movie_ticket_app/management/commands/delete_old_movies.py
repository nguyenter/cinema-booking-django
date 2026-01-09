"""
Django management command để xóa các phim có ngày công chiếu trước năm 2025
"""
import sys
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from book_movie_ticket_app.models import Movie, Showtime, Ticket

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


class Command(BaseCommand):
    help = 'Xóa các phim có ngày công chiếu trước năm 2025'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Chỉ hiển thị danh sách phim sẽ bị xóa, không thực sự xóa',
        )
        parser.add_argument(
            '--year',
            type=int,
            default=2025,
            help='Năm bắt đầu (mặc định: 2025)',
        )

    def handle(self, *args, **options):
        year = options['year']
        dry_run = options['dry_run']
        cutoff_date = date(year, 1, 1)
        
        # Tìm các phim có ngày công chiếu trước năm được chỉ định
        old_movies = Movie.objects.filter(release_date__lt=cutoff_date)
        count = old_movies.count()
        
        if count == 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Không có phim nào có ngày công chiếu trước {year}-01-01'
                )
            )
            return
        
        self.stdout.write(
            self.style.WARNING(
                f'\nTìm thấy {count} phim có ngày công chiếu trước {year}-01-01:'
            )
        )
        self.stdout.write('=' * 60)
        
        for movie in old_movies:
            # Đếm số suất chiếu và vé liên quan
            showtimes_count = Showtime.objects.filter(movie=movie).count()
            tickets_count = Ticket.objects.filter(movie=movie).count()
            
            self.stdout.write(
                f'ID: {movie.id} | {movie.title} | '
                f'Ngày công chiếu: {movie.release_date} | '
                f'Suất chiếu: {showtimes_count} | Vé: {tickets_count}'
            )
        
        self.stdout.write('=' * 60)
        
        if dry_run:
            self.stdout.write(
                self.style.WARNING(
                    '\nDRY RUN: Không có phim nào bị xóa. Chạy lại không có --dry-run để xóa thực sự.'
                )
            )
            return
        
        # Xác nhận xóa
        self.stdout.write(
            self.style.WARNING(
                f'\n⚠️  CẢNH BÁO: Bạn sắp xóa {count} phim và tất cả dữ liệu liên quan!'
            )
        )
        self.stdout.write(
            self.style.WARNING(
                'Điều này sẽ xóa:'
            )
        )
        self.stdout.write('  - Các phim cũ')
        self.stdout.write('  - Tất cả suất chiếu của các phim này')
        self.stdout.write('  - Tất cả vé đã đặt của các phim này')
        
        # Đếm tổng số suất chiếu và vé sẽ bị xóa
        total_showtimes = Showtime.objects.filter(movie__in=old_movies).count()
        total_tickets = Ticket.objects.filter(movie__in=old_movies).count()
        
        self.stdout.write(
            self.style.WARNING(
                f'\nTổng số sẽ bị xóa:'
            )
        )
        self.stdout.write(f'  - Phim: {count}')
        self.stdout.write(f'  - Suất chiếu: {total_showtimes}')
        self.stdout.write(f'  - Vé: {total_tickets}')
        
        # Xóa các phim (CASCADE sẽ tự động xóa showtime và ticket)
        deleted_count = 0
        for movie in old_movies:
            movie_title = movie.title
            movie.delete()
            deleted_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'  ✓ Đã xóa: {movie_title}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\n✅ Hoàn thành! Đã xóa {deleted_count} phim và tất cả dữ liệu liên quan.'
            )
        )
