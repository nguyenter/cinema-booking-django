# 📋 BÁO CÁO CHỨC NĂNG VÀ CÔNG NGHỆ HỆ THỐNG

## 🎯 TỔNG QUAN HỆ THỐNG
**Hệ thống đặt vé xem phim CinemaPlus** - Ứng dụng web quản lý và đặt vé xem phim trực tuyến

---

## 🚀 CÁC CHỨC NĂNG CHÍNH

### 1. **QUẢN LÝ NGƯỜI DÙNG (User Management)**

#### 1.1. Đăng ký tài khoản
- Đăng ký với username, password, tên, tuổi
- Validation mật khẩu (tối thiểu 8 ký tự, không toàn số, không giống username)
- Kiểm tra tuổi hợp lệ (0-100)
- Kiểm tra username đã tồn tại
- Tự động đăng nhập sau khi đăng ký thành công

#### 1.2. Đăng nhập
- Xác thực username/password
- Tùy chọn "Nhớ tài khoản" (14 ngày)
- Redirect tự động:
  - Admin → `/admin/` (nếu là staff)
  - User thường → Trang đặt vé

#### 1.3. Đăng xuất
- Xóa session
- Redirect về trang chủ

#### 1.4. Quản lý tài khoản
- Xem thông tin cá nhân
- Xem lịch sử đặt vé
- Custom User Model với các trường: username, name, age

---

### 2. **QUẢN LÝ PHIM (Movie Management)**

#### 2.1. Danh sách phim
- Hiển thị tất cả phim
- Thông tin: tiêu đề, thể loại, đạo diễn, ngày phát hành, poster
- Mỗi phim có form đặt vé riêng

#### 2.2. Chi tiết phim
- Thông tin đầy đủ: mô tả, thời lượng, poster
- Danh sách suất chiếu của phim

#### 2.3. Quản lý phim (Admin)
- CRUD phim (Create, Read, Update, Delete)
- Upload poster phim
- Quản lý suất chiếu inline
- Thống kê số suất chiếu

---

### 3. **QUẢN LÝ SUẤT CHIẾU (Showtime Management)**

#### 3.1. Tạo suất chiếu
- Gán phim vào phòng chiếu
- Thiết lập thời gian bắt đầu/kết thúc
- Quản lý trạng thái (active/inactive)
- Tự động tính end_time dựa trên duration

#### 3.2. Lịch chiếu phim
- Trang hiển thị lịch chiếu
- Lọc theo ngày, phim, phòng

#### 3.3. Quản lý suất chiếu (Admin)
- Xem danh sách suất chiếu
- Thống kê ghế còn trống/đã đặt
- Biểu đồ trực quan về tình trạng ghế
- Lọc theo phim, phòng, ngày

#### 3.4. Management Command
- Command `create_showtimes`: Tạo suất chiếu tự động
- Tùy chọn số ngày và số suất chiếu mỗi phim

---

### 4. **QUẢN LÝ PHÒNG CHIẾU (Room Management)**

#### 4.1. Tạo phòng chiếu
- Đặt tên phòng (A, B, C...)
- Thiết lập sức chứa (capacity)
- Tự động tạo ghế khi tạo phòng (signal)

#### 4.2. Quản lý phòng (Admin)
- Xem danh sách phòng
- Thống kê số ghế, ghế còn trống
- Liên kết đến danh sách ghế

---

### 5. **QUẢN LÝ GHẾ (Seat Management)**

#### 5.1. Tự động tạo ghế
- Signal tự động tạo ghế khi tạo phòng
- Số ghế = capacity của phòng

#### 5.2. Trạng thái ghế
- Còn trống (is_available = True)
- Đã đặt (is_available = False)
- Tự động cập nhật khi đặt/hủy vé

#### 5.3. Chọn ghế
- Hiển thị sơ đồ ghế
- Đánh dấu ghế đã đặt
- Chọn nhiều ghế cùng lúc
- Validation ghế còn trống

---

### 6. **ĐẶT VÉ (Ticket Booking)**

#### 6.1. Quy trình đặt vé
1. Chọn phim từ danh sách
2. Chọn suất chiếu
3. Chọn loại vé (Người lớn/Trẻ em)
4. Chọn số lượng vé
5. Chọn ghế trên sơ đồ
6. Xác nhận thông tin
7. Thanh toán qua VNPay
8. Nhận vé sau thanh toán thành công

#### 6.2. Tính giá vé
- Người lớn: 100,000 VNĐ
- Trẻ em: 50,000 VNĐ
- Tự động tính tổng tiền

#### 6.3. Validation đặt vé
- Kiểm tra ghế còn trống
- Kiểm tra số lượng ghế = số lượng vé
- Kiểm tra ghế không trùng lặp
- Kiểm tra user đã đăng nhập

#### 6.4. Lưu thông tin đặt vé
- Lưu vào session trước khi thanh toán
- Tạo vé sau khi thanh toán thành công

---

### 7. **THANH TOÁN (Payment Integration)**

#### 7.1. Tích hợp VNPay
- Tích hợp VNPay Payment Gateway
- Hỗ trợ sandbox và production
- SHA512 hash validation
- IPN (Instant Payment Notification)

#### 7.2. Quy trình thanh toán
1. Lưu thông tin đặt vé vào session
2. Tạo order_id từ timestamp + user_id
3. Build payment URL với VNPay
4. Redirect đến VNPay
5. Xử lý kết quả thanh toán (payment_return)
6. IPN callback từ VNPay server
7. Tạo vé nếu thanh toán thành công

#### 7.3. Xử lý kết quả
- Response Code = '00': Thành công
- Tạo vé cho mỗi ghế đã chọn
- Cập nhật trạng thái ghế
- Xóa session booking_data

---

### 8. **QUẢN LÝ VÉ (Ticket Management)**

#### 8.1. Xem vé đã đặt
- Danh sách vé của user
- Thông tin: phim, phòng, ghế, suất chiếu, giá, loại vé
- Hiển thị thời gian chiếu

#### 8.2. Quản lý vé (Admin)
- Xem tất cả vé
- Lọc theo user, phim, phòng, ngày
- Tìm kiếm vé
- Thống kê doanh thu

---

### 9. **TRANG ADMIN (Django Admin)**

#### 9.1. Giao diện tùy chỉnh
- Header với gradient màu tím/xanh
- CSS tùy chỉnh với modern design
- Badge trạng thái màu sắc
- Thumbnail ảnh poster
- Biểu đồ trực quan

#### 9.2. Quản lý Models
- **CustomUser**: Quản lý người dùng
- **Movie**: Quản lý phim với inline showtimes
- **Showtime**: Quản lý suất chiếu với thống kê ghế
- **Room**: Quản lý phòng chiếu
- **Seat**: Quản lý ghế
- **Ticket**: Quản lý vé

#### 9.3. Tính năng Admin
- List display với format đẹp
- Filters và search
- Date hierarchy
- Pagination
- Readonly fields
- Inline editing

---

### 10. **TRANG GIAO DIỆN NGƯỜI DÙNG**

#### 10.1. Trang chủ (Homepage)
- Carousel hiển thị poster phim
- Thông báo COVID-19
- Modal đăng nhập/đăng ký
- Redirect đến trang đặt vé nếu đã login

#### 10.2. Danh sách phim
- Grid layout hiển thị phim
- Form đặt vé cho mỗi phim
- Chọn suất chiếu từ dropdown

#### 10.3. Chọn ghế
- Sơ đồ ghế trực quan
- Đánh dấu ghế đã đặt
- Chọn nhiều ghế
- AJAX load ghế theo suất chiếu

#### 10.4. Thanh toán
- Form thanh toán VNPay
- Hiển thị thông tin đặt vé
- Redirect đến VNPay

#### 10.5. Lịch sử đặt vé
- Danh sách vé đã đặt
- Thông tin chi tiết từng vé

---

## 🛠️ CÔNG NGHỆ VÀ THƯ VIỆN SỬ DỤNG

### **Backend Framework & Core**

#### 1. **Django 5.0.3**
- Web framework chính
- ORM (Object-Relational Mapping)
- Admin interface
- Authentication & Authorization
- Session management
- CSRF protection
- Middleware

#### 2. **Python**
- Ngôn ngữ lập trình chính
- Standard libraries: datetime, json, os, hmac, hashlib

---

### **Database**

#### 1. **SQLite3**
- Database mặc định cho development
- File-based database
- Không cần cấu hình server riêng

---

### **Frontend Technologies**

#### 1. **HTML5**
- Semantic HTML
- Template inheritance với Django

#### 2. **CSS3**
- Custom CSS cho từng trang
- Responsive design
- Modern styling với gradients, shadows
- Admin custom CSS

#### 3. **JavaScript**
- AJAX requests
- DOM manipulation
- Form handling
- Modal interactions

#### 4. **jQuery 3.6.4**
- JavaScript library
- DOM manipulation
- Event handling
- AJAX requests

#### 5. **DataTables 1.13.4**
- Hiển thị bảng dữ liệu với sorting, searching, pagination
- Tích hợp với Bootstrap 4
- Sử dụng trong trang quản lý vé đã đặt
- Tùy chỉnh ngôn ngữ tiếng Việt

#### 6. **Bootstrap 4.5.2**
- CDN Bootstrap từ stackpath.bootstrapcdn.com
- Grid system
- Components (modals, carousel, buttons, navbar)
- Responsive utilities
- Note: Crispy Forms sử dụng Bootstrap 5, nhưng templates chính dùng Bootstrap 4

---

### **Django Packages & Extensions**

#### 1. **django-crispy-forms 2.1**
- Render forms với Bootstrap styling
- Form layout helpers

#### 2. **crispy-bootstrap5 2024.2**
- Bootstrap 5 integration cho crispy-forms
- Modern form styling

#### 3. **django-filter 24.1**
- Advanced filtering trong admin
- Custom filter sets

#### 4. **django.contrib.humanize**
- Human-readable formatting
- Date/time formatting

#### 5. **Pillow 10.2.0**
- Image processing
- Upload và xử lý poster phim
- ImageField support

---

### **Payment Integration**

#### 1. **VNPay Payment Gateway**
- Tích hợp thanh toán trực tuyến
- SHA512 hash validation
- IPN (Instant Payment Notification)
- Sandbox và Production mode
- Custom vnpay.py module

---

### **Deployment & Production**

#### 1. **Gunicorn 21.2.0**
- WSGI HTTP Server
- Production-ready
- Process management

#### 2. **WhiteNoise 6.6.0**
- Static files serving
- CDN-like performance
- Compressed static files

#### 3. **Procfile**
- Heroku/Railway deployment config
- Process definitions

---

### **Security Features**

#### 1. **Django Security**
- CSRF protection
- XSS protection
- SQL injection prevention (ORM)
- Password hashing (PBKDF2)
- Session security

#### 2. **Authentication**
- Custom User Model
- Login/Logout
- Remember me (14 days session)
- Staff/Admin permissions

#### 3. **Payment Security**
- HMAC SHA512 hash
- Secure hash validation
- IPN verification

---

### **Django Features Used**

#### 1. **Models**
- Custom User Model (AbstractBaseUser)
- ForeignKey relationships
- OneToOneField
- AutoField
- ImageField
- DateTimeField
- BooleanField
- Choices field

#### 2. **Signals**
- `post_save` signal: Tự động tạo ghế khi tạo phòng
- `post_save` signal: Cập nhật trạng thái ghế khi tạo vé
- `post_delete` signal: Cập nhật trạng thái ghế khi xóa vé

#### 3. **Management Commands**
- Custom command: `create_showtimes`
- Tạo suất chiếu tự động với options

#### 4. **Admin Customization**
- Custom ModelAdmin classes
- Inline editing (ShowtimeInline)
- Custom list_display methods
- Format HTML trong admin
- Custom filters và search
- Date hierarchy
- Readonly fields

#### 5. **Forms**
- ModelForm
- Form validation
- Custom widgets
- Dynamic queryset

#### 6. **Views**
- Function-based views
- Class-based views (imported but not used)
- Decorators (@login_required, @csrf_exempt)
- JSON responses
- Session management

#### 7. **Templates**
- Template inheritance
- Template tags và filters
- Static files
- Context variables
- Conditional rendering

#### 8. **URLs**
- URL routing
- Named URLs
- RedirectView
- Static files serving

---

### **Development Tools**

#### 1. **Django Admin**
- Built-in admin interface
- Custom admin templates
- Custom admin CSS

#### 2. **Django Debug Toolbar** (có thể có)
- Debug và profiling

---

### **File Structure**

```
book_movie_ticket/
├── book_movie_ticket/          # Project settings
│   ├── settings.py             # Cấu hình chính
│   ├── urls.py                 # URL routing
│   ├── wsgi.py                 # WSGI config
│   └── asgi.py                 # ASGI config
├── book_movie_ticket_app/      # Main app
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # App URLs
│   ├── admin.py                # Admin configuration
│   ├── forms.py                # Form classes
│   ├── vnpay.py                # VNPay integration
│   ├── templates/              # HTML templates
│   ├── static/                 # CSS, JS, images
│   └── management/             # Custom commands
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django management
└── requirements.txt            # Dependencies
```

---

## 📊 TỔNG KẾT

### **Số lượng chức năng chính: 10**
1. Quản lý người dùng
2. Quản lý phim
3. Quản lý suất chiếu
4. Quản lý phòng chiếu
5. Quản lý ghế
6. Đặt vé
7. Thanh toán
8. Quản lý vé
9. Trang Admin
10. Giao diện người dùng

### **Công nghệ chính:**
- **Backend**: Django 5.0.3, Python
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Payment**: VNPay Gateway
- **Deployment**: Gunicorn, WhiteNoise
- **Extensions**: Crispy Forms, Pillow, django-filter

### **Tính năng nổi bật:**
✅ Tích hợp thanh toán VNPay  
✅ Quản lý ghế tự động  
✅ Admin interface tùy chỉnh đẹp mắt  
✅ Responsive design  
✅ Session management  
✅ Security features đầy đủ  
✅ Management commands  
✅ Signal handlers  

---

*Báo cáo được tạo tự động từ phân tích codebase*
