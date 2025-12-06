# 🚀 Quick Start - Deploy lên Railway

## Bước 1: Push Code lên GitHub

```bash
# Thêm remote (thay YOUR_USERNAME và REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push code
git branch -M main
git push -u origin main
```

## Bước 2: Deploy lên Railway

1. Truy cập: https://railway.app/
2. Login với GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Chọn repository của bạn

## Bước 3: Thêm Environment Variables

Trong Railway → Service → Variables, thêm:

```
SECRET_KEY=<tạo key mới>
DEBUG=False
ALLOWED_HOSTS=terrzcinema.com,www.terrzcinema.com,*.railway.app
DOMAIN=https://terrzcinema.com
VNPAY_TMN_CODE=ITNQNTND
VNPAY_HASH_SECRET_KEY=SPAW62QPK9VRKYN4LIK7L3S1R32FJJIT
USE_SANDBOX=True
```

## Bước 4: Chạy Migrations

Railway Console → chạy:
```bash
cd book_movie_ticket
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

## Bước 5: Cấu hình Domain

1. Railway → Settings → Domains
2. Thêm custom domain: `terrzcinema.com`
3. Cấu hình DNS theo hướng dẫn

## Bước 6: Cập nhật VNPay

VNPay Merchant Admin:
- IPN URL: `https://terrzcinema.com/payment-ipn/`
- Return URL: `https://terrzcinema.com/payment-return/`

---

**Xem hướng dẫn chi tiết trong file `RAILWAY_DEPLOY_GUIDE.md`**

