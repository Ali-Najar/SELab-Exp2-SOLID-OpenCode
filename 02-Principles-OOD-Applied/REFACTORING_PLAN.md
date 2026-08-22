# Refactoring Plan — SOLID Checkout

## هدف

اصلاح نقض‌های SRP، OCP، LSP، ISP و DIP در نسخه دوم پروژه، بدون اضافه‌کردن Cash در مرحله Refactoring. پس از تثبیت و Commit نسخه SOLID، Cash به‌عنوان یک extension مستقل اضافه می‌شود.

## تصمیم‌های تأییدشده

1. **LSP / BundleOrder — Substitution wins**  
   Bundle باید بر اساس آیتم‌های واقعی سفارش‌های داخلی قیمت‌گذاری شود. خروجی قبلی Order 103 که فقط `$5.00` بود ناشی از `items=[]` و یک رفتار معیوب بود. پس از اصلاح، subtotal برابر `$1,194.99`، تخفیف VIP برابر `$239.00`، shipping برابر `$0.00` و total برابر `$955.99` است.

2. **Storage naming**  
   نام `MySqlDatabase` و متدهای `save_order` / `load_order` برای حفظ سادگی پروژه باقی می‌مانند، اما کلاس قرارداد `OrderRepository` را پیاده‌سازی می‌کند.

3. **Discount precedence**  
   `if/elif` به Ruleهای مرتب‌شده تبدیل می‌شود، ولی ترتیب business rule نسخه اولیه حفظ می‌شود: VIP 20% سپس Bulk 10% و سپس `WELCOME10` 10%. فقط اولین Rule منطبق اعمال می‌شود.

4. **Avoid overengineering**  
   از DI Container، Service Locator یا Event Bus استفاده نمی‌شود. Constructor Injection و Composition Root ساده برای اندازه این پروژه کافی است.

5. **Cash after checkpoint**  
   Cash فقط پس از تثبیت نسخه SOLID اضافه می‌شود. در نسخه نهایی `CashPayment` یک Strategy جدید است و منطق dispatch در `PaymentProcessor` برای Cash تغییر نمی‌کند.

## مراحل Refactoring

1. ثبت و اجرای رفتار baseline؛
2. اصلاح `BundleOrder` برای رعایت قرارداد `Order`؛
3. استخراج `OrderValidator` و `DefaultOrderValidator`؛
4. استخراج `ShippingService` و `StandardShippingService`؛
5. استخراج `ReceiptPrinter` و `ConsoleReceiptPrinter`؛
6. تعریف abstractionهای Payment و تبدیل روش‌های پرداخت به Strategy؛
7. تبدیل منطق تخفیف به Ruleهای مستقل با first-match-wins؛
8. کوچک‌کردن interface اعلان به `Notifier.send()`؛
9. تعریف `OrderRepository` و تطبیق `MySqlDatabase` با آن؛
10. تزریق تمام dependencyها به `OrderService`؛
11. انتقال ساخت concrete implementationها به `main.py` به‌عنوان Composition Root؛
12. اضافه‌کردن regression testها؛
13. اجرای Demo و test suite؛
14. ثبت checkpoint نسخه SOLID قبل از Cash در Git؛
15. افزودن `CashPayment`، wiring و تست Cash در مرحله مستقل.

## ساختار اعمال‌شده

- `store/contracts.py` — `PaymentMethod`, `PaymentService`, `OrderValidator`, `ShippingService`, `Notifier`, `OrderRepository`, `ReceiptPrinter`
- `store/payment.py` — Strategyهای پرداخت و `PaymentProcessor`
- `store/pricing.py` — Ruleهای تخفیف و `RuleBasedDiscountCalculator`
- `store/notification.py` — `EmailNotifier`, `SmsNotifier`, `PushNotifier`
- `store/validation.py` — `DefaultOrderValidator`
- `store/shipping.py` — `StandardShippingService`
- `store/receipt.py` — `ConsoleReceiptPrinter`
- `store/storage.py` — `MySqlDatabase` به‌عنوان `OrderRepository`
- `store/order_service.py` — orchestration و dependency injection
- `store/main.py` — Composition Root و Demo

## اصلاحات انسانی روی خروجی Agent

- در تعارض بین حفظ `$5.00` برای Bundle و اصلاح LSP، گزینه Substitution انتخاب شد.
- یک نسخه میانی `main.py` شامل خطوط تکراری/ناقص بود و به‌صورت دستی اصلاح شد.
- Cash که در یک مرحله میانی زودتر از checkpoint وارد Demo شده بود موقتاً حذف شد تا ترتیب آزمایش حفظ شود.
- پس از مرحله مستقل Cash، Golden Demo برای خروجی نهایی آگاهانه به‌روزرسانی شد.

## Verification نهایی

از داخل پوشه `02-Principles-OOD-Applied`:

```powershell
py -B -m store.main
py -B -m unittest discover -s tests -v
```

مجموع regression testها در نسخه نهایی: **40 تست** و نتیجه نهایی **OK** است.
