# گزارش تست و Verification

## دستورات اجرا در Windows / PowerShell

نسخه بدون SOLID:

```powershell
cd .\01-Principles-OOD-Without
py -B -m store.main
```

نسخه SOLID:

```powershell
cd .\02-Principles-OOD-Applied
py -B -m store.main
py -B -m unittest discover -s tests -v
```

## نتیجه تست نسخه SOLID

مجموع تست‌ها: **40**  
نتیجه نهایی: **همه تست‌ها Pass شدند (`OK`)**.

| فایل تست | تعداد تست | موضوع |
|---|---:|---|
| `test_golden_demo.py` | 1 | تطبیق کامل خروجی Demo نهایی |
| `test_models.py` | 4 | رفتار `BundleOrder` و قابلیت جانشینی |
| `test_notification.py` | 4 | استقلال Email/SMS/Push notifierها |
| `test_order_service.py` | 6 | جریان Checkout، persistence، notify و shipping |
| `test_payment.py` | 7 | Strategyهای پرداخت، Cash و روش‌های قابل توسعه |
| `test_pricing.py` | 10 | Ruleهای تخفیف و تقدم قوانین |
| `test_storage.py` | 3 | ذخیره و بازیابی سفارش |
| `test_validation.py` | 5 | اعتبارسنجی Order و Bundle |
| **جمع** | **40** | |

## خروجی‌های کلیدی Demo

### نسخه بدون SOLID

- Order 101: مبلغ نهایی `819.99` دلار.
- Order 103 (Bundle): به دلیل نقض LSP، subtotal صفر و مبلغ نهایی فقط `5.00` دلار است.
- Order 104 (Cash): مبلغ کالا `30.00` دلار + ارسال `5.00` دلار = `35.00` دلار.

### نسخه SOLID نهایی

- Order 101: مبلغ نهایی همچنان `819.99` دلار.
- Order 103: subtotal واقعی `1194.99` دلار، تخفیف VIP برابر `239.00` دلار و مبلغ نهایی `955.99` دلار.
- Order 104 (Cash): مبلغ نهایی `35.00` دلار.

## تفسیر تغییر Order 103

تفاوت Order 103 یک Regression ناخواسته نیست. در نسخه اولیه، `BundleOrder` از `Order` ارث می‌برد اما `items` را خالی نگه می‌داشت. پس از اصلاح LSP، آیتم‌های سفارش‌های داخلی Bundle در `items` نمایان می‌شوند و pricing/validation بدون special case کار می‌کنند.

## Golden Test

`test_golden_demo.py` خروجی کامل برنامه نهایی را بررسی می‌کند. این تست علاوه بر جلوگیری از تغییرهای ناخواسته، رفتار اصلاح‌شده Bundle و قابلیت Cash در Demo نهایی را نیز تثبیت می‌کند.
