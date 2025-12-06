# 🎬 Bắt đầu Deploy lên Railway

## ✅ Đã chuẩn bị xong

Code đã được commit và sẵn sàng để push lên GitHub!

## 📋 Checklist các bước tiếp theo

### Bước 1: Tạo GitHub Repository
- [ ] Truy cập: https://github.com/new
- [ ] Tạo repository mới (ví dụ: `cinema-booking-django`)
- [ ] Copy URL repository (ví dụ: `https://github.com/YOUR_USERNAME/cinema-booking-django.git`)

### Bước 2: Push Code lên GitHub
Chạy các lệnh sau (thay `YOUR_USERNAME` và `REPO_NAME`):

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

**Lưu ý**: Nếu GitHub yêu cầu authentication:
- Tạo Personal Access Token: GitHub → Settings → Developer settings → Personal access tokens → Generate new token
- Hoặc sử dụng GitHub Desktop

### Bước 3: Deploy lên Railway
- [ ] Truy cập: https://railway.app/
- [ ] Login với GitHub account
- [ ] Click **"New Project"** → **"Deploy from GitHub repo"**
- [ ] Chọn repository vừa tạo
- [ ] Đợi Railway deploy (2-5 phút)

### Bước 4: Cấu hình Environment Variables
Trong Railway → Service → Variables, thêm các biến sau:

```
SECRET_KEY=<tạo key mới - xem hướng dẫn bên dưới>
DEBUG=False
ALLOWED_HOSTS=terrzcinema.com,www.terrzcinema.com,*.railway.app
DOMAIN=https://terrzcinema.com
VNPAY_TMN_CODE=ITNQNTND
VNPAY_HASH_SECRET_KEY=SPAW62QPK9VRKYN4LIK7L3S1R32FJJIT
USE_SANDBOX=True
```

**Tạo SECRET_KEY mới:**
```bash
python manage.py shell
# Trong shell:
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
# Copy key và dùng cho biến SECRET_KEY
```

### Bước 5: Chạy Migrations
Trong Railway Console (Service → Deployments → View Logs → Open Console):

```bash
cd book_movie_ticket
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### Bước 6: Cấu hình Domain
- [ ] Railway → Settings → Domains
- [ ] Click **"Custom Domain"**
- [ ] Nhập: `terrzcinema.com`
- [ ] Cấu hình DNS theo hướng dẫn Railway
- [ ] Đợi DNS propagate (5 phút - 48 giờ)

### Bước 7: Cập nhật VNPay
- [ ] Đăng nhập: https://sandbox.vnpayment.vn/merchantv2/
- [ ] Cập nhật IPN URL: `https://terrzcinema.com/payment-ipn/`
- [ ] Cập nhật Return URL: `https://terrzcinema.com/payment-return/`

### Bước 8: Test
- [ ] Truy cập: `https://terrzcinema.com`
- [ ] Test đăng nhập/đăng ký
- [ ] Test đặt vé và thanh toán VNPay

---

## 📚 Tài liệu chi tiết

- **Hướng dẫn đầy đủ**: Xem file `RAILWAY_DEPLOY_GUIDE.md`
- **Quick Start**: Xem file `QUICK_START.md`
- **Tổng quan deploy**: Xem file `DEPLOY.md`

## ⚠️ Lưu ý quan trọng

1. **SECRET_KEY**: Luôn tạo key mới cho production
2. **DEBUG**: Phải đặt `False` trong production
3. **Domain**: Đợi DNS propagate trước khi test
4. **VNPay**: Cập nhật URLs trong merchant admin sau khi có domain

## 🆘 Gặp vấn đề?

1. Kiểm tra logs trong Railway dashboard
2. Kiểm tra Environment Variables đã đúng chưa
3. Kiểm tra DNS đã propagate: https://dnschecker.org/
4. Xem phần Troubleshooting trong `RAILWAY_DEPLOY_GUIDE.md`

---

**Chúc bạn deploy thành công! 🎉**

