# گزارش پرامپت‌های استفاده‌شده در آزمایش

## 1. افزودن Cash به نسخه اولیه، بدون Refactoring

**ابزار:** OpenCode  
**حالت:** Build پس از بررسی اولیه

```text
Analyze only the project inside 01-Principles-OOD-Without.

I need to add a new payment method named "cash".

Constraints:
- Do not refactor the architecture.
- Do not apply SOLID improvements.
- Make the minimum required changes.
- Preserve the existing design and coding style.
- First tell me exactly which files need to change and why.
- Do not touch 02-Principles-OOD-Applied.
```

### نتیجه و ارزیابی

در معماری اولیه برای اضافه‌کردن Cash لازم شد خود `PaymentProcessor` با یک شاخه `elif` جدید تغییر کند و یک سفارش Cash نیز در `main.py` برای نمایش قابلیت افزوده شود. این نتیجه به‌عنوان شاهد عملی نقض OCP ثبت شد.

---

## 2. تحلیل SOLID و تولید Plan

**ابزار:** OpenCode  
**حالت:** Plan

```text
Use the solid-review skill.

Analyze only the project inside 02-Principles-OOD-Applied.

Identify violations of:
- SRP
- OCP
- LSP
- ISP
- DIP

For every violation provide exact file and class evidence.

Then produce an ordered refactoring plan.

Constraints:
- Do not add cash payment yet.
- Preserve intended application behavior.
- Avoid overengineering.
- Keep OrderService as orchestration only.
- Make payment extensible without modifying PaymentProcessor for every new method.
- Make BundleOrder safely substitutable for Order.
- Do not force notifier implementations to support operations they cannot perform.
- High-level services should receive their dependencies instead of constructing concrete dependencies.

Do not edit source files yet.
```

### نتیجه و ارزیابی

Agent نقض‌های اصلی را در `OrderService`، `PaymentProcessor`، `DiscountCalculator`، `BundleOrder` و `NotificationService` شناسایی کرد. خروجی Plan قبل از اعمال تغییرات بررسی شد.

---

## 3. تصمیم درباره تعارض حفظ خروجی Baseline و اصلاح LSP

OpenCode هنگام اصلاح `BundleOrder` اعلام کرد که دو هدف با یکدیگر تعارض دارند: حفظ خروجی عددی قبلی Order 103 یا رعایت واقعی قابلیت جانشینی.

**تصمیم :**

```text
Substitution wins.
```

### دلیل تصمیم

خروجی قبلی Order 103 (`$5.00`) نتیجه خالی‌بودن `BundleOrder.items` بود و رفتار صحیح دامنه محسوب نمی‌شد. بنابراین اصلاح قرارداد `Order` بر حفظ خروجی معیوب اولویت داده شد. پس از اصلاح، Bundle بر اساس آیتم‌های واقعی سفارش‌های داخلی قیمت‌گذاری می‌شود.

---

## 4. اجرای Refactoring در Build Mode

**ابزار:** OpenCode  
**حالت:** Build

```text
Apply the approved SOLID refactoring plan now.

Target only:
02-Principles-OOD-Applied

Important decisions:
- Substitution wins for BundleOrder.
- Fix BundleOrder so it correctly satisfies the Order contract.
- It is acceptable that order 103 changes from the broken baseline total
  to the correct total based on its child items.
- Do not modify 01-Principles-OOD-Without.
- Do not add cash payment yet.

Apply the following refactorings:

1. SRP:
   Extract validation, shipping calculation and receipt printing
   from OrderService.

2. OCP:
   Replace PaymentProcessor if/elif dispatch with PaymentMethod strategies.
   Replace DiscountCalculator conditionals with ordered discount rules.

3. LSP:
   Make BundleOrder safely substitutable for Order.
   Remove BundleOrder-specific type checks from OrderService.

4. ISP:
   Replace the broad NotificationService with a small Notifier abstraction
   and separate EmailNotifier and SmsNotifier implementations.

5. DIP:
   Make OrderService depend on abstractions and inject its dependencies.
   Construct concrete dependencies only in main.py as the composition root.

6. Add regression tests.

After editing:
- run: py -m store.main
- run: py -m unittest discover -s tests -v

Report the exact files changed and the test results.

Do not add cash yet.
```

### اصلاح انسانی خروجی Agent

در یک خروجی میانی، `main.py` به‌علت هم‌پوشانی چند ویرایش شامل خطوط تکراری و ناقص شد. فایل به‌صورت دستی بازبینی و Composition Root به شکل صحیح بازسازی شد. همچنین Cash تا زمان ثبت checkpoint نسخه SOLID از Demo حذف شد.

---

## 5. افزودن Cash پس از Refactoring

**ابزار:** OpenCode  
**حالت:** Build

```text
Now add the same cash payment capability to
02-Principles-OOD-Applied.

Constraints:
- Do not add an if/elif branch to PaymentProcessor.
- Extend the existing payment abstraction.
- Keep PaymentProcessor unchanged.
- Add a test for cash.
- Update only composition wiring where required.
- First explain which files need to change.
- Do not touch 01-Principles-OOD-Without.
```

### نتیجه و ارزیابی

`CashPayment` به‌عنوان یک Strategy جدید از `PaymentMethod` پیاده‌سازی شد و بدون افزودن شرط جدید به منطق `PaymentProcessor` قابل ثبت است. تست‌های مستقل Cash نیز به مجموعه تست‌ها افزوده شدند.

---

## 6. بررسی و اصلاح تست Golden Demo

پس از اضافه‌شدن Cash به Demo نهایی، تست Golden که هنوز خروجی نسخه قبل از Cash را انتظار داشت شکست خورد. علت شکست با بررسی diff خروجی مشخص شد و پس از اطمینان از عمدی‌بودن قابلیت Cash در نسخه نهایی، expected output تست نیز به‌روزرسانی شد.

---

## 7. استفاده از ChatGPT در کنار OpenCode

**ابزار:** ChatGPT  
**مدل:** GPT-5.6 Sol

ChatGPT برای موارد زیر استفاده شد:

- استخراج الزامات دو فایل دستورالعمل آزمایشگاه؛
- طراحی ترتیب انجام پروژه در Windows/PowerShell؛
- توضیح تفاوت Plan و Build در OpenCode؛
- بررسی تصمیم LSP مربوط به `BundleOrder`؛
- تحلیل failure تست Golden Demo؛
- بازسازی `main.py` خراب‌شده در یک مرحله میانی؛
- بررسی ساختار نهایی پروژه، تست‌ها و تهیه گزارش فارسی.

