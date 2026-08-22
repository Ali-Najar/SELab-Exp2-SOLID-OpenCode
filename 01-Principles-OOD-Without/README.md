# نسخه 01 — بدون اعمال اصول SOLID

این پوشه نسخه اولیه پروژه را نگه می‌دارد که قابلیت **پرداخت نقدی (Cash)** با کمترین تغییر و بدون Refactoring معماری به آن اضافه شده است.

## اجرا در Windows / PowerShell

```powershell
cd .\01-Principles-OOD-Without
py -B -m store.main
```

## تغییرات لازم برای Cash

### `store/payment.py`

یک شاخه جدید به `PaymentProcessor.process()` اضافه شده است:

```python
elif method == "cash":
    print(f"[payment] Cash payment {amount:.2f}")
    return f"paid_by_cash:{amount:.2f}"
```

### `store/main.py`

یک سفارش جدید با `payment_method="cash"` ساخته و در Demo اجرا شده است.

## نتیجه مهم این مرحله

افزودن روش جدید پرداخت مستلزم **تغییر مستقیم منطق موجود `PaymentProcessor`** بود. این موضوع شاهد عملی نقض اصل Open/Closed است.

## نقض‌های شناخته‌شده SOLID در این نسخه

- **SRP:** `OrderService` چند مسئولیت مستقل دارد.
- **OCP:** `PaymentProcessor` و `DiscountCalculator` برای توسعه رفتار جدید باید تغییر کنند.
- **LSP:** `BundleOrder` با `items=[]` قرارداد `Order` را درست رعایت نمی‌کند.
- **ISP:** `SmsOnlyNotifier` به عملیات email/push وابسته شده و برای آن‌ها exception می‌دهد.
- **DIP:** `OrderService` وابستگی‌های concrete خود را مستقیماً می‌سازد.

## خروجی شاخص

در این نسخه، Order 103 به دلیل مشکل `BundleOrder` فقط `5.00` دلار محاسبه می‌شود. این رفتار عمداً در نسخه اول دست‌نخورده مانده تا اثر Refactoring در نسخه دوم قابل مشاهده باشد.
