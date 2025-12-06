# 🚀 Hướng dẫn Deploy lên Railway - Step by Step

## Bước 1: Tạo GitHub Repository và Push Code

### 1.1. Tạo Repository trên GitHub

1. Truy cập: https://github.com/new
2. Điền thông tin:
   - **Repository name**: `cinema-booking-django` (hoặc tên bạn muốn)
   - **Description**: "Cinema Booking Django App with VNPay"
   - **Visibility**: Public hoặc Private (tùy bạn)
   - **KHÔNG** tích vào "Initialize this repository with a README"
3. Click **"Create repository"**

### 1.2. Push Code lên GitHub

Sau khi tạo repository, GitHub sẽ hiển thị hướng dẫn. Bạn đã có code sẵn rồi, nên chạy các lệnh sau:

```bash
# Thêm remote repository (thay YOUR_USERNAME và YOUR_REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Đổi tên branch thành main (nếu cần)
git branch -M main

# Push code lên GitHub
git push -u origin main
```

**Lưu ý**: 
- Thay `YOUR_USERNAME` bằng username GitHub của bạn
- Thay `YOUR_REPO_NAME` bằng tên repository bạn vừa tạo
- Nếu GitHub yêu cầu authentication, bạn có thể cần:
  - Tạo Personal Access Token (Settings → Developer settings → Personal access tokens)
  - Hoặc sử dụng GitHub Desktop

---

## Bước 2: Đăng ký và Đăng nhập Railway

1. Truy cập: https://railway.app/
2. Click **"Start a New Project"** hoặc **"Login"**
3. Chọn **"Login with GitHub"**
4. Authorize Railway để truy cập GitHub repositories

---

## Bước 3: Deploy từ GitHub

1. Sau khi đăng nhập, click **"New Project"**
2. Chọn **"Deploy from GitHub repo"**
3. Chọn repository `cinema-booking-django` (hoặc tên bạn đã tạo)
4. Railway sẽ tự động:
   - Detect Django project
   - Cài đặt dependencies
   - Deploy app

**Lưu ý**: Lần đầu deploy có thể mất 2-5 phút

---

## Bước 4: Cấu hình Environment Variables

1. Trong Railway project, click vào service (thường là tên repository)
2. Vào tab **"Variables"**
3. Click **"New Variable"** và thêm từng biến sau:

### Biến bắt buộc:

```
SECRET_KEY=django-insecure-)h29&bzb3wo$xao$m!bndr=t=w-bg=#5#)2+8hya1l!6zt+i*$
```

**⚠️ QUAN TRỌNG**: Tạo SECRET_KEY mới cho production:
- Vào Django shell: `python manage.py shell`
- Chạy: `from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())`
- Copy key và dùng cho biến SECRET_KEY

```
DEBUG=False
```

```
ALLOWED_HOSTS=terrzcinema.com,www.terrzcinema.com,*.railway.app
```

```
DOMAIN=https://terrzcinema.com
```

```
VNPAY_TMN_CODE=ITNQNTND
```

```
VNPAY_HASH_SECRET_KEY=SPAW62QPK9VRKYN4LIK7L3S1R32FJJIT
```

```
USE_SANDBOX=True
```

### Sau khi thêm xong:
- Railway sẽ tự động redeploy
- Đợi deploy xong (có thể mất 1-2 phút)

---

## Bước 5: Chạy Migrations và Tạo Superuser

### 5.1. Mở Railway Console

1. Trong Railway project, click vào service
2. Vào tab **"Deployments"**
3. Click vào deployment mới nhất
4. Click **"View Logs"** hoặc tìm nút **"Open Console"**

### 5.2. Chạy Migrations

Trong console, chạy:

```bash
cd book_movie_ticket
python manage.py migrate
```

### 5.3. Tạo Superuser

```bash
python manage.py createsuperuser
```

Nhập:
- Username: `admin` (hoặc tên bạn muốn)
- Email: (có thể bỏ qua)
- Password: (nhập password mạnh)

### 5.4. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

---

## Bước 6: Cấu hình Domain

### 6.1. Lấy Railway Domain (Tạm thời)

1. Trong Railway project, vào tab **"Settings"**
2. Scroll xuống phần **"Domains"**
3. Click **"Generate Domain"**
4. Copy domain được tạo (ví dụ: `cinema-booking-production.up.railway.app`)

### 6.2. Cấu hình Custom Domain (terrzcinema.com)

1. Trong phần **"Domains"**, click **"Custom Domain"**
2. Nhập: `terrzcinema.com`
3. Railway sẽ hiển thị thông tin DNS cần cấu hình

### 6.3. Cấu hình DNS

1. Đăng nhập vào nhà cung cấp domain của bạn (nơi bạn mua domain terrzcinema.com)
2. Vào phần quản lý DNS
3. Thêm CNAME record:
   - **Name**: `@` hoặc `terrzcinema.com`
   - **Value**: Domain Railway cung cấp (ví dụ: `cinema-booking-production.up.railway.app`)
   - **TTL**: 3600 (hoặc mặc định)

4. Thêm CNAME cho www:
   - **Name**: `www`
   - **Value**: Domain Railway cung cấp
   - **TTL**: 3600

### 6.4. Đợi DNS Propagate

- DNS có thể mất 5 phút đến 48 giờ để propagate
- Kiểm tra: https://dnschecker.org/
- Nhập `terrzcinema.com` và kiểm tra CNAME record

### 6.5. Railway sẽ tự động cấu hình SSL

- Sau khi DNS propagate, Railway sẽ tự động cài SSL certificate
- Đợi 5-10 phút sau khi DNS đã propagate

---

## Bước 7: Cập nhật VNPay Merchant Admin

1. Đăng nhập: https://sandbox.vnpayment.vn/merchantv2/
2. Vào phần **"Cấu hình"** hoặc **"Settings"**
3. Cập nhật:
   - **IPN URL**: `https://terrzcinema.com/payment-ipn/`
   - **Return URL**: `https://terrzcinema.com/payment-return/`
4. Lưu cấu hình

---

## Bước 8: Kiểm tra và Test

### 8.1. Kiểm tra Website

1. Truy cập: `https://terrzcinema.com`
2. Kiểm tra:
   - Trang chủ load được
   - Đăng nhập/Đăng ký hoạt động
   - Danh sách phim hiển thị
   - Admin panel: `https://terrzcinema.com/admin`

### 8.2. Test Thanh toán VNPay

1. Đăng nhập vào website
2. Chọn phim và đặt vé
3. Thử thanh toán qua VNPay
4. Kiểm tra:
   - Redirect đến VNPay thành công
   - Thanh toán thành công
   - Quay lại website và tạo vé thành công

---

## Troubleshooting

### Lỗi: "Application Error"

1. Kiểm tra **Logs** trong Railway:
   - Vào tab **"Deployments"** → Click deployment → **"View Logs"**
2. Kiểm tra Environment Variables đã đúng chưa
3. Kiểm tra migrations đã chạy chưa

### Lỗi: "Static files not found"

Chạy lại:
```bash
python manage.py collectstatic --noinput
```

### Lỗi: "Database error"

Chạy migrations:
```bash
python manage.py migrate
```

### Lỗi: "VNPay IPN not working"

1. Kiểm tra domain đã được cấu hình đúng trong VNPay merchant admin
2. Kiểm tra SSL certificate đã được cài đặt (phải có HTTPS)
3. Kiểm tra logs trong Railway để xem request từ VNPay

### Lỗi: "Domain not working"

1. Kiểm tra DNS đã propagate chưa: https://dnschecker.org/
2. Kiểm tra CNAME record đã đúng chưa
3. Đợi thêm thời gian (có thể mất đến 48 giờ)

---

## Các lệnh hữu ích trong Railway Console

```bash
# Xem logs
# (Trong Railway dashboard → Deployments → View Logs)

# Chạy migrations
cd book_movie_ticket
python manage.py migrate

# Tạo superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Tạo showtimes (nếu cần)
python manage.py create_showtimes

# Django shell
python manage.py shell
```

---

## Lưu ý quan trọng

1. **SECRET_KEY**: Luôn tạo key mới cho production, không dùng key mặc định
2. **DEBUG**: Luôn đặt `False` trong production
3. **Database**: Railway sử dụng PostgreSQL (miễn phí), không phải SQLite
4. **Static Files**: Railway tự động serve static files qua WhiteNoise
5. **Media Files**: Cần cấu hình storage (S3, Cloudinary) cho production
6. **VNPay**: Khi chuyển sang production, cập nhật:
   - `USE_SANDBOX=False`
   - Thông tin VNPay production từ merchant admin

---

## Hỗ trợ

Nếu gặp vấn đề:
1. Kiểm tra logs trong Railway dashboard
2. Kiểm tra Environment Variables
3. Kiểm tra DNS và domain configuration
4. Tham khảo: https://docs.railway.app/

Chúc bạn deploy thành công! 🎉

