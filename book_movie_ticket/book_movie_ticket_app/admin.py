from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Movie, Ticket, CustomUser, Room, Seat, Showtime
from django import forms    

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'name', 'age', 'is_staff', 'is_active']
    list_filter = ['id', 'username', 'name', 'age', 'is_staff', 'is_active']
    fieldsets = (
        ('Thông tin tài khoản', {'fields': ('username', 'password')}),
        ('Thông tin cá nhân', {'fields': ('name', 'age')}),
        ('Quyền hạn', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    search_fields = ('username','name')
    ordering = ('id',)
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'age', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    
class ShowtimeInline(admin.TabularInline):
    model = Showtime
    extra = 1
    fields = ['room', 'start_time', 'end_time', 'is_active']
    
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'genre', 'duration', 'director', 'release_date','poster']
    list_filter = ['id', 'title', 'genre', 'duration', 'director', 'release_date']
    search_fields = ('title', 'genre', 'director')
    ordering = ('id',)
    inlines = [ShowtimeInline]
    
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'room', 'start_time', 'end_time', 'is_active', 'get_available_seats_count', 'get_booked_seats_count']
    list_filter = ['movie', 'room', 'is_active', 'start_time']
    search_fields = ('movie__title', 'room__name')
    ordering = ('start_time',)
    readonly_fields = ['get_available_seats_count', 'get_booked_seats_count']
    
    def get_available_seats_count(self, obj):
        return obj.get_available_seats_count()
    get_available_seats_count.short_description = 'Ghế còn trống'
    
    def get_booked_seats_count(self, obj):
        return obj.get_booked_seats_count()
    get_booked_seats_count.short_description = 'Ghế đã đặt'
    
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'capacity']
    list_filter = ['id', 'name', 'capacity']
    search_fields = ('name',)
    ordering = ('id',)
    
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'room', 'seat', 'showtime', 'price', 'type', 'date_time']
    list_filter = ['id', 'user', 'movie', 'room', 'seat', 'showtime', 'price', 'type', 'date_time']
    search_fields = ('user__username', 'movie__title', 'room__name', 'seat__seat_number', 'showtime__id')
    ordering = ('id',)
    
class SeatAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'seat_number', 'is_available']
    list_filter = ['id', 'room', 'seat_number', 'is_available']
    search_fields = ('room', 'seat_number', 'is_available')
    ordering = ('id',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Showtime, ShowtimeAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Seat, SeatAdmin)
