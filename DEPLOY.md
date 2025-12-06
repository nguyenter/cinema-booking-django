# Hướng dẫn Deploy Cinema Booking Django lên Production

## ⚠️ Lưu ý quan trọng

**GitHub không thể host Django app trực tiếp.** Bạn cần deploy lên các platform khác như:
- **Railway** (miễn phí, dễ dùng) - Khuyến nghị
- **Render** (miễn phí)
- **Heroku** (có phí)
- **PythonAnywhere** (miễn phí)
- **VPS/Cloud Server** (DigitalOcean, AWS, etc.)

## Các bước chuẩn bị

### 1. Push code lên GitHub

```bash
# Khởi tạo git (nếu chưa có)
git init

# Thêm remote repository
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Thêm tất cả files
git add .

# Commit
git commit -m "Initial commit - Cinema Booking Django App"

# Push lên GitHub
git push -u origin main
```

### 2. Cấu hình Domain với VNPay

1. Đăng nhập vào VNPay Merchant Admin: https://sandbox.vnpayment.vn/merchantv2/
2. Cập nhật **IPN URL** thành: `https://terrzcinema.com/payment-ipn/`
3. Cập nhật **Return URL** thành: `https://terrzcinema.com/payment-return/`

## Deploy lên Railway (Khuyến nghị - Miễn phí)

### Bước 1: Tạo tài khoản Railway
1. Truy cập: https://railway.app/
2. Đăng ký bằng GitHub account

### Bước 2: Deploy từ GitHub
1. Click "New Project"
2. Chọn "Deploy from GitHub repo"
3. Chọn repository của bạn
4. Railway sẽ tự động detect Django và deploy

### Bước 3: Cấu hình Environment Variables
Trong Railway dashboard, thêm các biến môi trường:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=terrzcinema.com,www.terrzcinema.com
DOMAIN=https://terrzcinema.com
VNPAY_TMN_CODE=ITNQNTND
VNPAY_HASH_SECRET_KEY=SPAW62QPK9VRKYN4LIK7L3S1R32FJJIT
USE_SANDBOX=True
```

### Bước 4: Cấu hình Domain
1. Trong Railway project, vào "Settings"
2. Click "Generate Domain" để có domain miễn phí
3. Hoặc thêm custom domain `terrzcinema.com`:
   - Thêm CNAME record trong DNS provider trỏ đến Railway domain
   - Railway sẽ tự động cấu hình SSL

### Bước 5: Chạy migrations
Trong Railway, mở "Deploy Logs" và chạy:
```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

## Deploy lên Render (Miễn phí)

### Bước 1: Tạo tài khoản
1. Truy cập: https://render.com/
2. Đăng ký bằng GitHub

### Bước 2: Tạo Web Service
1. Click "New +" → "Web Service"
2. Connect GitHub repository
3. Cấu hình:
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn book_movie_ticket.wsgi:application`

### Bước 3: Environment Variables
Thêm các biến môi trường giống như Railway

### Bước 4: Custom Domain
1. Vào "Settings" → "Custom Domains"
2. Thêm `terrzcinema.com`
3. Cấu hình DNS theo hướng dẫn

## Deploy lên PythonAnywhere (Miễn phí)

### Bước 1: Tạo tài khoản
1. Truy cập: https://www.pythonanywhere.com/
2. Đăng ký tài khoản miễn phí

### Bước 2: Upload code
1. Mở Bash console
2. Clone repository:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### Bước 3: Cài đặt dependencies
```bash
pip3.10 install --user -r requirements.txt
```

### Bước 4: Cấu hình Web App
1. Vào "Web" tab
2. Click "Add a new web app"
3. Chọn "Manual configuration" → Python 3.10
4. Cấu hình WSGI file:
```python
import os
import sys

path = '/home/YOUR_USERNAME/YOUR_REPO_NAME'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'book_movie_ticket.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Bước 5: Environment Variables
Trong Web app settings, thêm các biến môi trường

### Bước 6: Static files
Trong Web app settings:
- Static files URL: `/static/`
- Static files directory: `/home/YOUR_USERNAME/YOUR_REPO_NAME/staticfiles`

## Sau khi deploy

### 1. Chạy migrations
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### 2. Tạo superuser
```bash
python manage.py createsuperuser
```

### 3. Tạo showtimes (nếu cần)
```bash
python manage.py create_showtimes
```

### 4. Kiểm tra
- Truy cập: `https://terrzcinema.com`
- Kiểm tra admin: `https://terrzcinema.com/admin`
- Test thanh toán VNPay

## Lưu ý bảo mật

1. **SECRET_KEY**: Tạo key mới cho production:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

2. **DEBUG**: Luôn đặt `DEBUG=False` trong production

3. **ALLOWED_HOSTS**: Chỉ thêm domain của bạn

4. **VNPay**: Khi chuyển sang production, cập nhật:
   - `USE_SANDBOX=False`
   - `VNPAY_PAYMENT_URL` thành production URL
   - Thông tin VNPay production từ merchant admin

## Troubleshooting

### Lỗi static files
```bash
python manage.py collectstatic --noinput
```

### Lỗi database
```bash
python manage.py migrate
```

### Lỗi VNPay IPN
- Kiểm tra domain đã được cấu hình đúng trong VNPay merchant admin
- Kiểm tra SSL certificate (phải có HTTPS)
- Kiểm tra firewall không chặn request từ VNPay

## Hỗ trợ

Nếu gặp vấn đề, kiểm tra:
- Logs trong platform dashboard
- Django logs: `python manage.py runserver` (local)
- VNPay merchant admin để xem transaction logs

