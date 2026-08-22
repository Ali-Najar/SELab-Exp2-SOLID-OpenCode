# گزارش آزمایش دوم آزمایشگاه مهندسی نرم‌افزار

## مروری بر اصول طراحی شی‌گرا (SOLID) و استفاده از OpenCode

**نام دانشجو:** Ali Najar  
**شماره دانشجویی:** **401102701**  
---

## 1. هدف آزمایش

این آزمایش با دو هدف اصلی انجام شد:

1. بررسی عملی اصول طراحی شی‌گرای **SOLID**، شناسایی موارد نقض و اصلاح آن‌ها با Refactoring؛
2. استفاده از **OpenCode** به‌عنوان AI Coding Agent برای تحلیل، برنامه‌ریزی و اعمال کنترل‌شده تغییرات، همراه با ارزیابی انسانی خروجی Agent.

برای مشاهده عملی اثر SOLID بر توسعه‌پذیری، قابلیت **پرداخت نقدی (Cash)** دو بار پیاده‌سازی شد:

- یک بار روی معماری اولیه و بدون Refactoring؛
- یک بار پس از اصلاح معماری بر اساس SOLID.

سپس نوع و دامنه تغییرات لازم در دو حالت مقایسه شد.

---

## 2. ساختار Repository

```text
SELab-Exp2-SOLID-OpenCode/
│
├── README.md
├── AGENTS.md
├── .gitignore
│
├── docs/
│   ├── PROMPTS.md
│   ├── AI_USAGE.md
│   └── TEST_REPORT.md
│
├── 01-Principles-OOD-Without/
│   ├── README.md
│   └── store/
│       ├── main.py
│       ├── models.py
│       ├── notification.py
│       ├── order_service.py
│       ├── payment.py
│       ├── pricing.py
│       └── storage.py
│
└── 02-Principles-OOD-Applied/
    ├── README.md
    ├── REFACTORING_PLAN.md
    ├── .opencode/
    │   └── skills/
    │       └── solid-review/
    │           └── SKILL.md
    ├── store/
    │   ├── contracts.py
    │   ├── main.py
    │   ├── models.py
    │   ├── notification.py
    │   ├── order_service.py
    │   ├── payment.py
    │   ├── pricing.py
    │   ├── receipt.py
    │   ├── shipping.py
    │   ├── storage.py
    │   └── validation.py
    └── tests/
        ├── test_golden_demo.py
        ├── test_models.py
        ├── test_notification.py
        ├── test_order_service.py
        ├── test_payment.py
        ├── test_pricing.py
        ├── test_storage.py
        └── test_validation.py
```

دو نسخه از یک مسئله نگهداری شده است:

- `01-Principles-OOD-Without`: معماری اولیه + Cash بدون اعمال SOLID؛
- `02-Principles-OOD-Applied`: معماری Refactorشده + Cash به‌صورت extension.

---

## 3. محیط اجرا و دستورات

### نسخه بدون SOLID

```powershell
cd .\01-Principles-OOD-Without
py -B -m store.main
```

### نسخه SOLID

```powershell
cd .\02-Principles-OOD-Applied
py -B -m store.main
```

### اجرای تست‌ها

```powershell
py -B -m unittest discover -s tests -v
```

---

# بخش اول — افزودن قابلیت Cash به نسخه اولیه

## 4. محدودیت مرحله اول

در این مرحله ساختار پروژه عمداً Refactor نشد. هدف این بود که مشخص شود افزودن یک روش پرداخت جدید به معماری اولیه دقیقاً کدام قسمت‌های موجود را مجبور به تغییر می‌کند.

نسخه مربوط به این مرحله در پوشه زیر قرار دارد:

```text
01-Principles-OOD-Without/
```

---

## 5. پیاده‌سازی Cash در نسخه غیر SOLID

### 5.1 تغییر `store/payment.py`

کلاس `PaymentProcessor` در نسخه اولیه نوع پرداخت را با مجموعه‌ای از `if/elif`ها تشخیص می‌دهد. برای Cash یک branch جدید به همان متد اضافه شد:

```python
elif method == "cash":
    print(f"[payment] Cash payment {amount:.2f}")
    return f"paid_by_cash:{amount:.2f}"
```

این تغییر نشان می‌دهد برای اضافه‌کردن یک روش پرداخت جدید باید منطق موجود Processor ویرایش شود.

### 5.2 تغییر `store/main.py`

یک سفارش جدید برای نمایش Cash ساخته شد:

```python
cash_order = Order(
    id=104,
    customer=regular,
    payment_method="cash",
    items=[OrderItem(5, "Notebook", 15.00, 2)],
)
```

و سپس در Demo اجرا شد:

```python
service.process_order(cash_order)
```

---

## 6. جدول تغییرات مرحله اول

| ردیف | فایل / کلاس | نوع تغییر | توضیح و علت ضرورت |
|---:|---|---|---|
| 1 | `store/payment.py` / `PaymentProcessor` | افزودن شرط جدید | برای اینکه Processor روش `cash` را بشناسد، یک `elif` جدید به منطق موجود اضافه شد. |
| 2 | `store/main.py` | افزودن داده و اجرای Demo | یک `Order` با `payment_method="cash"` اضافه شد تا قابلیت جدید در اجرای برنامه قابل مشاهده باشد. |

### نتیجه عملی

برای افزودن Cash، بخشی از **منطق مرکزی پرداخت موجود** تغییر کرد. این مشاهده بعداً به‌عنوان شاهد عملی نقض OCP استفاده شد.

---

## 7. خروجی مهم نسخه اولیه

برای Cash، سفارش شماره 104 شامل دو Notebook به قیمت مجموع 30 دلار است. چون subtotal کمتر از 100 دلار است، 5 دلار Shipping نیز اضافه می‌شود:

```text
Subtotal  = $30.00
Shipping  = $5.00
Total     = $35.00
Payment   = paid_by_cash:35.00
```

در همین نسخه Order 103 که یک `BundleOrder` است به‌صورت زیر محاسبه می‌شود:

```text
Subtotal = $0.00
Shipping = $5.00
Total    = $5.00
```

این خروجی نتیجه طراحی `BundleOrder` در نسخه اولیه است و در بخش LSP تحلیل می‌شود.

---

# بخش دوم — تحلیل اصول SOLID

## 8. جدول کلی تحلیل

| اصل | رعایت شده؟ | محل اصلی در نسخه اولیه | خلاصه مشکل |
|---|---|---|---|
| SRP | خیر | `OrderService` | یک کلاس هم‌زمان validation، pricing، shipping، payment، persistence، notification و receipt را مدیریت می‌کند. |
| OCP | خیر | `PaymentProcessor` | روش پرداخت جدید نیازمند ویرایش `if/elif` موجود است. |
| OCP | خیر | `DiscountCalculator` | افزودن/تغییر قانون تخفیف نیازمند ویرایش زنجیره شرط‌هاست. |
| LSP | خیر | `BundleOrder` | subtype قرارداد `Order.items/subtotal/item_count` را به‌شکل قابل جانشینی رعایت نمی‌کند. |
| ISP | خیر | `NotificationService` / `SmsOnlyNotifier` | notifier فقط-SMS مجبور است عملیات email و push را نیز به ارث ببرد. |
| DIP | خیر | `OrderService` | سرویس سطح بالا concrete dependencyهای خود را مستقیماً ایجاد می‌کند. |

---

## 9. SRP — Single Responsibility Principle

### محل نقض

`01-Principles-OOD-Without/store/order_service.py`

### علت نقض

`OrderService` در نسخه اولیه هم‌زمان مسئول موارد زیر است:

- اعتبارسنجی سفارش؛
- محاسبه تخفیف؛
- محاسبه Shipping؛
- انجام Payment؛
- تغییر وضعیت و ذخیره سفارش؛
- ارسال Email و SMS؛
- چاپ Receipt.

در نتیجه کلاس بیش از یک دلیل برای تغییر دارد.

### روش اصلاح

مسئولیت‌ها به componentهای مستقل منتقل شدند:

- `DefaultOrderValidator`
- `RuleBasedDiscountCalculator`
- `StandardShippingService`
- `PaymentProcessor`
- `OrderRepository`
- `Notifier`
- `ConsoleReceiptPrinter`

`OrderService` فقط ترتیب اجرای Checkout را هماهنگ می‌کند.

### دلیل انتخاب

این طراحی coupling را کاهش می‌دهد، تست هر مسئولیت را ساده‌تر می‌کند و تغییر یک بخش، برای مثال روش چاپ Receipt، نیازمند تغییر منطق اصلی Checkout نیست.

---

## 10. OCP — Open/Closed Principle

### 10.1 Payment

#### علت نقض

در نسخه اولیه `PaymentProcessor` دارای ساختار زیر است:

```text
if credit_card
elif paypal
elif bitcoin
elif cash
```

برای هر روش جدید، خود کلاس باید تغییر کند.

#### روش اصلاح

یک abstraction به نام `PaymentMethod` تعریف شد و هر روش پرداخت به Strategy مستقلی تبدیل شد:

```text
PaymentMethod
├── CreditCardPayment
├── PayPalPayment
├── BitcoinPayment
└── CashPayment
```

`PaymentProcessor` فقط Strategyهای تزریق‌شده را در یک mapping نگه می‌دارد و بر اساس `key` اجرا می‌کند.

#### دلیل انتخاب

روش جدید بدون اضافه‌کردن branch جدید به dispatch logic قابل توسعه است. برای Cash، `PaymentProcessor.process()` تغییر نکرد.

### 10.2 Discount

#### علت نقض

در نسخه اولیه `DiscountCalculator` شامل زنجیره `if/elif` برای VIP، Bulk و Coupon بود.

#### روش اصلاح

قوانین به کلاس‌های مستقل تبدیل شدند:

- `VipDiscountRule`
- `BulkDiscountRule`
- `WelcomeCouponDiscountRule`

و `RuleBasedDiscountCalculator` آن‌ها را به ترتیب بررسی می‌کند.

#### دلیل انتخاب

قانون جدید را می‌توان با افزودن Rule جدید و ثبت آن در لیست وارد کرد، بدون اینکه الگوریتم انتخاب Rule بازنویسی شود.

### حفظ Business Rule قبلی

برای جلوگیری از تغییر ناخواسته رفتار، تقدم قوانین نسخه اولیه حفظ شد:

1. VIP → 20%
2. Bulk با `item_count >= 10` → 10%
3. `WELCOME10` → 10%

فقط اولین Rule منطبق اعمال می‌شود.

---

## 11. LSP — Liskov Substitution Principle

### علت نقض

در نسخه اولیه:

```python
class BundleOrder(Order):
    def __init__(self, id, customer, orders):
        super().__init__(id=id, customer=customer, items=[])
        self.orders = orders
```

`BundleOrder` از `Order` ارث می‌برد، اما `items` آن خالی است. در حالی که propertyهای مهم `Order` یعنی `subtotal` و `item_count` بر اساس `items` کار می‌کنند.

در `OrderService` نیز برای جلوگیری از رد شدن Bundle یک special case وجود داشت:

```python
if not order.items and not isinstance(order, BundleOrder):
    raise ValueError("Order has no items")
```

وجود چنین شرطی نشان می‌دهد `BundleOrder` در تمام محل‌هایی که `Order` انتظار می‌رود بدون شناخت subtype قابل استفاده نیست.

### روش اصلاح

آیتم‌های سفارش‌های داخلی Bundle Flatten شدند و در قرارداد اصلی `Order.items` قرار گرفتند:

```python
flattened_items = [
    item
    for child_order in orders
    for item in child_order.items
]
```

سپس `Order` با همان آیتم‌ها initialize می‌شود.

### تصمیم مهم در فرایند OpenCode

هنگام Plan/Build، Agent اعلام کرد که حفظ خروجی قدیمی Order 103 با اصلاح واقعی LSP تعارض دارد. دو گزینه وجود داشت:

- حفظ مبلغ قدیمی 5 دلار و باقی‌گذاشتن special case؛
- اولویت دادن به قابلیت جانشینی و قیمت‌گذاری Bundle بر اساس محتویات واقعی.

گزینه دوم، یعنی **Substitution wins**، انتخاب شد.

### نتیجه

Order 103 بعد از اصلاح:

```text
Subtotal  = $1194.99
VIP       = -$239.00
Shipping  = $0.00
Total     = $955.99
```

این تغییر یک Regression ناخواسته نیست؛ خروجی 5 دلار نسخه قبل نتیجه design defect بود.

---

## 12. ISP — Interface Segregation Principle

### علت نقض

نسخه اولیه دارای `NotificationService` با سه قابلیت بود:

```text
send_email
send_sms
send_push
```

اما `SmsOnlyNotifier` قادر به Email یا Push نبود و برای این متدها `NotImplementedError` ایجاد می‌کرد.

### روش اصلاح

یک abstraction کوچک تعریف شد:

```python
class Notifier(ABC):
    @abstractmethod
    def send(self, customer, message: str) -> None:
        ...
```

سپس implementationهای مستقل ایجاد شدند:

- `EmailNotifier`
- `SmsNotifier`
- `PushNotifier`

### دلیل انتخاب

هر client فقط قراردادی را پیاده می‌کند که واقعاً به آن نیاز دارد و هیچ implementation مجبور به پشتیبانی از عملیات نامرتبط نیست.

---

## 13. DIP — Dependency Inversion Principle

### علت نقض

در نسخه اولیه `OrderService` dependencyهای concrete خود را می‌سازد:

```python
self.discount_calculator = DiscountCalculator()
self.payment_processor = PaymentProcessor()
self.notification = NotificationService()
self.database = MySqlDatabase()
```

در نتیجه high-level policy مستقیماً به implementationهای مشخص وابسته است.

### روش اصلاح

dependencyها از constructor دریافت می‌شوند:

```python
OrderService(
    validator=...,
    pricing=...,
    shipping=...,
    payment=...,
    repository=...,
    notifiers=...,
    receipt_printer=...,
)
```

ساخت concrete implementationها فقط در `main.py` انجام می‌شود که نقش **Composition Root** را دارد.

### دلیل انتخاب

- تست با Fake/Stub ساده می‌شود؛
- implementationها قابل جایگزینی می‌شوند؛
- `OrderService` به سیاست سطح بالا محدود می‌ماند.

---

# بخش سوم — طراحی Skill برای OpenCode

## 14. Skill `solid-review`

مسیر Skill:

```text
02-Principles-OOD-Applied/.opencode/skills/solid-review/SKILL.md
```

### هدف Skill

وادارکردن Agent به انجام تحلیل ساختاریافته و مبتنی بر شواهد برای پنج اصل SOLID، قبل از اعمال هر تغییری.

### اطلاعاتی که Skill در اختیار Agent قرار می‌دهد

Skill مشخص می‌کند که Agent باید:

1. فایل‌های مرتبط را ابتدا بخواند؛
2. SRP، OCP، LSP، ISP و DIP را جداگانه بررسی کند؛
3. برای هر نقض فایل، کلاس و evidence مشخص ارائه کند؛
4. علت نقض را توضیح دهد؛
5. Refactoring مناسب و دلیل انتخاب آن را پیشنهاد کند؛
6. ریسک احتمالی را گزارش کند؛
7. قبل از edit یک Plan بسازد؛
8. بعد از تأیید، تغییرات را incremental اعمال کند؛
9. بعد از مراحل اصلی verification انجام دهد.

### دلیل انتخاب این ساختار

هدف این بود که Agent به‌جای ارائه مستقیم یک بازنویسی بزرگ، ابتدا تحلیل خود را قابل بررسی کند و کنترل تصمیم‌های معماری در اختیار دانشجو باقی بماند.

---

# بخش چهارم — Plan و تصمیم‌های Refactoring

## 15. استفاده از Plan Mode

قبل از تغییر کد، از OpenCode خواسته شد نقض‌های SOLID را تحلیل و یک برنامه مرحله‌ای ایجاد کند. Plan نهایی در فایل زیر نگهداری شده است:

```text
02-Principles-OOD-Applied/REFACTORING_PLAN.md
```

### ترتیب اصلی Plan

1. ثبت رفتار baseline؛
2. اصلاح Substitutability در `BundleOrder`؛
3. استخراج Validation؛
4. استخراج Shipping؛
5. استخراج Receipt؛
6. تعریف abstractionهای Payment و Strategyها؛
7. تبدیل Discount به Ruleها؛
8. تفکیک Notifierها؛
9. تعریف Repository abstraction؛
10. Dependency Injection در `OrderService`؛
11. ساخت Composition Root؛
12. افزودن regression testها؛
13. Verification؛
14. checkpoint نسخه SOLID پیش از Cash؛
15. افزودن Cash در مرحله مستقل.

---

## 16. اصلاحات انسانی روی خروجی OpenCode


### 16.1 تعارض Bundle

Agent درباره حفظ مبلغ 5 دلار یا اصلاح LSP سؤال کرد. تصمیم انسانی: **Substitution wins**.

### 16.2 خرابی یک نسخه میانی `main.py`

در یک مرحله Build، فایل `main.py` شامل خطوط تکراری و ناقص شد. فایل بررسی و ساخت Composition Root به‌صورت دستی اصلاح شد.

### 16.3 زمان اضافه‌شدن Cash

در یک مرحله Cash زودتر از checkpoint مورد نیاز وارد Demo شده بود و Golden Test را نیز تغییر می‌داد. این تغییر موقتاً عقب برده شد تا ابتدا نسخه SOLID-only تثبیت شود و سپس Cash در مرحله توسعه مستقل اضافه شود.

### 16.4 Golden Test نهایی

پس از اضافه‌شدن عمدی Cash به نسخه نهایی، expected output تست Golden نیز برای وضعیت نهایی به‌روزرسانی شد.

این موارد نمونه‌ای از بررسی، رد یا اصلاح خروجی Agent توسط دانشجو هستند.

---

# بخش پنجم — معماری Refactorشده

## 17. تفکیک مسئولیت‌ها

### `contracts.py`

قراردادهای اصلی را نگه می‌دارد:

- `PaymentMethod`
- `PaymentService`
- `OrderValidator`
- `ShippingService`
- `Notifier`
- `OrderRepository`
- `ReceiptPrinter`

### `validation.py`

`DefaultOrderValidator` فقط مسئول validation است.

### `shipping.py`

`StandardShippingService` مسئول قانون Shipping است:

```text
subtotal < 100  -> $5
subtotal >= 100 -> $0
```

### `receipt.py`

`ConsoleReceiptPrinter` فقط فرمت و چاپ Receipt را انجام می‌دهد.

### `notification.py`

هر کانال اعلان implementation مستقل دارد.

### `storage.py`

`MySqlDatabase` قرارداد `OrderRepository` را پیاده‌سازی می‌کند.

### `order_service.py`

فقط orchestration مراحل Checkout را انجام می‌دهد:

```text
validate
  ↓
pricing
  ↓
shipping
  ↓
payment
  ↓
persist
  ↓
notify
  ↓
receipt
```

---

# بخش ششم — افزودن مجدد Cash بعد از SOLID

## 18. `CashPayment` به‌عنوان Strategy

پس از Refactoring، Cash به‌صورت یک کلاس جدید از `PaymentMethod` پیاده‌سازی شد:

```python
class CashPayment(PaymentMethod):
    @property
    def key(self) -> str:
        return "cash"

    def pay(self, order, amount: float) -> str:
        print(f"[payment] Cash payment {amount:.2f}")
        return f"paid_by_cash:{amount:.2f}"
```

در Composition Root ثبت می‌شود:

```python
payment = PaymentProcessor(
    [
        CreditCardPayment(),
        PayPalPayment(),
        BitcoinPayment(),
        CashPayment(),
    ]
)
```

نکته اصلی این است که برای Cash هیچ `elif` جدیدی به `PaymentProcessor.process()` اضافه نشده است.

---

## 19. جدول تغییرات Cash پس از SOLID

| ردیف | فایل / کلاس | نوع تغییر | توضیح |
|---:|---|---|---|
| 1 | `store/payment.py` / `CashPayment` | افزودن Strategy جدید | behavior مربوط به Cash در implementation مستقل قرار گرفت؛ dispatch logic موجود تغییر نکرد. |
| 2 | `store/main.py` | Composition wiring + Demo | `CashPayment` در لیست Strategyها ثبت و سفارش Cash برای Demo اضافه شد. |
| 3 | `tests/test_payment.py` | تست جدید | صحت receipt و قابلیت plug-in شدن Cash در Processor بررسی شد. |
| 4 | `tests/test_golden_demo.py` | به‌روزرسانی خروجی نهایی | Demo نهایی شامل Cash است، بنابراین expected output نهایی نیز ثبت شد. |

در مقایسه معماری فقط **تغییرات production** معیار اصلی توسعه‌پذیری هستند؛ اضافه‌شدن تست یک هزینه مثبت برای verification است و نقض OCP محسوب نمی‌شود.

---

# بخش هفتم — مقایسه قبل و بعد از SOLID

## 20. مقایسه توسعه قابلیت Cash

| معیار | نسخه اولیه | نسخه SOLID |
|---|---|---|
| نحوه شناسایی روش پرداخت | زنجیره `if/elif` | Strategy registry |
| تغییر داخل `PaymentProcessor.process()` برای Cash | لازم | لازم نیست |
| Cash behavior مستقل | خیر | بله، `CashPayment` |
| Coupling میان روش‌های پرداخت | بیشتر | کمتر |
| امکان تست روش جدید به‌تنهایی | محدودتر | مستقیم و مستقل |
| ریسک تغییر dispatch قبلی | بیشتر | کمتر |
| Composition Root | وجود ندارد | وجود دارد |

### نتیجه مقایسه

SOLID لزوماً تعداد خطوط یا حتی تعداد فایل‌های لمس‌شده را کم نمی‌کند. اثر مهم آن **محدودشدن محل اثر تغییر** است.

در نسخه اولیه:

```text
Add Cash
   ↓
Modify existing PaymentProcessor logic
   ↓
Add another conditional branch
```

در نسخه SOLID:

```text
Add Cash
   ↓
Create/extend a PaymentMethod implementation
   ↓
Register it in composition wiring
```

به این ترتیب منطق dispatch موجود نسبت به قابلیت جدید بسته‌تر و ساختار برای extension بازتر شده است.

---

# بخش هشتم — تست و Verification

## 21. مجموعه تست‌ها

نسخه SOLID دارای **40 تست** است و در بررسی نهایی همه تست‌ها Pass شدند.

| حوزه | تعداد تست |
|---|---:|
| Golden Demo | 1 |
| Models / BundleOrder | 4 |
| Notification | 4 |
| OrderService | 6 |
| Payment | 7 |
| Pricing | 10 |
| Storage | 3 |
| Validation | 5 |
| **جمع** | **40** |

دستور:

```powershell
cd .\02-Principles-OOD-Applied
py -B -m unittest discover -s tests -v
```

نتیجه نهایی:

```text
Ran 40 tests

OK
```

جزئیات بیشتر در:

```text
docs/TEST_REPORT.md
```

---

## 22. رفتارهای مهم پوشش‌داده‌شده توسط تست‌ها

- `BundleOrder` آیتم‌های child orderها را Flatten می‌کند؛
- Bundle مانند یک Order عادی توسط Validation و Pricing استفاده می‌شود؛
- Nested Bundle نیز قابل Flatten شدن است؛
- Email/SMS/Push مستقل‌اند؛
- `notify=False` ارسال اعلان را متوقف می‌کند ولی Receipt همچنان چاپ می‌شود؛
- پرداخت نامعتبر قبل از persistence متوقف می‌شود؛
- Shipping در مرز 100 دلار تست شده است؛
- Payment strategy جدید بدون تغییر Processor قابل ثبت است؛
- Cash receipt و خروجی آن تست شده است؛
- تقدم Discount Ruleها و rounding تست شده است؛
- Repository save/load تست شده است؛
- Golden Test خروجی کامل Demo نهایی را کنترل می‌کند.

---

# بخش نهم — ارزیابی عملکرد OpenCode

## 23. OpenCode چه بخش‌هایی را به‌درستی تحلیل کرد؟

موارد مفید اصلی عبارت بودند از:

- تشخیص مسئولیت‌های متعدد `OrderService`؛
- تشخیص مشکل extension در `PaymentProcessor`؛
- پیشنهاد Strategy برای Payment؛
- تشخیص نیاز به جداسازی Discount Ruleها؛
- شناسایی مشکل `BundleOrder` و مطرح‌کردن تعارض حفظ baseline با substitutability؛
- پیشنهاد interface کوچک برای Notification؛
- انتقال concrete dependency construction به Composition Root؛
- پیشنهاد regression test برای محافظت از رفتارها.

---

## 24. در کدام قسمت‌ها نیاز به اصلاح خروجی Agent بود؟

### خرابی `main.py`

یک خروجی میانی Build باعث ایجاد خطوط تکراری و ناقص در `main.py` شد. فایل به‌صورت دستی بررسی و اصلاح شد.

### ترتیب Cash و checkpoint

Cash در یک مرحله زودتر از زمان مورد نیاز وارد Demo شد. برای اینکه مقایسه آزمایش معتبر بماند، ابتدا checkpoint نسخه SOLID بدون Cash نگهداری شد و Cash بعداً به‌صورت مستقل اعمال شد.

### تصمیم LSP

OpenCode تصمیم نهایی را به کاربر واگذار کرد. حفظ output معیوب Bundle رد شد و قرارداد صحیح subtype انتخاب شد.

### تست Golden

شکست Golden Test صرفاً به دلیل تفاوت میان expected output و Demo دارای Cash بود. به‌جای تغییر کورکورانه تست، ابتدا مرحله پروژه بررسی شد و سپس در نسخه نهایی expected output به‌طور آگاهانه به‌روزرسانی شد.

---

## 25. مهم‌ترین Promptها

تمام Promptهای اصلی و توضیح نتیجه آن‌ها در فایل زیر ثبت شده‌اند:

```text
docs/PROMPTS.md
```

Promptهای اصلی شامل این موضوعات بودند:

1. افزودن Cash به نسخه اولیه بدون Refactoring؛
2. تحلیل SOLID با Skill در Plan Mode؛
3. تصمیم `Substitution wins`؛
4. اجرای Plan در Build Mode؛
5. افزودن Cash پس از SOLID بدون تغییر Processor؛
6. عیب‌یابی و Verification تست‌ها.

---

## 26. تأثیر Skill بر کیفیت پاسخ OpenCode

قبل از اعمال تغییر، Agent ملزم شد برای هر اصل شواهد دقیق و Plan ارائه دهد. این موضوع باعث شد:

- پیشنهادها قبل از edit قابل بررسی باشند؛
- موارد نقض به فایل و کلاس مشخص متصل شوند؛
- دلیل Refactoring در گزارش قابل استناد باشد؛
- از بازنویسی ناگهانی و بدون توضیح جلوگیری شود؛
- نقش دانشجو در تأیید/رد تصمیم‌های Agent حفظ شود.

---

# بخش دهم — مستندسازی استفاده از هوش مصنوعی

## 28. ابزارهای استفاده‌شده

| ابزار | مدل / Provider | نحوه استفاده |
|---|---|---|
| ChatGPT | GPT-5.6 Sol / OpenAI | تفسیر دستورالعمل، برنامه‌ریزی مراحل Windows، debugging، بررسی Agent و تهیه گزارش |

شرح کامل‌تر در:

```text
docs/AI_USAGE.md
```

در فرایند انجام این پروژه از ابزار هوش مصنوعی به عنوان دستیار آموزشی استفاده شده است.

**به دلیل اینکه نسخه ChatGPT Buisness امکان export چت به افراد خارج workspace را نمی‌دهد، محتوای چت داخل این فایل مارک داون قرار گرفته است.**


---

# بخش دوازدهم — نتیجه‌گیری

## 30. جمع‌بندی

در نسخه اولیه، افزودن Cash مستلزم تغییر مستقیم `PaymentProcessor` بود. بررسی معماری همچنین نشان داد:

- `OrderService` مسئولیت‌های زیادی دارد؛
- Payment و Discount نسبت به extension بسته نیستند؛
- `BundleOrder` قرارداد قابل جانشینی `Order` را رعایت نمی‌کند؛
- Notification interface بیش از نیاز بعضی implementationهاست؛
- high-level service به concrete dependencyها وابسته است.

پس از Refactoring:

- مسئولیت‌ها از `OrderService` خارج شدند؛
- Payment بر اساس Strategy قابل توسعه شد؛
- Discount بر اساس Ruleها توسعه‌پذیر شد؛
- `BundleOrder` بدون special case با قرارداد `Order` کار می‌کند؛
- notifierها interface کوچک و مستقل دارند؛
- dependencyها به `OrderService` تزریق می‌شوند؛
- 40 regression test رفتار نهایی را پوشش می‌دهند.

مهم‌ترین نتیجه این آزمایش این است که SOLID الزاماً به معنی «کد کمتر» نیست. مزیت اصلی آن **کاهش coupling، محدودشدن اثر تغییر، افزایش testability و آسان‌ترشدن توسعه قابلیت‌های بعدی** است.

---

## 31. فایل‌های تکمیلی گزارش

- `01-Principles-OOD-Without/README.md` — توضیح نسخه اولیه؛
- `02-Principles-OOD-Applied/README.md` — توضیح نسخه SOLID؛
- `02-Principles-OOD-Applied/REFACTORING_PLAN.md` — Plan و تصمیم‌های Refactoring؛
- `docs/PROMPTS.md` — Promptهای AI؛
- `docs/AI_USAGE.md` — مستندسازی استفاده از AI؛
- `docs/TEST_REPORT.md` — گزارش 40 تست؛
- `docs/FINAL_CHECKLIST.md` — چک‌لیست پیش از تحویل.

---
