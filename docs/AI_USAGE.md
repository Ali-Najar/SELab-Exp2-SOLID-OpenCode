# رونوشت کامل گفت‌وگوی پروژه آزمایش دوم مهندسی نرم‌افزار

> این فایل شامل پیام‌های قابل‌مشاهده‌ی کاربر و دستیار در همین گفت‌وگو است. پیام‌های سیستمی، دستورهای داخلی، خروجی خام ابزارها و زنجیره‌ی استدلال خصوصی در آن قرار نگرفته‌اند. فایل‌ها و تصاویر پیوست‌شده نیز به‌صورت باینری داخل Markdown جاسازی نشده‌اند و در جای خود با توضیح مشخص شده‌اند.

---

## کاربر

در انجام گام به گام این پروژه توضیحات لازمی که باید داده شود و کارهایی که نیاز است تا انجام دهم را بگو.
در حال انجام پروژه بصورت تک نفره هستم ولی خب میشه عمده چیز هایش را تک نفره هم انجام داد  
@SELab-Plc-Summer-2025.pdf 
دستور العمل ازمایشگاه هم گذاشتم. 
طبق این readme کامل را به من بده برای گزارش کار. سپس توضیح بده که چه نکاتی مهم است که به آنها اشاره کنم و چیز های خواسته شده مسئله چیست.  
(بجای همگیت هم از گیتهاب استفاده میکنم)
همه ی موارد نیاز از جمله کد های هر بخش را هم به من بده به همراه توضیحات مربوط. از صفر تا صد بگو چیکار باید بکنم.

---

## دستیار

هر دو فایل را بررسی کردم و لینک مخزن پایه‌ای که داخل PDF آزمایش ۲ قرار داده شده بود را هم استخراج و کد فعلی آن را بررسی کردم. خود صورت آزمایش صریحاً می‌خواهد ابتدا قابلیت **پرداخت نقدی** را روی طراحی فعلی اضافه کنی، بعد SOLID را تحلیل و Refactor کنی، سپس همان قابلیت را دوباره روی نسخه اصلاح‌شده اضافه کنی و میزان تغییرات دو حالت را مقایسه کنی.

همچنین یک بسته آماده برایت ساختم که شامل **README کامل فارسی، نمونه `AGENTS.md`، Skill مخصوص SOLID، Promptهای OpenCode، Plan پیشنهادی Refactoring، Patch نسخه بدون SOLID، کد کامل نسخه SOLID و تست‌ها** است. نسخه Refactorشده را هم اجرا و تست کردم و هر سه تست آن پاس شده‌اند.

[دانلود بسته کامل پروژه و راهنما](sandbox:/mnt/data/selab-exp2-complete-guide.zip)  
[دانلود مستقیم README پیشنهادی](sandbox:/mnt/data/selab-exp2-complete-guide/README-template.md)

---

# اول: دقیقاً چه چیزهایی از تو خواسته شده؟

صورت آزمایش دو هدف اصلی دارد: یادگیری عملی SOLID، تشخیص و Refactor کردن نقض‌ها، و یادگیری استفاده صحیح از OpenCode به‌عنوان Coding Agent؛ نه این‌که کل مسئله را به AI بسپاری.

خروجی نهایی باید حداقل این ساختار را داشته باشد:

```text
your-repository/
│
├── README.md
├── AGENTS.md
│
├── .opencode/
│   └── skills/
│       └── solid-review/
│           └── SKILL.md
│
├── 01-Without-OOD-Principles/
│   └── store/
│
└── 02-Applied-OOD-Principles/
    ├── store/
    ├── tests/
    └── REFACTORING_PLAN.md
```

طبق خود PDF، در پایان هر دو پوشه باید موجود باشند و README باید مطالب تمام گام‌ها را به ترتیب شامل شود.

یک نکته مهم دیگر: گزارش اصلی **باید فارسی و در `README.md` باشد؛ نه PDF** و کدها هم باید در همان repository تحویل داده شوند.

تاریخ تحویل درج‌شده در فایل آزمایش هم **۳۰ مرداد ۱۴۰۵ ساعت ۲۳:۵۹** است.

---

# نکته مهم درباره تک‌نفره انجام دادن پروژه

دستورالعمل عمومی آزمایشگاه اساساً برای کار گروهی نوشته شده و روی سرگروه، مشارکت همه اعضا و Kanban تأکید دارد.

پس اگر با اجازه دستیار تک‌نفره انجام می‌دهی، بهترین کار این است که در README صریحاً بنویسی:

> «این آزمایش به‌صورت تک‌نفره و با هماهنگی دستیار مربوطه انجام شده است.»

و در GitHub Project تمام Issueها را به خودت Assign کن. **تقسیم کار ساختگی درست نکن.**

اگر اجازه تک‌نفره را صریح نگرفته‌ای، این بخش ارزش یک سؤال از TA را دارد؛ چون مقررات عمومی روی مشارکت گروهی تأکید دارند.

---

# استفاده از GitHub به‌جای Hamgit

این کار از نظر workflow کاملاً قابل پیاده‌سازی است: یک GitHub repository و یک GitHub Project با Board layout بساز.

پیشنهاد من برای ستون‌ها:

```text
Todo
In Progress
Done
```

و Issueهای زیر را بساز:

1. Setup repository and OpenCode
2. Create AGENTS.md
3. Create SOLID Review Skill
4. Run and inspect original project
5. Add cash payment to non-SOLID version
6. Record first change table
7. Analyze SRP
8. Analyze OCP
9. Analyze LSP
10. Analyze ISP
11. Analyze DIP
12. Generate OpenCode Plan
13. Review and correct Plan
14. Apply SRP refactor
15. Apply OCP refactor
16. Fix BundleOrder / LSP
17. Fix notification / ISP
18. Apply dependency injection / DIP
19. Run regression tests
20. Add cash to refactored version
21. Compare both versions
22. Complete README
23. Document AI prompts
24. Record final video

---

# مسیر انجام پروژه از صفر تا صد

## گام ۱ — گرفتن پروژه پایه

```bash
git clone https://github.com/soleyman79/Software-Engineering-Lab-Experiment2.git selab-exp2
cd selab-exp2
```

اگر repository شخصی خودت را قبلاً در GitHub ساخته‌ای:

```bash
git remote rename origin upstream
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

حالا **قبل از هیچ تغییری** از نسخه پایه دو کپی بساز:

```bash
cp -R store 01-Without-OOD-Principles
cp -R store 02-Applied-OOD-Principles
rm -rf store

git add .
git commit -m "chore: prepare experiment 2 baselines"
```

این قسمت خیلی مهم است.

نباید اول `01` را cash کنی و بعد همان را در `02` کپی کنی. چون صورت سؤال می‌خواهد cash یک بار **قبل از SOLID** و یک بار **پس از SOLID** اضافه شود.

مسیر صحیح:

```text
              ┌─> Version 01 -> Add Cash
Original -----|
              └─> Version 02 -> Refactor -> Add Cash
```

## گام ۲ — نصب و راه‌اندازی OpenCode

```bash
curl -fsSL https://opencode.ai/install | bash
```

یا:

```bash
npm install -g opencode-ai
```

سپس:

```bash
cd selab-exp2
opencode
```

داخل OpenCode:

```text
/init
```

## گام ۳ — `AGENTS.md`

نمونه:

```markdown
- 01-Without-OOD-Principles نباید Refactor شود.
- در 02 ابتدا Refactoring انجام شود.
- سپس Refactoring commit شود.
- cash بعداً در commit مستقل وارد 02 شود.
- قبل از تغییرات بزرگ Plan ارائه شود.
- رفتار سیستم بدون دلیل تغییر نکند.
- پس از هر تغییر تست اجرا شود.
```

## گام ۴ — اجرای نسخه اولیه قبل از تغییر

```bash
cd 01-Without-OOD-Principles
python -m store.main
```

یک نکته بسیار مهم در پروژه پایه وجود دارد که برای LSP عالی است:

`BundleOrder` از `Order` ارث می‌برد، ولی `items=[]` قرار می‌دهد و سفارش‌ها را در `orders` نگهداری می‌کند.

در عین حال `Order.subtotal` بر اساس `items` حساب می‌شود. در نتیجه Bundle عملاً subtotal صفر پیدا می‌کند.

حتی در `OrderService` هم برای Bundle یک special case نوشته شده:

```python
if not order.items and not isinstance(order, BundleOrder):
    raise ValueError("Order has no items")
```

## گام ۵ — افزودن cash بدون SOLID

Prompt پیشنهادی:

```text
Add a cash payment method to this version with the minimum possible
change. Do NOT refactor the architecture and do NOT apply SOLID
improvements in this folder.

Cash does not require card, PayPal, or Bitcoin credentials.
Return a receipt string consistent with the existing payment methods.

First explain the exact changes you intend to make. Then apply them
after my approval.
```

### تغییر در `payment.py`

```python
elif method == "cash":
    print(f"[payment] Cash payment {amount:.2f}")
    return f"paid_by_cash:{amount:.2f}"
```

### تغییر در `main.py`

```python
cash_order = Order(
    id=104,
    customer=regular,
    payment_method="cash",
    items=[OrderItem(5, "Notebook", 15.00, 2)],
)
```

و:

```python
service.process_order(cash_order)
```

بعد:

```bash
python -m store.main
git add .
git commit -m "feat: add cash payment to non-solid version"
```

## گام ۶ — جدول تغییرات مرحله اول

| فایل | نوع تغییر | علت |
|---|---|---|
| `payment.py` | افزودن `elif cash` | معماری فعلی برای شناخت روش جدید مجبور به تغییر processor است |
| `main.py` | ایجاد cash order و اجرا | برای نمایش و تست قابلیت جدید |

برای اعداد واقعی:

```bash
git log --oneline
git diff --stat BEFORE..AFTER -- 01-Without-OOD-Principles
git diff --numstat BEFORE..AFTER -- 01-Without-OOD-Principles
```

## گام ۷ — تحلیل واقعی SOLID

| اصل | رعایت شده؟ | محل | دلیل |
|---|---|---|---|
| SRP | ❌ | `OrderService` | validation، pricing، shipping، payment، persistence، notification و receipt |
| OCP | ❌ | `PaymentProcessor` | روش جدید = `elif` جدید |
| OCP | ❌ | `DiscountCalculator` | قانون تخفیف جدید = شرط جدید |
| LSP | ❌ | `BundleOrder` | subtype قرارداد `Order.items/subtotal` را رعایت نمی‌کند |
| ISP | ❌ | `NotificationService` | `SmsOnlyNotifier` مجبور به داشتن عملیات email/push است |
| DIP | ❌ | `OrderService` | concrete dependencyها را خودش instantiate می‌کند |

## گام ۸ — طراحی Skill

```markdown
---
name: solid-review
description: Analyze Python object-oriented code for SOLID violations...
---

1. Read all Python files.
2. Run existing behavior.
3. Analyze SRP/OCP/LSP/ISP/DIP.
4. Give exact file/class evidence.
5. Explain violation, fix, rationale and risk.
6. Produce a plan before editing.
7. Wait for explicit approval.
8. Apply small changes.
9. Verify after every step.
```

## گام ۹ — Plan Mode

```text
Use the solid-review skill.

Analyze this no-cash version for SRP, OCP, LSP, ISP and DIP.
For every violation provide concrete evidence from exact files/classes.

Then produce an ordered refactoring plan.

Constraints:
- Do NOT add cash payment yet.
- Preserve intended behavior.
- Keep OrderService as an orchestration service.
- PaymentProcessor must become extensible without adding conditionals.
- BundleOrder must become safely substitutable for Order.
- Notifications should not force unsupported operations.
- High-level checkout code should receive dependencies instead of
  constructing concrete dependencies.
- Use standard Python only.

Do not edit files. Stop after the plan.
```

## گام ۱۰ — معماری SOLID پیشنهادی

```text
contracts.py
    abstractions

validation.py
    DefaultOrderValidator

shipping.py
    StandardShippingService

pricing.py
    VipDiscountRule
    BulkDiscountRule
    WelcomeCouponDiscountRule
    RuleBasedDiscountCalculator

payment.py
    CreditCardPayment
    PayPalPayment
    BitcoinPayment
    PaymentProcessor

cash_payment.py
    CashPayment

notification.py
    EmailNotifier
    SmsNotifier
    PushNotifier

storage.py
    MySqlOrderRepository

receipt.py
    ConsoleReceiptPrinter

order_service.py
    checkout orchestration only
```

## گام ۱۱ — مهم‌ترین کدهای نسخه SOLID

### قرارداد پرداخت

```python
class PaymentMethod(ABC):
    @property
    @abstractmethod
    def key(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def pay(self, order: Order, amount: float) -> str:
        raise NotImplementedError
```

### Processor جدید

```python
class PaymentProcessor(PaymentService):
    def __init__(self, methods: Iterable[PaymentMethod]):
        self._methods = {method.key: method for method in methods}

    def process(self, order: Order, amount: float) -> str:
        method = self._methods.get(order.payment_method)

        if method is None:
            raise ValueError(
                f"Unknown payment method: {order.payment_method!r}"
            )

        return method.pay(order, amount)
```

### cash بعد از SOLID

```python
class CashPayment(PaymentMethod):
    @property
    def key(self) -> str:
        return "cash"

    def pay(self, order: Order, amount: float) -> str:
        print(f"[payment] Cash payment {amount:.2f}")
        return f"paid_by_cash:{amount:.2f}"
```

## گام ۱۲ — اصلاح LSP

```python
class BundleOrder(Order):
    def __init__(self, id, customer, orders):
        flattened_items = [
            item
            for child_order in orders
            for item in child_order.items
        ]

        super().__init__(
            id=id,
            customer=customer,
            items=flattened_items,
        )

        self.orders = orders
```

## گام ۱۳ — اصلاح ISP

```python
class Notifier(ABC):
    @abstractmethod
    def send(self, customer: Customer, message: str) -> None:
        raise NotImplementedError
```

## گام ۱۴ — اصلاح DIP و SRP

```python
def __init__(
    self,
    validator: OrderValidator,
    pricing: PricingService,
    shipping: ShippingService,
    payment: PaymentService,
    repository: OrderRepository,
    notifiers: Iterable[Notifier],
    receipt_printer: ReceiptPrinter,
):
```

## گام ۱۵ — Commit بسیار مهم قبل از cash دوم

```bash
python -m store.main
python -m unittest discover -s tests -v

git add .
git commit -m "refactor: apply SOLID principles to second version"
```

## گام ۱۶ — حالا cash را دوباره اضافه کن

```text
Now add the same cash-payment capability to the refactored version.

Extend the payment abstraction rather than adding a new conditional
branch to PaymentProcessor.

Keep PaymentProcessor unchanged if possible.

Add:
- a cash payment strategy,
- composition-root wiring,
- a test,
- a demo.

Before editing, tell me which existing files need to change and which
new file will be added.
```

## گام ۱۷ — مقایسه واقعی قبل/بعد

```bash
git diff --numstat BASE..NON_SOLID_CASH -- 01-Without-OOD-Principles
```

و:

```bash
git diff --numstat SOLID_COMMIT..SOLID_CASH -- 02-Applied-OOD-Principles
```

تفاوت مهم:

```text
قبل:
cash => تغییر خود PaymentProcessor

بعد:
cash => extension جدید
        PaymentProcessor بدون تغییر
```

## گام ۱۸ — تست‌ها

```bash
cd 02-Applied-OOD-Principles

python -m store.main
python -m unittest discover -s tests -v
```

## گام ۱۹ — مستندسازی AI

باید موارد زیر مستند شوند:

- نام مدل
- ابزار
- روش تأمین مدل
- تمام Promptها
- نحوه تعامل
- اصلاحات انسانی روی خروجی Agent

## گام ۲۰ — فیلم

حداکثر ۱۵ دقیقه.

```text
00:00 – 01:00   معرفی مسئله و ساختار repository
01:00 – 02:30   GitHub Project / commit history
02:30 – 04:00   اجرای نسخه اولیه + نمایش مشکل BundleOrder
04:00 – 05:30   cash قبل از SOLID + diff
05:30 – 08:30   تحلیل پنج اصل SOLID
08:30 – 10:00   Skill و Plan و اصلاحات انسانی
10:00 – 12:00   معماری Refactorشده
12:00 – 13:00   cash بعد از SOLID + مقایسه diff
13:00 – 14:00   اجرای تست‌ها
14:00 – 15:00   نحوه استفاده واقعی از AI + جمع‌بندی
```

---

## کاربر

ایدی گیتهابم Ali-Najar عه و خب اسم ریپو و چیزای خالی رو خودت بزار

---

## دستیار

باشه. از اینجا به بعد همه‌چیز را با GitHub ID خودت یعنی **`Ali-Najar`** و اسم‌های مشخص جلو می‌بریم؛ طوری که فقط مرحله‌ها را انجام بدهی و خروجی واقعی هر مرحله را داخل README ثبت کنی.

اسم Repository را این می‌گذاریم:

**`SELab-Exp2-SOLID-OpenCode`**

پس آدرس نهایی مخزن تو می‌شود:

`https://github.com/Ali-Najar/SELab-Exp2-SOLID-OpenCode`

اسم GitHub Project/Kanban هم:

**`SELab Experiment 2 Board`**

صورت آزمایش می‌خواهد ابتدا قابلیت جدید را روی نسخه اولیه اضافه کنی، بعد SOLID را تحلیل و Refactor کنی، سپس همان قابلیت را روی نسخه اصلاح‌شده اضافه و دو حالت را مقایسه کنی.

---

# نقشه کلی پروژه

کل کار تو به این ترتیب است:

```text
1. ساخت Repository در GitHub
2. گرفتن پروژه پایه
3. ساخت دو نسخه مستقل از پروژه
4. ساخت Kanban Board
5. راه‌اندازی OpenCode
6. ساخت AGENTS.md
7. اجرای نسخه اصلی و فهمیدن معماری
8. اضافه کردن Cash بدون SOLID
9. ثبت دقیق تغییرات نسخه اول
10. تحلیل پنج اصل SOLID
11. ساخت Skill مخصوص SOLID
12. گرفتن Refactoring Plan از OpenCode
13. بررسی و اصلاح دستی Plan
14. Refactor کردن نسخه دوم
15. تست نسخه Refactorشده
16. Commit کردن نسخه SOLID بدون Cash
17. اضافه کردن Cash مجدد روی نسخه SOLID
18. ثبت تغییرات نسخه دوم
19. مقایسه Before / After
20. تکمیل README فارسی
21. مستندسازی استفاده از AI
22. مرتب‌کردن GitHub Issues و Kanban
23. ضبط فیلم حداکثر 15 دقیقه
24. تحویل لینک Repository
```

گزارش نهایی باید در `README.md` و به زبان فارسی باشد؛ طبق دستورالعمل آزمایشگاه گزارش PDF نباید تحویل شود.

---

# گام 0 — چیزهایی که باید نصب داشته باشی

قبل از شروع:

```bash
git --version
python --version
```

همچنین باید GitHub account خودت را داشته باشی که داری:

```text
Ali-Najar
```

و OpenCode هم باید نصب و تنظیم شود، چون صورت آزمایش صراحتاً استفاده از OpenCode و آشنایی با Agent، Skill، Plan، Build و `AGENTS.md` را می‌خواهد.

---

# گام 1 — Repository را بساز

در GitHub وارد اکانت `Ali-Najar` شو.

Repository جدید:

```text
Repository name:
SELab-Exp2-SOLID-OpenCode
```

Description:

```text
Software Engineering Lab - Experiment 2 - SOLID Principles and OpenCode
```

پیشنهاد:

```text
Public Repository
```

فعلاً گزینه‌های زیر را نزن:

```text
Add README
Add .gitignore
Add license
```

Repository خالی بساز.

---

# گام 2 — پروژه پایه را Clone کن

```bash
git clone https://github.com/soleyman79/Software-Engineering-Lab-Experiment2.git
```

بعد:

```bash
cd Software-Engineering-Lab-Experiment2
```

Remote فعلی را تغییر نام بده:

```bash
git remote rename origin upstream
```

Repository خودت را اضافه کن:

```bash
git remote add origin https://github.com/Ali-Najar/SELab-Exp2-SOLID-OpenCode.git
```

بررسی:

```bash
git remote -v
```

باید چیزی شبیه این ببینی:

```text
origin    https://github.com/Ali-Najar/SELab-Exp2-SOLID-OpenCode.git
upstream  https://github.com/soleyman79/Software-Engineering-Lab-Experiment2.git
```

حالا:

```bash
git push -u origin main
```

اگر branch پروژه `master` بود:

```bash
git branch -M main
git push -u origin main
```

---

# گام 3 — اولین Commit تمیز

قبل از تغییر پروژه:

```bash
git status
```

بعد یک tag هم روی baseline بگذار:

```bash
git tag baseline
git push origin baseline
```

---

# گام 4 — ساخت دو نسخه مستقل

نام پوشه‌ها:

```text
01-Principles-OOD-Without
02-Principles-OOD-Applied
```

ساختار نهایی:

```text
SELab-Exp2-SOLID-OpenCode/
│
├── README.md
├── AGENTS.md
│
├── .opencode/
│   └── skills/
│       └── solid-review/
│           └── SKILL.md
│
├── 01-Principles-OOD-Without/
│   └── store/
│
└── 02-Principles-OOD-Applied/
    └── store/
```

اگر پروژه اصلی فقط یک `store` دارد:

```bash
mkdir 01-Principles-OOD-Without
mkdir 02-Principles-OOD-Applied

cp -R store 01-Principles-OOD-Without/
cp -R store 02-Principles-OOD-Applied/
```

بعد:

```bash
rm -rf store
```

و Commit:

```bash
git add .
git commit -m "chore: prepare experiment baseline versions"
git push
```

مسیر صحیح:

```text
              ┌─> Version 01 -> Add Cash
Original -----|
              └─> Version 02 -> Refactor -> Add Cash
```

---

# گام 5 — GitHub Project/Kanban

در GitHub برای Repository یک Project بساز:

```text
SELab Experiment 2 Board
```

نوع:

```text
Board
```

ستون‌ها:

```text
Todo
In Progress
Done
```

---

# گام 6 — Issueهای پروژه

این Issueها را بساز:

```text
Setup repository and experiment structure
Setup OpenCode and AGENTS.md
Analyze original project behavior
Add cash payment to non-SOLID version
Record changes required for cash payment
Analyze SRP violations
Analyze OCP violations
Analyze LSP violations
Analyze ISP violations
Analyze DIP violations
Create SOLID analysis OpenCode Skill
Generate and review refactoring plan
Apply SOLID refactoring
Add regression tests
Add cash payment to SOLID version
Compare before and after SOLID
Complete Persian README report
Document AI usage and prompts
Record experiment presentation video
```

همه را Assign کن به:

```text
Ali-Najar
```

---

# گام 7 — README اولیه

```bash
touch README.md
```

بالای آن:

```markdown
# آزمایش دوم آزمایشگاه مهندسی نرم‌افزار

## مروری بر اصول طراحی شی‌گرا و SOLID

**دانشجو:** Ali Najar  
**GitHub:** [Ali-Najar](https://github.com/Ali-Najar)  
**Repository:** SELab-Exp2-SOLID-OpenCode  
**نحوه انجام:** تک‌نفره
```

اگر تک‌نفره بودن با TA هماهنگ شده:

```markdown
این آزمایش به‌صورت تک‌نفره و با هماهنگی دستیار مربوطه انجام شده است.
```

---

# گام 8 — OpenCode

در ریشه پروژه:

```bash
opencode
```

سپس داخل OpenCode:

```text
/init
```

---

# گام 9 — `AGENTS.md`

```markdown
# Project Instructions

This repository contains two versions of the same software.

## 01-Principles-OOD-Without

This version represents the original non-SOLID design.

Rules:

- Do not refactor this version.
- Implement new functionality using the existing architecture.
- Minimize unrelated changes.
- Record every changed file.
- Run the application after modifications.

## 02-Principles-OOD-Applied

This version will be refactored using SOLID principles.

Rules:

- Do not add cash payment before the SOLID refactoring is complete.
- Analyze SRP, OCP, LSP, ISP and DIP.
- Produce a plan before major modifications.
- Preserve intended behavior.
- Prefer small abstractions over unnecessary complexity.
- Run tests after each major refactoring step.
- Commit the refactored version before adding cash payment.

## General Rules

- Explain changes before applying them.
- Do not silently change business behavior.
- Keep code simple.
- Use standard Python where possible.
- Treat AI output as suggestions, not final truth.
```

Commit:

```bash
git add AGENTS.md
git commit -m "docs: add OpenCode project instructions"
git push
```

---

# گام 10 — نسخه اولیه را اجرا کن

```bash
cd 01-Principles-OOD-Without
python -m store.main
```

فعلاً هیچ Refactor نکن.

---

# گام 11 — Cash را روی نسخه بدون SOLID اضافه کن

Prompt:

```text
Analyze the current payment implementation.

I need to add a new payment method named "cash".

Important constraints:
- Do not refactor the architecture.
- Do not apply SOLID improvements.
- Make the minimum required changes.
- Preserve the existing coding style.
- Explain the required modifications before editing.
```

Cash:

```python
elif method == "cash":
    print(f"[payment] Cash payment {amount:.2f}")
    return f"paid_by_cash:{amount:.2f}"
```

---

# گام 12 — یک سفارش Cash برای Demo

```python
cash_order = Order(
    id=104,
    customer=regular,
    payment_method="cash",
    items=[
        OrderItem(
            id=5,
            name="Notebook",
            unit_price=15.00,
            quantity=2,
        )
    ],
)
```

و:

```python
service.process_order(cash_order)
```

---

# گام 13 — نسخه Without را اجرا کن

```bash
python -m store.main
git status
git diff
```

---

# گام 14 — Commit Cash نسخه اول

```bash
git add 01-Principles-OOD-Without
git commit -m "feat: add cash payment to non-solid version"
git push
```

---

# گام 15 — آمار تغییرات را ثبت کن

```bash
git show --stat HEAD
git show --numstat HEAD
```

جدول README:

| فایل | نوع تغییر | دلیل |
|---|---|---|
| `payment.py` | افزودن branch جدید | PaymentProcessor برای شناخت Cash باید تغییر کند |
| `main.py` | افزودن Cash Order | نمایش و بررسی قابلیت جدید |

---

# گام 16 تا 21 — تحلیل SOLID

### SRP

تمرکز روی `OrderService`: validation، pricing، shipping، payment، database، notification، receipt.

### OCP

تمرکز روی `PaymentProcessor` و `DiscountCalculator`.

### LSP

تمرکز روی `BundleOrder` و special caseهایی مثل:

```python
isinstance(order, BundleOrder)
```

### ISP

تمرکز روی `NotificationService` با `send_email`, `send_sms`, `send_push` و implementationهایی که مجبور به `NotImplementedError` هستند.

### DIP

تمرکز روی concrete dependency creation در `OrderService`.

جدول:

| اصل | رعایت شده؟ | محل | مشکل |
|---|---|---|---|
| SRP | خیر | `OrderService` | چند مسئولیت |
| OCP | خیر | `PaymentProcessor` | روش جدید نیازمند branch جدید |
| OCP | خیر | `DiscountCalculator` | قانون جدید نیازمند تغییر کلاس |
| LSP | خیر | `BundleOrder` | subtype رفتار سازگار با Order ندارد |
| ISP | خیر | `NotificationService` | interface بیش از نیاز implementationهاست |
| DIP | خیر | `OrderService` | وابستگی مستقیم به concrete classها |

---

# گام 23 — Skill بساز

```bash
mkdir -p .opencode/skills/solid-review
```

فایل:

```text
.opencode/skills/solid-review/SKILL.md
```

محتوا:

```markdown
---
name: solid-review
description: Analyze object-oriented Python projects for SOLID violations and propose controlled refactoring.
---

# SOLID Review Skill

When asked to analyze a project:

1. Read the relevant Python source files.
2. Identify concrete evidence for SRP, OCP, LSP, ISP and DIP.
3. For every violation provide:
   - file and class
   - reason
   - consequence
   - proposed refactoring
   - rationale
4. Do not infer violations without code evidence.
5. Produce a refactoring plan before editing.
6. Do not modify files until the user approves the plan.
7. Apply refactoring incrementally.
8. Preserve existing intended behavior.
9. Run tests or executable examples after each major change.
10. Report any AI proposal that may introduce unnecessary complexity.
```

---

# گام 24 — Plan Mode

```text
Use the solid-review skill.

Analyze the project in 02-Principles-OOD-Applied.

Identify violations of:
- SRP
- OCP
- LSP
- ISP
- DIP

For every issue provide exact file and class evidence.

Then produce a step-by-step refactoring plan.

Constraints:
- Do not add cash payment yet.
- Preserve intended behavior.
- Avoid overengineering.
- Keep OrderService as orchestration only.
- Remove concrete dependency creation from high-level services.
- Make payment extensible without modifying PaymentProcessor.
- Make BundleOrder substitutable for Order.
- Split notification responsibilities appropriately.

Do not modify files yet.
```

---

# گام 25 — Plan Agent را کورکورانه قبول نکن

اگر Agent overengineering پیشنهاد داد، آن را کاهش بده و فقط تغییر واقعی را در گزارش ثبت کن.

---

# گام 26 — Plan نهایی

```markdown
# Refactoring Plan

1. Preserve baseline behavior.
2. Fix BundleOrder substitutability.
3. Extract order validation.
4. Extract shipping responsibility.
5. Extract receipt printing.
6. Introduce payment abstraction.
7. Convert each payment method to a strategy.
8. Convert discount conditions to rules.
9. Split notification implementations.
10. Introduce repository abstraction.
11. Inject dependencies into OrderService.
12. Add regression tests.
13. Verify existing behavior.
14. Commit SOLID version before adding cash.
```

---

# گام 27 — Refactor با Build

```text
Apply the approved refactoring plan incrementally.

After each major step:
1. summarize the change,
2. run relevant tests or the application,
3. stop if behavior changes unexpectedly.

Do not add cash payment.
```

---

# گام 28 — ساختار پیشنهادی نسخه SOLID

```text
02-Principles-OOD-Applied/
│
├── store/
│   ├── __init__.py
│   ├── models.py
│   ├── contracts.py
│   ├── validation.py
│   ├── pricing.py
│   ├── shipping.py
│   ├── payment.py
│   ├── notification.py
│   ├── storage.py
│   ├── receipt.py
│   ├── order_service.py
│   └── main.py
│
├── tests/
│   └── test_store.py
│
└── REFACTORING_PLAN.md
```

---

# گام 29 تا 34 — کدهای اصلی SOLID

### Contractهای اصلی

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @property
    @abstractmethod
    def key(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def pay(self, order, amount: float) -> str:
        raise NotImplementedError

class Notifier(ABC):
    @abstractmethod
    def send(self, customer, message: str) -> None:
        raise NotImplementedError

class OrderRepository(ABC):
    @abstractmethod
    def save(self, order) -> None:
        raise NotImplementedError
```

### Payment Strategy

```python
class PaymentProcessor:
    def __init__(self, methods):
        self._methods = {
            method.key: method
            for method in methods
        }

    def process(self, order, amount):
        method = self._methods.get(order.payment_method)

        if method is None:
            raise ValueError(
                f"Unknown payment method: {order.payment_method}"
            )

        return method.pay(order, amount)
```

### Notification

```python
class EmailNotifier(Notifier):
    def send(self, customer, message):
        print(f"[email] {customer.email}: {message}")

class SmsNotifier(Notifier):
    def send(self, customer, message):
        print(f"[sms] {customer.phone}: {message}")
```

### OrderService

```python
class OrderService:
    def __init__(
        self,
        validator,
        pricing,
        shipping,
        payment,
        repository,
        notifiers,
        receipt_printer,
    ):
        self.validator = validator
        self.pricing = pricing
        self.shipping = shipping
        self.payment = payment
        self.repository = repository
        self.notifiers = list(notifiers)
        self.receipt_printer = receipt_printer
```

### BundleOrder

```python
class BundleOrder(Order):
    def __init__(self, id, customer, orders):
        items = [
            item
            for order in orders
            for item in order.items
        ]

        super().__init__(
            id=id,
            customer=customer,
            items=items,
        )

        self.orders = orders
```

---

# گام 35 تا 37 — تست و Commit نسخه SOLID بدون Cash

```bash
python -m store.main
python -m unittest discover -s tests -v

git add .
git commit -m "refactor: apply SOLID principles to second version"
git push

git tag solid-before-cash
git push origin solid-before-cash
```

---

# گام 38 تا 41 — افزودن Cash به نسخه SOLID

Prompt:

```text
Now add a new cash payment method to the refactored project.

Constraints:
- Do not add an if/elif branch to PaymentProcessor.
- Extend the existing payment abstraction.
- Keep PaymentProcessor unchanged if possible.
- Add a regression test.
- Explain which existing files must change before editing.
```

Cash Strategy:

```python
from .contracts import PaymentMethod

class CashPayment(PaymentMethod):
    @property
    def key(self):
        return "cash"

    def pay(self, order, amount):
        print(f"[payment] Cash payment {amount:.2f}")
        return f"paid_by_cash:{amount:.2f}"
```

Register:

```python
payment_processor = PaymentProcessor(
    methods=[
        CreditCardPayment(),
        PayPalPayment(),
        BitcoinPayment(),
        CashPayment(),
    ]
)
```

Commit:

```bash
git add .
git commit -m "feat: add cash payment to SOLID version"
git push

git tag solid-with-cash
git push origin solid-with-cash
```

---

# گام 42 و 43 — مقایسه

```bash
git diff --stat solid-before-cash..solid-with-cash
git diff --numstat solid-before-cash..solid-with-cash
```

قبل:

```text
Add Cash
   ↓
Modify PaymentProcessor
   ↓
Add new branch
```

بعد:

```text
Add Cash
   ↓
Create CashPayment
   ↓
Register strategy
```

---

# گام 44 تا 47 — OpenCode، Promptها و README

باید در README پاسخ داده شود:

- OpenCode کجا درست عمل کرد؟
- کجا پاسخ Agent نیاز به اصلاح داشت؟
- مهم‌ترین Promptها چه بودند؟
- Skill چه اثری داشت؟
- دفعه بعد چه چیزی تغییر می‌کرد؟

فایل:

```text
docs/PROMPTS.md
```

و اطلاعات AI شامل ابزار، نسخه، مدل و Provider واقعی ثبت شود.

---

# گام 48 تا 50 — Git History، فیلم و تحویل

Git history پیشنهادی:

```text
chore: import base experiment project
chore: prepare experiment baseline versions
docs: add OpenCode project instructions
feat: add SOLID analysis OpenCode skill
feat: add cash payment to non-solid version
docs: record non-solid cash changes
docs: add SOLID violation analysis
docs: add reviewed refactoring plan
refactor: apply SOLID principles to second version
test: add regression tests for refactored design
feat: add cash payment to SOLID version
test: add cash payment test
docs: compare pre-SOLID and post-SOLID changes
docs: document OpenCode prompts and AI usage
docs: complete Persian experiment report
```

ساختار نهایی:

```text
Ali-Najar/
└── SELab-Exp2-SOLID-OpenCode
    │
    ├── README.md
    ├── AGENTS.md
    │
    ├── docs/
    │   └── PROMPTS.md
    │
    ├── .opencode/
    │   └── skills/
    │       └── solid-review/
    │           └── SKILL.md
    │
    ├── 01-Principles-OOD-Without/
    │   └── store/
    │
    └── 02-Principles-OOD-Applied/
        ├── REFACTORING_PLAN.md
        ├── store/
        └── tests/
```

لینک:

```text
https://github.com/Ali-Najar/SELab-Exp2-SOLID-OpenCode
```

---

## کاربر

ایدی گیتهابم Ali-Najar عه و خب اسم ریپو و چیزای خالی رو خودت بزار . گام به گام مراحل پروژه رو بگو

---

## دستیار

از اینجا به بعد همه‌چیز را با GitHub ID **`Ali-Najar`** و Repository **`SELab-Exp2-SOLID-OpenCode`** جلو می‌بریم. روند اصلی همان ساخت دو نسخه مستقل، اضافه‌کردن Cash در نسخه اولیه، Refactor نسخه دوم، Commit نسخه SOLID بدون Cash، اضافه‌کردن Cash در نسخه SOLID، تست و مقایسه است.

نام Repository:

```text
SELab-Exp2-SOLID-OpenCode
```

URL:

```text
https://github.com/Ali-Najar/SELab-Exp2-SOLID-OpenCode
```

ساختار نهایی پیشنهادی:

```text
SELab-Exp2-SOLID-OpenCode/
│
├── README.md
├── AGENTS.md
│
├── .opencode/
│   └── skills/
│       └── solid-review/
│           └── SKILL.md
│
├── 01-Principles-OOD-Without/
│   └── store/
│
└── 02-Principles-OOD-Applied/
    ├── REFACTORING_PLAN.md
    ├── store/
    └── tests/
```

ترتیب مهم:

```text
Original
   |
   +---------------------------+
   |                           |
   v                           v
Version 01                  Version 02
   |                           |
Add Cash                    Analyze SOLID
   |                           |
Commit                        Skill
   |                           |
Record Diff                   Plan
                               |
                            Refactor
                               |
                            Test
                               |
                    COMMIT WITHOUT CASH
                               |
                          Tag checkpoint
                               |
                           Add Cash
                               |
                            Test
                               |
                            Commit
                               |
                        Compare Diffs
```

دستورهای کلیدی Git:

```bash
git clone https://github.com/soleyman79/Software-Engineering-Lab-Experiment2.git
cd Software-Engineering-Lab-Experiment2

git remote rename origin upstream
git remote add origin https://github.com/Ali-Najar/SELab-Exp2-SOLID-OpenCode.git

git branch -M main
git push -u origin main
```

بعد دو نسخه پایه ساخته می‌شوند، README و `AGENTS.md` ایجاد می‌شوند، Cash نسخه اول با کمترین تغییر اضافه می‌شود، پنج اصل SOLID تحلیل می‌شوند، Skill ساخته می‌شود، Plan گرفته و بررسی می‌شود، Build اجرا می‌شود، تست‌ها اضافه می‌شوند، نسخه SOLID بدون Cash Commit و Tag می‌شود و سپس Cash به‌صورت Strategy اضافه می‌شود.

---

## کاربر

چون تک نفره هستم نیازی به کانبان ندارم پس همه مراحل رو بدون کانبان بگو بهم

---

## دستیار

بله. مسیر را کاملاً **تک‌نفره و بدون Kanban/Project Board** می‌چینیم و از اینجا به بعد فرض می‌کنیم فقط خودت روی پروژه کار می‌کنی.

فقط یک نکته مهم: در دستورالعمل عمومی آزمایشگاه، Kanban به‌عنوان بخشی از نحوه نمایش فعالیت‌های گروه ذکر شده و حتی روی عمومی بودن آن تأکید شده است. در فایل آزمایش ۲ هم استثنای صریحی برای دانشجوی تک‌نفره نوشته نشده است. بنابراین راهنمای زیر را بدون Kanban می‌دهم، اما بهتر است مطمئن باشی TA واقعاً برای حالت تک‌نفره Kanban را لازم نمی‌داند.

## نقشه نهایی پروژه تو

GitHub ID:

```text
Ali-Najar
```

اسم Repository:

```text
SELab-Exp2-SOLID-OpenCode
```

آدرس نهایی:

```text
https://github.com/Ali-Najar/SELab-Exp2-SOLID-OpenCode
```

ساختار نهایی:

```text
SELab-Exp2-SOLID-OpenCode/
│
├── README.md
├── AGENTS.md
├── .gitignore
│
├── docs/
│   └── PROMPTS.md
│
├── .opencode/
│   └── skills/
│       └── solid-review/
│           └── SKILL.md
│
├── 01-Principles-OOD-Without/
│   └── store/
│
└── 02-Principles-OOD-Applied/
    ├── REFACTORING_PLAN.md
    ├── store/
    └── tests/
```

اصل مسئله این است که اول Cash را روی نسخه خراب اولیه اضافه کنی، بعد پروژه را از نظر SOLID اصلاح کنی، و سپس **همان Cash را دوباره** روی طراحی اصلاح‌شده اضافه کنی و میزان تغییر لازم را مقایسه کنی.

### مرحله ۱ — ساخت Repository

Repository:

```text
SELab-Exp2-SOLID-OpenCode
```

Description:

```text
Software Engineering Lab - Experiment 2 - SOLID Principles and OpenCode
```

### مرحله ۲ — گرفتن پروژه پایه

```bash
git clone https://github.com/soleyman79/Software-Engineering-Lab-Experiment2.git
cd Software-Engineering-Lab-Experiment2

git remote rename origin upstream
git remote add origin https://github.com/Ali-Najar/SELab-Exp2-SOLID-OpenCode.git
git remote -v

git branch -M main
git push -u origin main
```

### مرحله ۳ — ثبت نسخه اصلی

```bash
git tag baseline
git push origin baseline
```

### مرحله ۴ — ساخت دو نسخه مستقل

```bash
mkdir 01-Principles-OOD-Without
mkdir 02-Principles-OOD-Applied

cp -R store 01-Principles-OOD-Without/
cp -R store 02-Principles-OOD-Applied/
rm -rf store

git add .
git commit -m "chore: prepare experiment baseline versions"
git push
```

### مرحله ۵ — README اولیه

```markdown
# آزمایش دوم آزمایشگاه مهندسی نرم‌افزار

## مروری بر اصول طراحی شی‌گرا (SOLID) و استفاده از OpenCode

**نام دانشجو:** Ali Najar  
**GitHub ID:** Ali-Najar  
**Repository:** SELab-Exp2-SOLID-OpenCode  
**نحوه انجام آزمایش:** تک‌نفره
```

### مرحله ۶ — راه‌اندازی OpenCode

```bash
opencode
```

داخل OpenCode:

```text
/init
```

### مرحله ۷ — تنظیم `AGENTS.md`

```markdown
# Project Instructions

This repository contains two independent versions of the same project.

## 01-Principles-OOD-Without

This version represents the original design.

Rules:
- Do not apply SOLID refactoring here.
- Add the requested cash payment using the existing architecture.
- Make only necessary changes.
- Preserve existing behavior.
- Explain changes before applying them.

## 02-Principles-OOD-Applied

This version is used for SOLID refactoring.

Rules:
- Do not add cash payment before refactoring is complete.
- Analyze SRP, OCP, LSP, ISP and DIP.
- Produce a plan before major modifications.
- Avoid unnecessary overengineering.
- Preserve intended behavior.
- Run tests after refactoring.
- Commit the SOLID version before adding cash.

## General

- AI output must be reviewed by the student.
- Do not silently change business rules.
- Prefer small and understandable abstractions.
- Explain important architectural decisions.
```

### مرحله ۸ — شناخت پروژه اصلی

```bash
cd 01-Principles-OOD-Without
python -m store.main
```

فایل‌ها و کلاس‌های مهم:

```text
models.py
payment.py
pricing.py
notification.py
storage.py
order_service.py
main.py

Order
BundleOrder
OrderService
PaymentProcessor
DiscountCalculator
NotificationService
MySqlDatabase
```

### مرحله ۹ — ثبت رفتار اولیه

خروجی برنامه و رفتار `BundleOrder` را بررسی و نگه دار.

### مرحله ۱۰ — افزودن Cash به نسخه Without

Prompt:

```text
Analyze the payment implementation in
01-Principles-OOD-Without.

I need to add a new payment method named "cash".

Constraints:
- Do not refactor the existing architecture.
- Do not apply SOLID improvements.
- Make the minimum possible changes.
- Preserve the current coding style.
- First explain which files need to change and why.
```

### مرحله ۱۱ — تغییر `payment.py`

```python
elif method == "cash":
    print(f"[payment] Cash payment {amount:.2f}")
    return f"paid_by_cash:{amount:.2f}"
```

### مرحله ۱۲ — اضافه کردن Cash Order

```python
cash_order = Order(
    id=104,
    customer=regular,
    payment_method="cash",
    items=[
        OrderItem(
            5,
            "Notebook",
            15.00,
            2,
        )
    ],
)
```

و:

```python
service.process_order(cash_order)
```

### مرحله ۱۳ — اجرای نسخه Without

```bash
python -m store.main
git status
git diff
```

### مرحله ۱۴ — Commit نسخه Without

```bash
git add 01-Principles-OOD-Without
git commit -m "feat: add cash payment to non-solid version"
git push

git tag non-solid-with-cash
git push origin non-solid-with-cash
```

### مرحله ۱۵ — ثبت آمار تغییر Cash اول

```bash
git show --stat HEAD
git show --numstat HEAD
```

جدول:

| فایل | نوع تغییر | علت |
|---|---|---|
| `payment.py` | اضافه‌شدن شرط Cash | معماری فعلی برای روش جدید نیازمند تغییر Processor بود |
| `main.py` | اضافه‌شدن Cash Order | برای Demo و بررسی قابلیت |

### مرحله ۱۶ تا ۲۲ — تحلیل SOLID

- SRP: `OrderService`
- OCP: `PaymentProcessor`, `DiscountCalculator`
- LSP: `BundleOrder`
- ISP: `NotificationService`
- DIP: concrete dependency creation در `OrderService`

جدول:

| اصل | رعایت شده؟ | محل | مشکل |
|---|---|---|---|
| SRP | خیر | `OrderService` | چند مسئولیت |
| OCP | خیر | `PaymentProcessor` | روش جدید نیازمند branch جدید |
| OCP | خیر | `DiscountCalculator` | قانون جدید نیازمند تغییر کلاس |
| LSP | خیر | `BundleOrder` | رفتار subtype با Order سازگار نیست |
| ISP | خیر | `NotificationService` | interface بیش از نیاز clientها |
| DIP | خیر | `OrderService` | وابستگی مستقیم به concrete classها |

### مرحله ۲۳ — ساخت Skill

```bash
mkdir -p .opencode/skills/solid-review
```

```markdown
---
name: solid-review
description: Analyze Python object-oriented code for SOLID violations and propose controlled refactoring.
---

# SOLID Review

1. Read the relevant Python source files.
2. Analyze SRP, OCP, LSP, ISP and DIP.
3. For each violation provide:
   - exact file
   - exact class
   - evidence
   - reason for violation
   - proposed refactoring
   - rationale
4. Do not modify code without producing a plan first.
5. Avoid unnecessary abstractions.
6. Preserve existing intended behavior.
7. After approval, apply changes incrementally.
8. Run tests after important changes.
9. Report uncertainties instead of guessing.
```

### مرحله ۲۴ — Plan Mode

```text
Use the solid-review skill.

Analyze 02-Principles-OOD-Applied for violations of:
SRP, OCP, LSP, ISP and DIP.

For every violation provide exact file/class evidence.

Then create an ordered refactoring plan.

Constraints:
- Do not add cash yet.
- Preserve intended behavior.
- Avoid overengineering.
- Keep OrderService as an orchestration service.
- PaymentProcessor should support extension without if/elif changes.
- BundleOrder should be substitutable for Order.
- Notification clients should not depend on unsupported operations.
- High-level services should not construct their concrete dependencies.

Do not modify any source file yet.
```

### مرحله ۲۵ — Plan را بررسی کن

Plan را کورکورانه نپذیر و overengineering را حذف کن.

### مرحله ۲۶ — ذخیره Plan

```markdown
# Refactoring Plan

1. Record baseline behavior.
2. Fix BundleOrder substitutability.
3. Extract validation responsibility.
4. Extract shipping responsibility.
5. Extract receipt responsibility.
6. Introduce payment abstraction.
7. Convert payments to strategies.
8. Convert discount conditions to rules.
9. Split notification implementations.
10. Introduce repository abstraction.
11. Inject dependencies into OrderService.
12. Add regression tests.
13. Run the full application.
14. Commit the refactored version before adding cash.
```

### مرحله ۲۷ — Build Mode و Refactoring

```text
Apply the approved refactoring plan incrementally.

After every major step:
- explain what changed,
- run the relevant tests or application,
- report any behavior difference.

Do not add cash payment yet.
```

### مرحله ۲۸ — ساختار پیشنهادی نسخه SOLID

```text
store/
├── models.py
├── contracts.py
├── validation.py
├── pricing.py
├── shipping.py
├── payment.py
├── notification.py
├── storage.py
├── receipt.py
├── order_service.py
└── main.py
```

### مرحله ۲۹ تا ۳۴ — Refactor

- Payment Strategy
- Notification split
- OrderService orchestration
- Composition Root در `main.py`
- اصلاح `BundleOrder`
- تست‌ها

### مرحله ۳۵ — اجرای نسخه SOLID بدون Cash

```bash
python -m store.main
python -m unittest discover -s tests -v
```

### مرحله ۳۶ — Commit نسخه SOLID بدون Cash

```bash
git add 02-Principles-OOD-Applied
git commit -m "refactor: apply SOLID principles to second version"
git push

git tag solid-before-cash
git push origin solid-before-cash
```

### مرحله ۳۷ تا ۴۱ — Cash بعد از SOLID

Prompt:

```text
Now add the same cash payment capability to
02-Principles-OOD-Applied.

Constraints:
- Do not modify PaymentProcessor with an if/elif branch.
- Extend the existing payment abstraction.
- Keep core payment logic unchanged.
- Add a test for cash payment.
- Explain the required changes before editing.
```

`CashPayment`:

```python
from .contracts import PaymentMethod

class CashPayment(PaymentMethod):
    @property
    def key(self):
        return "cash"

    def pay(self, order, amount):
        print(f"[payment] Cash payment {amount:.2f}")
        return f"paid_by_cash:{amount:.2f}"
```

Commit:

```bash
git add .
git commit -m "feat: add cash payment to SOLID version"
git push

git tag solid-with-cash
git push origin solid-with-cash
```

### مرحله ۴۲ — مقایسه

```bash
git diff --stat solid-before-cash..solid-with-cash
git diff --numstat solid-before-cash..solid-with-cash
```

جدول:

| معیار | قبل از SOLID | بعد از SOLID |
|---|---|---|
| تغییر `PaymentProcessor` | بله | خیر |
| اضافه کردن branch | بله | خیر |
| extension جدید مستقل | خیر | بله |
| وابستگی به concrete logic | بیشتر | کمتر |
| احتمال Regression | بیشتر | کمتر |
| تست‌پذیری | پایین‌تر | بالاتر |

### مرحله ۴۳ تا ۴۷ — مستندسازی OpenCode و README

`docs/PROMPTS.md` شامل Promptهای واقعی شود. در README نام ابزار، نسخه OpenCode، مدل، Provider و ارزیابی واقعی Agent نوشته شود.

### مرحله ۴۸ — فیلم

حداکثر ۱۵ دقیقه با معرفی پروژه، Cash قبل از SOLID، تحلیل پنج اصل، Skill/Plan، Refactor، Cash بعد از SOLID، تست و AI.

### ترتیب خیلی خلاصه

1. Repository بساز.
2. پروژه پایه را Clone کن.
3. دو نسخه مستقل بساز.
4. README و `AGENTS.md` ایجاد کن.
5. پروژه اولیه را اجرا کن.
6. Cash را بدون SOLID روی نسخه 01 اضافه کن.
7. Commit و Diff ثبت کن.
8. نسخه 02 را برای پنج اصل تحلیل کن.
9. Skill بساز.
10. Plan بگیر و بررسی کن.
11. Refactor کن.
12. تست‌ها را اضافه کن.
13. نسخه SOLID بدون Cash را Commit و Tag کن.
14. Cash را روی نسخه SOLID اضافه کن.
15. تست کن.
16. Commit و Tag کن.
17. دو Diff را مقایسه کن.
18. Promptها و ارزیابی OpenCode را ثبت کن.
19. README را کامل کن.
20. فیلم را ضبط و لینک GitHub را تحویل بده.

---

## کاربر

من داخل ویندوز هستم اینارو در نظر بگیر و همه مراحل رو بده

---

## دستیار

حتماً. از اینجا به بعد کل مسیر را برای **Windows 10/11 + PowerShell + GitHub + کار تک‌نفره و بدون Kanban** می‌چینیم. تمام دستورهای ترمینال این پاسخ برای **PowerShell** هستند، نه Linux.

یک نکته را فقط از نظر تحویل در نظر داشته باش: دستورالعمل عمومی آزمایشگاه Kanban را جزو الزامات کار گروهی آورده است. با فرض اینکه برای حالت تک‌نفره‌ات عدم استفاده از Kanban پذیرفته شده، در ادامه **هیچ Board، Issue یا Kanbanای نمی‌سازیم** و روند کارت را با Commitهای Git مستند می‌کنیم.

---

# 0. مشخصات ثابتی که از اینجا استفاده می‌کنیم

GitHub ID:

```text
Ali-Najar
```

نام Repository:

```text
SELab-Exp2-SOLID-OpenCode
```

آدرس نهایی:

```text
https://github.com/Ali-Najar/SELab-Exp2-SOLID-OpenCode
```

نام دو پوشه:

```text
01-Principles-OOD-Without
02-Principles-OOD-Applied
```

ساختار نهایی پروژه:

```text
SELab-Exp2-SOLID-OpenCode
│
├── README.md
├── AGENTS.md
├── .gitignore
│
├── docs
│   └── PROMPTS.md
│
├── .opencode
│   └── skills
│       └── solid-review
│           └── SKILL.md
│
├── 01-Principles-OOD-Without
│   └── store
│       ├── main.py
│       ├── models.py
│       ├── notification.py
│       ├── order_service.py
│       ├── payment.py
│       ├── pricing.py
│       └── storage.py
│
└── 02-Principles-OOD-Applied
    ├── REFACTORING_PLAN.md
    ├── store
    │   └── ...
    └── tests
        └── test_store.py
```

اصل آزمایش:

```text
پروژه اولیه
   |
   +----> نسخه 01 ---> Cash بدون SOLID
   |
   +----> نسخه 02 ---> Refactor با SOLID ---> Cash
```

---

# 1. نصب ابزارهای لازم در Windows

پیشنهاد:

```text
Windows PowerShell
VS Code
Git
Python
Node.js
OpenCode
```

## بررسی Git

```powershell
git --version
```

اگر Git نصب نیست:

```powershell
winget install --id Git.Git -e
```

## بررسی Python

```powershell
py --version
```

اگر نصب نیست، Python را نصب کن و `Add Python to PATH` را فعال کن.

## نصب Node.js

```powershell
node --version
npm.cmd --version
```

اگر نصب نیست:

```powershell
winget install --id OpenJS.NodeJS.LTS -e
```

## نصب OpenCode

```powershell
npm.cmd install -g opencode-ai
```

سپس:

```powershell
opencode --version
```

## نصب VS Code

```powershell
winget install --id Microsoft.VisualStudioCode -e
```

---

# 2. تنظیم اولیه Git

```powershell
git config --global user.name "Ali Najar"
git config --global user.email "YOUR_GITHUB_EMAIL"
```

بررسی:

```powershell
git config --global user.name
git config --global user.email
```

---

# 3. Repository خودت را در GitHub بساز

نام:

```text
SELab-Exp2-SOLID-OpenCode
```

Description:

```text
Software Engineering Lab - Experiment 2 - SOLID Principles and OpenCode
```

Visibility:

```text
Public
```

README/.gitignore/license را از GitHub نساز.

---

# 4. پوشه کاری در Windows

```powershell
cd $HOME\Documents
New-Item -ItemType Directory -Path "SELab" -Force
cd .\SELab
```

---

# 5. Clone پروژه اصلی

```powershell
git clone https://github.com/soleyman79/Software-Engineering-Lab-Experiment2.git
cd .\Software-Engineering-Lab-Experiment2
```

---

# 6. Remote

```powershell
git remote rename origin upstream
git remote add origin https://github.com/Ali-Najar/SELab-Exp2-SOLID-OpenCode.git
git remote -v
```

بعد:

```powershell
git branch -M main
git push -u origin main
```

---

# 7. Tag اولیه

```powershell
git tag baseline-original
git push origin baseline-original
```

---

# 8. دو نسخه مستقل پروژه

```powershell
New-Item -ItemType Directory -Path ".\01-Principles-OOD-Without" -Force
New-Item -ItemType Directory -Path ".\02-Principles-OOD-Applied" -Force
```

کپی:

```powershell
Copy-Item -Path ".\store" -Destination ".\01-Principles-OOD-Without\store" -Recurse
Copy-Item -Path ".\store" -Destination ".\02-Principles-OOD-Applied\store" -Recurse
```

بررسی:

```powershell
Get-ChildItem .\01-Principles-OOD-Without\store
Get-ChildItem .\02-Principles-OOD-Applied\store
```

حذف store اصلی:

```powershell
Remove-Item -Path ".\store" -Recurse -Force
```

Commit:

```powershell
git status
git add .
git commit -m "chore: prepare independent experiment baselines"
git push
```

---

# 9. README اولیه

```powershell
New-Item -ItemType File -Path ".\README.md" -Force
code .\README.md
```

ابتدای README:

```markdown
# آزمایش دوم آزمایشگاه مهندسی نرم‌افزار

## مروری بر اصول طراحی شی‌گرا (SOLID) و استفاده از OpenCode

**نام دانشجو:** Ali Najar  
**GitHub ID:** Ali-Najar  
**Repository:** SELab-Exp2-SOLID-OpenCode  
**Repository URL:** https://github.com/Ali-Najar/SELab-Exp2-SOLID-OpenCode  
**نحوه انجام آزمایش:** تک‌نفره
```

---

# 10. اجرای اولیه پروژه

```powershell
cd .\01-Principles-OOD-Without
py -m store.main
```

نکته مهم `BundleOrder`: `items=[]` دارد و `subtotal`/`item_count` از `items` می‌آیند، در حالی که سفارش‌های واقعی داخل `orders` هستند. در `OrderService` هم special case برای `BundleOrder` وجود دارد.

---

# 11. OpenCode را Initialize کن

به Root برگرد:

```powershell
cd ..
opencode
```

داخل OpenCode:

```text
/init
```

سپس `AGENTS.md` را بررسی کن.

---

# 12. `AGENTS.md`

```markdown
# SELab Experiment 2 Instructions

This repository contains two independent versions of the same project.

## 01-Principles-OOD-Without

- This folder represents the original non-SOLID architecture.
- Do not apply SOLID refactoring in this folder.
- Implement cash payment using the existing design.
- Make only the minimum required changes.
- Explain proposed changes before applying them.
- Preserve existing behavior.

## 02-Principles-OOD-Applied

- Start from the original version without cash.
- Analyze SRP, OCP, LSP, ISP and DIP.
- Do not add cash before SOLID refactoring is complete.
- Produce a refactoring plan before making major changes.
- Avoid unnecessary abstractions and overengineering.
- Preserve intended business behavior.
- Add regression tests.
- Commit the SOLID-refactored version before adding cash.
- Add cash only after the previous checkpoint.

## AI Usage

- AI is a development assistant, not the final decision maker.
- Explain important architectural decisions.
- Report uncertainties.
- Do not silently change business rules.
- Verify changes after every major refactoring step.
```

Commit:

```powershell
git add AGENTS.md
git commit -m "docs: add OpenCode project instructions"
git push
```

---

# 13. مرحله اول: Cash بدون SOLID

OpenCode:

```powershell
opencode
```

Prompt:

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

در `payment.py`:

```python
elif method == "cash":
    print(f"[payment] Cash payment {amount:.2f}")
    return f"paid_by_cash:{amount:.2f}"
```

در `main.py`:

```python
cash_order = Order(
    id=104,
    customer=regular,
    payment_method="cash",
    items=[
        OrderItem(5, "Notebook", 15.00, 2)
    ],
)
```

و Cash Order را در demo اجرا کن.

تست:

```powershell
cd .\01-Principles-OOD-Without
py -m store.main
```

برگرد root و diff:

```powershell
cd ..
git diff -- .\01-Principles-OOD-Without
```

Commit:

```powershell
git add .\01-Principles-OOD-Without
git commit -m "feat: add cash payment to non-solid version"
git push

git tag non-solid-with-cash
git push origin non-solid-with-cash
```

آمار:

```powershell
git show --stat HEAD
git show --numstat HEAD
```

---

# 14. تحلیل SOLID نسخه دوم

```powershell
cd .\02-Principles-OOD-Applied
py -m store.main
```

### SRP

`OrderService` هم‌زمان validation، pricing، shipping، payment، persistence، notification و receipt را انجام می‌دهد.

### OCP

`PaymentProcessor` برای credit card، PayPal و Bitcoin `if/elif` دارد و برای Cash هم نیازمند branch جدید است. `DiscountCalculator` نیز condition-based است.

### LSP

`BundleOrder` از `Order` ارث می‌برد اما `items=[]` دارد و special case لازم می‌شود.

### ISP

`NotificationService` چند operation دارد و `SmsOnlyNotifier` مجبور به operationهای نامربوط است.

### DIP

`OrderService` خودش `DiscountCalculator()`, `PaymentProcessor()`, `NotificationService()`, `MySqlDatabase()` را می‌سازد.

جدول:

| اصل | رعایت شده؟ | محل | دلیل |
|---|---|---|---|
| SRP | خیر | `OrderService` | چند مسئولیت مستقل |
| OCP | خیر | `PaymentProcessor` | روش پرداخت جدید نیازمند branch جدید |
| OCP | خیر | `DiscountCalculator` | قانون جدید نیازمند تغییر کلاس |
| LSP | خیر | `BundleOrder` | قرارداد `Order.items/subtotal` را رعایت نمی‌کند |
| ISP | خیر | `NotificationService` | client مجبور به عملیات غیرضروری است |
| DIP | خیر | `OrderService` | dependencyهای concrete را خودش ایجاد می‌کند |

---

# 15. Skill

```powershell
New-Item -ItemType Directory -Path ".\.opencode\skills\solid-review" -Force
New-Item -ItemType File -Path ".\.opencode\skills\solid-review\SKILL.md" -Force
code .\.opencode\skills\solid-review\SKILL.md
```

محتوا:

```markdown
---
name: solid-review
description: Analyze Python object-oriented code for SOLID violations and propose safe incremental refactoring.
---

# SOLID Review Skill

When analyzing a Python object-oriented project:

1. Read all relevant source files before making conclusions.
2. Analyze the code for:
   - Single Responsibility Principle
   - Open/Closed Principle
   - Liskov Substitution Principle
   - Interface Segregation Principle
   - Dependency Inversion Principle
3. For every violation report:
   - exact file
   - exact class
   - concrete code evidence
   - why it violates the principle
   - proposed refactoring
   - why the proposed solution is appropriate
   - possible risks
4. Do not modify files immediately.
5. Produce an ordered refactoring plan first.
6. Avoid overengineering.
7. Preserve intended application behavior.
8. Wait for user approval before applying major modifications.
9. Apply approved refactoring incrementally.
10. Run tests or executable examples after every major change.
11. If unsure about a violation or behavior, report the uncertainty instead of guessing.
```

Commit:

```powershell
git add .\.opencode
git commit -m "feat: add SOLID review OpenCode skill"
git push
```

---

# 16. Plan Mode

```powershell
opencode
```

Prompt:

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

Plan پیشنهادی:

```text
1. Preserve baseline behavior
2. Fix BundleOrder substitutability
3. Extract validation
4. Extract shipping
5. Extract receipt output
6. Introduce payment abstraction
7. Convert payment implementations to strategies
8. Convert discounts to rules
9. Split notification implementations
10. Abstract persistence
11. Inject dependencies into OrderService
12. Add regression tests
13. Verify behavior
14. Commit refactored version WITHOUT cash
15. Add cash afterward
```

فایل:

```text
02-Principles-OOD-Applied\REFACTORING_PLAN.md
```

---

# 17. Build Mode

Prompt:

```text
Apply the approved refactoring plan to
02-Principles-OOD-Applied incrementally.

After each major step:
1. explain the modification,
2. run the relevant verification,
3. report unexpected behavior.

Do not add cash payment yet.
Do not modify 01-Principles-OOD-Without.
```

---

# 18. معماری SOLID

```text
02-Principles-OOD-Applied
│
├── REFACTORING_PLAN.md
│
├── store
│   ├── main.py
│   ├── models.py
│   ├── contracts.py
│   ├── validation.py
│   ├── shipping.py
│   ├── pricing.py
│   ├── payment.py
│   ├── notification.py
│   ├── storage.py
│   ├── receipt.py
│   └── order_service.py
│
└── tests
    └── test_store.py
```

### Payment abstraction

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @property
    @abstractmethod
    def key(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def pay(self, order, amount: float) -> str:
        raise NotImplementedError

class PaymentService(ABC):
    @abstractmethod
    def process(self, order, amount: float) -> str:
        raise NotImplementedError
```

### PaymentProcessor

```python
class PaymentProcessor(PaymentService):
    def __init__(self, methods):
        self._methods = {
            method.key: method
            for method in methods
        }

    def process(self, order, amount):
        method = self._methods.get(order.payment_method)
        if method is None:
            raise ValueError(f"Unknown payment method: {order.payment_method!r}")
        return method.pay(order, amount)
```

### BundleOrder

```python
class BundleOrder(Order):
    def __init__(self, id, customer, orders):
        flattened_items = [
            item
            for child_order in orders
            for item in child_order.items
        ]

        super().__init__(
            id=id,
            customer=customer,
            items=flattened_items,
        )

        self.orders = orders
```

### Validation

```python
class DefaultOrderValidator(OrderValidator):
    def validate(self, order) -> None:
        if not order.items:
            raise ValueError("Order has no items")
        if not order.payment_method:
            raise ValueError("Order has no payment method")
```

### Shipping

```python
class StandardShippingService(ShippingService):
    def calculate(self, order, subtotal: float) -> float:
        return 5.0 if subtotal < 100 else 0.0
```

### Notification

```python
class EmailNotifier(Notifier):
    def send(self, customer, message: str) -> None:
        print(f"[email] to {customer.email}: {message}")

class SmsNotifier(Notifier):
    def send(self, customer, message: str) -> None:
        print(f"[sms] to {customer.phone}: {message}")

class PushNotifier(Notifier):
    def send(self, customer, message: str) -> None:
        print(f"[push] to {customer.name}: {message}")
```

### Persistence

```python
class MySqlOrderRepository(OrderRepository):
    def __init__(self, connection_string: str = "mysql://localhost/store"):
        self._connection_string = connection_string
        self._orders = {}

    def save(self, order) -> None:
        self._orders[order.id] = order

    def load(self, order_id: int):
        return self._orders.get(order_id)
```

### Receipt

```python
class ConsoleReceiptPrinter(ReceiptPrinter):
    def print_receipt(
        self,
        order,
        subtotal,
        discount,
        shipping,
        total,
        receipt,
    ) -> None:
        print(f"--- Receipt for order {order.id} ---")
        for item in order.items:
            print(f" {item.name:20s} x{item.quantity} ${item.line_total:.2f}")
        print(f" Subtotal ${subtotal:.2f}")
        print(f" Discount -${discount:.2f}")
        print(f" Shipping ${shipping:.2f}")
        print(f" TOTAL ${total:.2f}")
        print(f" Payment {receipt}")
```

### Pricing rules

```python
class VipDiscountRule:
    def applies(self, order):
        return order.customer.is_vip

    def calculate(self, order):
        return order.subtotal * 0.20

class BulkDiscountRule:
    def applies(self, order):
        return order.item_count >= 10

    def calculate(self, order):
        return order.subtotal * 0.10

class WelcomeCouponDiscountRule:
    def applies(self, order):
        return "WELCOME10" in order.coupons

    def calculate(self, order):
        return order.subtotal * 0.10

class RuleBasedDiscountCalculator:
    def __init__(self, rules):
        self.rules = list(rules)

    def calculate(self, order):
        for rule in self.rules:
            if rule.applies(order):
                return round(rule.calculate(order), 2)
        return 0.0
```

### OrderService جدید

```python
class OrderService:
    def __init__(
        self,
        validator,
        pricing,
        shipping,
        payment,
        repository,
        notifiers,
        receipt_printer,
    ):
        self.validator = validator
        self.pricing = pricing
        self.shipping = shipping
        self.payment = payment
        self.repository = repository
        self.notifiers = list(notifiers)
        self.receipt_printer = receipt_printer

    def process_order(self, order, notify=True):
        self.validator.validate(order)
        subtotal = order.subtotal
        discount = self.pricing.calculate(order)
        shipping = self.shipping.calculate(order, subtotal)
        total = round(subtotal - discount + shipping, 2)
        receipt = self.payment.process(order, total)
        order.status = "paid"
        self.repository.save(order)

        if notify:
            message = f"Order {order.id} total ${total:.2f} ({receipt})"
            for notifier in self.notifiers:
                notifier.send(order.customer, message)

        self.receipt_printer.print_receipt(
            order,
            subtotal,
            discount,
            shipping,
            total,
            receipt,
        )
        return order
```

### Composition Root

```python
payment_processor = PaymentProcessor(
    [
        CreditCardPayment(),
        PayPalPayment(),
        BitcoinPayment(),
    ]
)

pricing = RuleBasedDiscountCalculator(
    [
        VipDiscountRule(),
        BulkDiscountRule(),
        WelcomeCouponDiscountRule(),
    ]
)

service = OrderService(
    validator=DefaultOrderValidator(),
    pricing=pricing,
    shipping=StandardShippingService(),
    payment=payment_processor,
    repository=MySqlOrderRepository(),
    notifiers=[EmailNotifier(), SmsNotifier()],
    receipt_printer=ConsoleReceiptPrinter(),
)
```

---

# 19. تست نسخه SOLID بدون Cash

```powershell
cd .\02-Principles-OOD-Applied
py -m store.main
py -m unittest discover -s tests -v
```

Commit:

```powershell
cd ..
git add .\02-Principles-OOD-Applied
git commit -m "refactor: apply SOLID principles to second version"
git push

git tag solid-before-cash
git push origin solid-before-cash
```

---

# 20. Cash بعد از SOLID

Prompt:

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

Cash:

```python
from store.contracts import PaymentMethod

class CashPayment(PaymentMethod):
    @property
    def key(self) -> str:
        return "cash"

    def pay(self, order, amount: float) -> str:
        print(f"[payment] Cash payment {amount:.2f}")
        return f"paid_by_cash:{amount:.2f}"
```

Register:

```python
payment_processor = PaymentProcessor(
    [
        CreditCardPayment(),
        PayPalPayment(),
        BitcoinPayment(),
        CashPayment(),
    ]
)
```

تست:

```python
def test_cash_payment(self):
    payment = CashPayment()
    result = payment.pay(self.order, 100.0)
    self.assertEqual(result, "paid_by_cash:100.00")
```

اجرای تست:

```powershell
cd .\02-Principles-OOD-Applied
py -m unittest discover -s tests -v
py -m store.main
```

Commit و Tag:

```powershell
cd ..
git add .\02-Principles-OOD-Applied
git commit -m "feat: add cash payment to SOLID version"
git push

git tag solid-with-cash
git push origin solid-with-cash
```

---

# 21. مقایسه

```powershell
git diff --stat solid-before-cash..solid-with-cash
git diff --numstat solid-before-cash..solid-with-cash
```

برای نسخه اول commit مربوط به Cash را با `git log --oneline` پیدا کن و:

```powershell
git show --stat COMMIT_HASH
git show --numstat COMMIT_HASH
```

تفاوت اصلی:

```text
Before SOLID:
new feature -> modify existing core logic

After SOLID:
new feature -> create new implementation -> register implementation
```

جدول:

| معیار | قبل از SOLID | بعد از SOLID |
|---|---|---|
| تغییر `PaymentProcessor` | بله | خیر |
| branch جدید | بله | خیر |
| implementation مستقل | خیر | بله |
| Coupling | بیشتر | کمتر |
| ریسک Regression | بیشتر | کمتر |
| امکان تست مستقل | کمتر | بیشتر |
| Dependency Injection | ندارد | دارد |
| special case برای Bundle | دارد | ندارد |

---

# 22. مستندسازی Promptها و AI

```powershell
New-Item -ItemType Directory -Path ".\docs" -Force
New-Item -ItemType File -Path ".\docs\PROMPTS.md" -Force
```

ساختار:

```markdown
# OpenCode Interaction Log

## Prompt 1 - Initial Project Analysis
...

## Prompt 2 - Add Cash Without SOLID
...

## Prompt 3 - SOLID Analysis
...

## Prompt 4 - Generate Refactoring Plan
...

## Prompt 5 - Apply Refactoring
...

## Prompt 6 - Add Cash After SOLID
...
```

README:

```markdown
## مستندسازی استفاده از هوش مصنوعی

| مورد | مقدار |
|---|---|
| ابزار | OpenCode |
| نسخه OpenCode | ... |
| مدل | ... |
| Provider | ... |
| سیستم عامل | Windows |
| Terminal | PowerShell |
```

نسخه:

```powershell
opencode --version
```

پرسش‌های ارزیابی:

```markdown
# ارزیابی OpenCode

## بخش‌هایی که Agent به‌درستی تحلیل کرد
...

## بخش‌هایی که نیاز به اصلاح پاسخ Agent داشتند
...

## مهم‌ترین Promptهای استفاده‌شده
...

## تأثیر Skill بر کیفیت خروجی Agent
...

## تغییراتی که در اجرای دوباره آزمایش انجام می‌دادم
...
```

---

# 23. README تک‌نفره

موارد Kanban/Board/Issues حذف شوند و به‌جایش:

```markdown
## روند انجام تک‌نفره پروژه

این آزمایش به‌صورت تک‌نفره انجام شده است. برای حفظ قابلیت
ردیابی مراحل توسعه، هر مرحله اصلی در یک Commit مجزا ثبت شده
و از Tagهای Git برای مشخص‌کردن نقاط مهم مقایسه استفاده شده است.
```

---

# 24. Git History و Tags

```powershell
git log --oneline --decorate
git tag
git status
```

Tags مورد انتظار:

```text
baseline-original
non-solid-with-cash
solid-before-cash
solid-with-cash
```

Status نهایی:

```text
nothing to commit, working tree clean
```

---

# 25. ساختار نهایی

```powershell
tree /F
```

README باید شامل این بخش‌ها باشد:

1. مشخصات دانشجو و Repository
2. هدف آزمایش
3. محیط اجرا: Windows/PowerShell
4. ساختار Repository
5. نصب و راه‌اندازی OpenCode
6. اجرای پروژه اولیه
7. افزودن Cash بدون SOLID
8. جدول تغییرات Cash اول
9. تحلیل SRP
10. تحلیل OCP
11. تحلیل LSP
12. تحلیل ISP
13. تحلیل DIP
14. طراحی Skill
15. Plan اولیه OpenCode
16. بررسی و اصلاح Plan
17. معماری Refactorشده
18. تست‌های نسخه Refactorشده
19. افزودن Cash بعد از SOLID
20. جدول تغییرات Cash دوم
21. مقایسه دو نسخه
22. ارزیابی OpenCode
23. Promptها
24. مستندسازی AI
25. نتیجه‌گیری
26. لینک Repository

---

# 26. فیلم نهایی

```text
00:00 - 01:00
معرفی آزمایش و Repository

01:00 - 02:00
ساختار دو پوشه

02:00 - 03:30
اجرای نسخه اولیه و مشکل BundleOrder

03:30 - 05:00
Cash قبل از SOLID + Git diff

05:00 - 08:00
SRP / OCP / LSP / ISP / DIP

08:00 - 09:30
OpenCode Skill + Plan

09:30 - 12:00
معماری Refactorشده

12:00 - 13:00
Cash بعد از SOLID

13:00 - 14:00
Tests + مقایسه Git diff

14:00 - 15:00
نحوه استفاده از AI + نتیجه‌گیری
```

دستورهای آماده برای فیلم:

```powershell
cd .\01-Principles-OOD-Without
py -m store.main
```

```powershell
cd ..\02-Principles-OOD-Applied
py -m store.main
py -m unittest discover -s tests -v
```

```powershell
cd ..
git diff --stat solid-before-cash..solid-with-cash
```

---

# 27. چک نهایی

```text
README فارسی                       OK
گزارش PDF نیست                    OK
GitHub Repository                 Public
01-Principles-OOD-Without         موجود
02-Principles-OOD-Applied         موجود
Cash نسخه اول                     موجود
Cash نسخه دوم                     موجود
SOLID Analysis                    کامل
SRP/OCP/LSP/ISP/DIP               هر پنج مورد
SKILL.md                          موجود
AGENTS.md                         موجود
REFACTORING_PLAN.md               موجود
Promptهای واقعی                   ثبت شده
AI Model/Provider                 ثبت شده
Tests                             Pass
Git History                       مرحله‌ای
Git Tags                          موجود
Kanban                            حذف شده
فیلم                              <= 15 دقیقه
```

مهم‌ترین ترتیب:

```text
Original
   |
   +---------------------------+
   |                           |
   v                           v
Version 01                  Version 02
   |                           |
Add Cash                    Analyze SOLID
   |                           |
Commit                        Skill
   |                           |
Record Diff                   Plan
                               |
                            Refactor
                               |
                            Test
                               |
                    COMMIT WITHOUT CASH
                               |
                          Tag checkpoint
                               |
                           Add Cash
                               |
                            Test
                               |
                            Commit
                               |
                        Compare Diffs
```

---

## کاربر

[تصویر پیوست‌شده از OpenCode که دو گزینه درباره BundleOrder نشان می‌داد: «Substitution wins» و «Baseline numbers win».]

---

## دستیار

اینجا **گزینه ۱ را انتخاب کن**:

> **1. Substitution wins (Recommended)**

یعنی Enter را روی همین گزینه بزن.

دلیلش این است که خروجی قبلی Order 103 عملاً حاصل همان باگ طراحی `BundleOrder` بوده. در نسخه اولیه، `BundleOrder` سفارش‌های داخلی دارد ولی `items` خودش خالی است؛ در نتیجه `subtotal` آن صفر دیده می‌شود و سیستم فقط `$5` هزینه shipping می‌گیرد. اگر بخواهیم همان `$5` را صرفاً برای حفظ خروجی قبلی نگه داریم، مجبور می‌شویم special-caseهایی مثل `isinstance(order, BundleOrder)` را نگه داریم و عملاً **نقض LSP را اصلاح نکرده‌ایم**.

با گزینه ۱، `BundleOrder` واقعاً مثل یک `Order` رفتار می‌کند:

```text
BundleOrder
    ↓
items = flattened child-order items
    ↓
subtotal = $1,194.99
    ↓
VIP discount = -$239.00
    ↓
shipping = $0.00
    ↓
total = $955.99
```

پس تغییر خروجی Order 103 در این مورد **Regression ناخواسته نیست**؛ اصلاح یک رفتار اشتباه ناشی از طراحی قبلی است.

در گزارشت هم این نکته خیلی ارزشمند است. می‌توانی بنویسی:

```markdown
### تغییر رفتار BundleOrder پس از اصلاح LSP

در نسخه اولیه، `BundleOrder` با وجود ارث‌بری از `Order`، لیست
`items` خالی داشت. در نتیجه مقادیر `subtotal` و `item_count`
برای سفارش Bundle به‌درستی محاسبه نمی‌شدند و برای جلوگیری از
خطا نیز یک شرط ویژه بر اساس نوع `BundleOrder` در سرویس سفارش
وجود داشت.

در فرآیند Refactoring تصمیم گرفته شد سازگاری جانشینی
(Substitutability) نسبت به حفظ خروجی عددی ناشی از رفتار معیوب
نسخه اولیه اولویت داشته باشد.

پس از اصلاح، آیتم‌های سفارش‌های داخلی Bundle در قرارداد
`Order.items` منعکس می‌شوند. بنابراین Order 103 به‌جای مبلغ
غیرواقعی 5 دلار، بر اساس محتویات واقعی Bundle قیمت‌گذاری می‌شود.

این تغییر یک تغییر عمدی در رفتار است و ناشی از اصلاح نقض LSP
است، نه تغییر ناخواسته در منطق کسب‌وکار.
```

یک نکته مهم هم برای ادامه OpenCode: **اجازه بده Order 101 هم داخل Bundle 103 دوباره در demo نمایش/پردازش شود**؛ پیامی که می‌گوید Alice «visibly charged twice» مربوط به داده‌های Demo موجود است، نه Refactor تو. فعلاً demo data را دست نزن، چون Agent هم درست اشاره کرده که این ویژگی داده‌های اولیه پروژه است.

پس الان:

```text
→ 1. Substitution wins (Recommended)
```

و **Enter**.

---

## کاربر

نقش opencode
اصن چی بود؟ چرا فایل ها تغییر نکردن؟ و خب فایل های درستی که solid رو رعایت میکنن هم بده

---

## دستیار

بله؛ اینجا یک سوءتفاهم مهم پیش آمده بود. **OpenCode قرار نبود فقط درباره SOLID با تو حرف بزند؛ قرار است در مرحله Build واقعاً فایل‌های پروژه را Refactor کند.** دلیل اینکه تا الان فایل‌ها تغییر نکرده‌اند این است که ما عمداً در مرحله **Plan** بودیم و حتی در Prompt هم گفته بودیم `Do not edit source files yet`.

خود آزمایش هم OpenCode را یک **AI Coding Agent** معرفی می‌کند که باید پروژه را تحلیل کند، تغییرات را برنامه‌ریزی کند و بعد از تأیید توسعه‌دهنده آن‌ها را اعمال کند؛ نه اینکه فقط کد نهایی از AI بگیری.

## پس OpenCode دقیقاً چه نقشی دارد؟

```text
کد خراب اولیه
      ↓
OpenCode / Plan
      ↓
تحلیل SOLID
      ↓
پیشنهاد Refactoring
      ↓
تو بررسی و اصلاح می‌کنی
      ↓
OpenCode / Build
      ↓
واقعاً فایل‌ها را تغییر می‌دهد
      ↓
تو Diff و Test را بررسی می‌کنی
```

### چرا فایل‌ها تغییر نکردند؟

پیام OpenCode هنوز یک **تصمیم معماری** از تو می‌خواست. تا زمانی که Agent روی Plan باشد، قرار نیست فایل‌ها واقعاً تغییر کنند.

در OpenCode با `Tab` از Plan به Build برو.

### Promptی که در Build باید بدهی

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

بعدش OpenCode باید کارهایی مثل این انجام دهد:

```text
Edit models.py
Create contracts.py
Create validation.py
Create shipping.py
Modify payment.py
Modify pricing.py
Modify notification.py
Modify storage.py
Create receipt.py
Modify order_service.py
Modify main.py
Create tests/test_store.py
```

اگر برای permission پرسید، اجازه بده.

### فایل‌های SOLID درست

یک نسخه کامل و تست‌شده ساخته شد:

[دانلود نسخه کامل و تست‌شده SOLID](sandbox:/mnt/data/solid-solution.zip)

داخل ZIP:

```text
solid-solution/
│
├── 02-Principles-OOD-Applied/
│   └── نسخه SOLID بدون Cash
│
├── after-solid-cash/
│   └── فایل لازم برای مرحله Cash بعدی
│
└── 02-Principles-OOD-Applied-WITH-CASH/
    └── نسخه نهایی SOLID + Cash
```

فعلاً باید از:

```text
02-Principles-OOD-Applied
```

استفاده شود و پوشه `WITH-CASH` فعلاً وارد پروژه نشود.

معماری نسخه SOLID:

```text
02-Principles-OOD-Applied
│
├── REFACTORING_PLAN.md
│
├── store
│   ├── __init__.py
│   ├── models.py
│   ├── contracts.py
│   ├── validation.py
│   ├── shipping.py
│   ├── pricing.py
│   ├── payment.py
│   ├── notification.py
│   ├── storage.py
│   ├── receipt.py
│   ├── order_service.py
│   └── main.py
│
└── tests
    └── test_store.py
```

### `models.py` → LSP

نسخه اصلاح‌شده:

```python
class BundleOrder(Order):
    def __init__(self, id, customer, orders):
        flattened_items = [
            item
            for child_order in orders
            for item in child_order.items
        ]

        super().__init__(
            id=id,
            customer=customer,
            items=flattened_items,
        )

        self.orders = orders
```

### `contracts.py` → DIP + ISP

```text
OrderValidator
PricingService
ShippingService
PaymentMethod
PaymentService
OrderRepository
Notifier
ReceiptPrinter
```

### `payment.py` → OCP

```python
class PaymentProcessor(PaymentService):
    def __init__(self, methods):
        self._methods = {
            method.key: method
            for method in methods
        }

    def process(self, order, amount):
        method = self._methods.get(order.payment_method)

        if method is None:
            raise ValueError(...)

        return method.pay(order, amount)
```

### `pricing.py` → OCP

```text
VipDiscountRule
BulkDiscountRule
WelcomeCouponDiscountRule
RuleBasedDiscountCalculator
```

### `notification.py` → ISP

```text
Notifier
EmailNotifier
SmsNotifier
PushNotifier
```

### `order_service.py` → SRP + DIP

```python
class OrderService:
    def __init__(
        self,
        validator,
        pricing,
        shipping,
        payment,
        repository,
        notifiers,
        receipt_printer,
    ):
        ...
```

Concrete classها در `main.py` ساخته می‌شوند؛ یعنی Composition Root.

### تست نسخه SOLID

```powershell
cd .\02-Principles-OOD-Applied
py -m store.main
py -m unittest discover -s tests -v
```

Bundle باید:

```text
Subtotal $1194.99
Discount -$239.00
Shipping $0.00
TOTAL $955.99
```

داشته باشد.

بعد:

```powershell
cd ..
git status
git diff -- .\02-Principles-OOD-Applied
```

و Commit:

```powershell
git add .\02-Principles-OOD-Applied
git commit -m "refactor: apply SOLID principles to second version"
git push

git tag solid-before-cash
git push origin solid-before-cash
```

**اینجا توقف کن. هنوز Cash را اضافه نکن.**

---

## کاربر

```text
test_bulk_discount_when_not_vip (test_pricing.DiscountPrecedenceTests) ... ok
test_coupon_discount_when_not_vip_and_below_bulk (test_pricing.DiscountPrecedenceTests) ... ok
test_default_rules_match_baseline_precedence (test_pricing.DiscountPrecedenceTests) ... ok
test_discount_is_rounded_to_cents (test_pricing.DiscountPrecedenceTests) ... ok
test_first_match_wins_is_caller_controlled (test_pricing.DiscountPrecedenceTests) ... ok
test_no_rule_applies_returns_zero (test_pricing.DiscountPrecedenceTests) ... ok
test_only_one_discount_is_ever_applied (test_pricing.DiscountPrecedenceTests) ... ok
test_vip_discount_wins_over_bulk_and_coupon (test_pricing.DiscountPrecedenceTests) ... ok
test_bulk_rule_threshold_is_inclusive_at_ten (test_pricing.RuleUnitTests) ... ok
test_coupon_rule_requires_exact_code (test_pricing.RuleUnitTests) ... ok
test_load_missing_returns_none (test_storage.MySqlDatabaseTests) ... ok
test_save_same_id_replaces_entry (test_storage.MySqlDatabaseTests) ... ok
test_save_then_load_roundtrip (test_storage.MySqlDatabaseTests) ... ok
test_empty_bundle_rejected_like_empty_order (test_validation.DefaultOrderValidatorTests) ... ok
test_empty_items_rejected (test_validation.DefaultOrderValidatorTests) ... ok
test_missing_payment_method_rejected (test_validation.DefaultOrderValidatorTests) ... ok
test_populated_bundle_validates_as_plain_order (test_validation.DefaultOrderValidatorTests) ... ok
test_valid_order_passes (test_validation.DefaultOrderValidatorTests) ... ok

======================================================================
FAIL: test_full_demo_output_matches_expected (test_golden_demo.GoldenDemoTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Haj Ali\Desktop\HajAli\University\SE Az\2-OOD\SELab-Exp2-SOLID-OpenCode\02-Principles-OOD-Applied\tests\test_golden_demo.py", line 49, in test_full_demo_output_matches_expected
    self.assertEqual(result.stdout.replace("\r\n", "\n"), EXPECTED_OUTPUT)
AssertionError: '>>> [1017 chars].99\n\n>>> Checkout a cash order\n[payment] Ca[337 chars]00\n' != '>>> [1017 chars].99\n'
Diff is 1448 characters long. Set self.maxDiff to None to see it.

----------------------------------------------------------------------
Ran 40 tests in 0.085s

FAILED (failures=1)
```

---

## دستیار

این خطا در واقع خیلی خوب مشخص می‌کند مشکل کجاست: **Refactor تقریباً درست انجام شده** و از ۴۰ تست، ۳۹ تا پاس شده‌اند. تنها تست `GoldenDemoTests` به این دلیل fail شده که نسخه‌ی فعلی `02-Principles-OOD-Applied` علاوه بر خروجی مورد انتظار، یک **Cash Order** هم اجرا می‌کند:

```text
>>> Checkout a cash order
[payment] Cash ...
```

در حالی که در مرحله‌ای که الان هستی، **نسخه SOLID باید هنوز Cash نداشته باشد**.

پس **Golden Test را فعلاً تغییر نده. Cash را از نسخه فعلی بردار.**

### کاری که الان باید انجام بدهی

در:

```text
02-Principles-OOD-Applied\store\main.py
```

هر قسمتی که Cash Order را ساخته حذف کن. احتمالاً چیزی شبیه این داری:

```python
cash_order = Order(
    id=104,
    customer=regular,
    payment_method="cash",
    items=[
        OrderItem(5, "Notebook", 15.00, 2)
    ],
)
```

و احتمالاً در `return` هم اضافه شده:

```python
return laptop, books, bundle, cash_order
```

آن را برگردان به:

```python
return laptop, books, bundle
```

و اگر در `main()` داری:

```python
laptop, books, bundle, cash_order = build_demo_orders()
```

برگردان به:

```python
laptop, books, bundle = build_demo_orders()
```

و این بخش را کامل حذف کن:

```python
print("\n>>> Checkout a cash order")
service.process_order(cash_order)
```

### Cash را از Composition Root هم فعلاً بردار

اگر این import را داری:

```python
from store.cash_payment import CashPayment
```

حذفش کن.

اگر PaymentProcessor این‌طور شده:

```python
payment_processor = PaymentProcessor(
    [
        CreditCardPayment(),
        PayPalPayment(),
        BitcoinPayment(),
        CashPayment(),
    ]
)
```

در این مرحله باید باشد:

```python
payment_processor = PaymentProcessor(
    [
        CreditCardPayment(),
        PayPalPayment(),
        BitcoinPayment(),
    ]
)
```

اگر فایل:

```text
store\cash_payment.py
```

داری، فعلاً هم حذفش کن:

```powershell
Remove-Item .\02-Principles-OOD-Applied\store\cash_payment.py
```

و اگر تست مستقلی مثل `test_cash_payment` داری، فعلاً از تست‌های نسخه قبل از Cash حذف کن.

هدف checkpoint:

```text
SOLID = YES
Cash  = NO
```

### دوباره تست کن

```powershell
cd .\02-Principles-OOD-Applied
py -m unittest discover -s tests -v
```

بعد:

```powershell
py -m store.main
```

Order 103 باید همچنان مقدار اصلاح‌شده Bundle را داشته باشد:

```text
Subtotal $1194.99
Discount -$239.00
Shipping $0.00
TOTAL $955.99
```

بعد از Pass شدن همه تست‌ها:

```powershell
cd ..
git status
git diff -- .\02-Principles-OOD-Applied
```

و:

```powershell
git add .\02-Principles-OOD-Applied
git commit -m "refactor: apply SOLID principles to second version"
git push

git tag solid-before-cash
git push origin solid-before-cash
```

بعد از این Commit تازه Cash را برمی‌گردانی، ولی این بار به‌صورت Strategy.

این failure هم یک نمونه خیلی خوب برای گزارش است:

> OpenCode قابلیت پرداخت نقدی را پیش از ثبت checkpoint نسخه Refactorشده وارد نسخه دوم کرده بود. با توجه به طراحی آزمایش، این تغییر رد شد تا ابتدا نسخه SOLID بدون قابلیت جدید Commit شود و امکان مقایسه میزان تغییرات لازم برای افزودن Cash قبل و بعد از Refactoring حفظ شود.

---

## کاربر

```python
from store.models import BundleOrder, Customer, Order, OrderItemffrom store.notification import EmailNotifier, SmsNotifier
from store.order_service import OrderService
from store.payment import (
    BitcoinPayment,
    CashPayment,
    CreditCardPayment,
    PayPalPayment,
    PaymentProcessor,
)
from store.pricing import (
    BulkDiscountRule,
    RuleBasedDiscountCalculator,
    VipDiscountRule,
    WelcomeCouponDiscountRule,
)
from store.receipt import ConsoleReceiptPrinter
from store.shipping import StandardShippingService
from store.storage import MySqlDatabase
from store.validation import DefaultOrderValidator


def build_demo_orders():
    vip = Customer(
        id=1, name="Alice", email="alice@example.com",
        phone="555-0100", is_vip=True, credit_card="4111 1111 1111 1111",
    )
    regular = Customer(
        id=2, name="Bob", email="bob@example.com", phone="555-0199",
    )

    laptop = Order(
        id=101, customer=vip, payment_method="credit_card",
        items=[OrderItem(1, "Laptop", 999.99, 1),
               OrderItem(2, "Mouse", 25.00, 1)],
    )

    books = Order(
        id=102, customer=regular, payment_method="paypal",
        items=[OrderItem(3, "Clean Code", 45.00, 2),
               OrderItem(4, "Pragmatic Programmer", 40.00, 2)],
    )

    bundle = BundleOrder(id=103, customer=vip, orders=[laptop, books])
    bundle.payment_method = "credit_card"
    return laptop, books, bundle


def build_order_service() -> OrderService:
    return OrderService(
        validator=DefaultOrderValidator(),
        pricing=RuleBasedDiscountCalculator([
            VipDiscountRule(),
            BulkDiscountRule(),
            WelcomeCouponDiscountRule(),
        ]),
        shipping=StandardShippingService(),
        payment=PaymentProcessor([
            CreditCardPayment(),
            PayPalPayment(),
            BitcoinPayment(),
            CashPayment(),
        ]),
        repository=MySqlDatabase(),
        notifiers=[EmailNotifier(), SmsNotifier()],
        receipt_printer=ConsoleReceiptPrinter(),
    )


def main() -> None:
    service = build_order_service()
]
    )
    service = Ord, cash_ordererService()
]
    )
    service = OrderService()

     
    service = OrderService()    service.process_order(bundle)
    service.process_order(bundle)s")
    service.process_order(bundle)


if __name__ == "__main__":
    main()
```

---

## دستیار

بله، `main.py`ای که الان فرستادی **خراب شده و چند تکه کد به‌صورت تصادفی روی هم افتاده‌اند**. مشکل اصلی فقط Cash نیست؛ انتهای فایل از نظر Syntax هم خراب است.

الان که در مرحله **SOLID Refactoring قبل از Cash** هستی، کل محتوای `02-Principles-OOD-Applied\store\main.py` را پاک کن و دقیقاً این را جایگزینش کن:

```python
from store.models import BundleOrder, Customer, Order, OrderItem
from store.notification import EmailNotifier, SmsNotifier
from store.order_service import OrderService
from store.payment import (
    BitcoinPayment,
    CreditCardPayment,
    PayPalPayment,
    PaymentProcessor,
)
from store.pricing import (
    BulkDiscountRule,
    RuleBasedDiscountCalculator,
    VipDiscountRule,
    WelcomeCouponDiscountRule,
)
from store.receipt import ConsoleReceiptPrinter
from store.shipping import StandardShippingService
from store.storage import MySqlDatabase
from store.validation import DefaultOrderValidator


def build_demo_orders():
    vip = Customer(
        id=1,
        name="Alice",
        email="alice@example.com",
        phone="555-0100",
        is_vip=True,
        credit_card="4111 1111 1111 1111",
    )

    regular = Customer(
        id=2,
        name="Bob",
        email="bob@example.com",
        phone="555-0199",
    )

    laptop = Order(
        id=101,
        customer=vip,
        payment_method="credit_card",
        items=[
            OrderItem(1, "Laptop", 999.99, 1),
            OrderItem(2, "Mouse", 25.00, 1),
        ],
    )

    books = Order(
        id=102,
        customer=regular,
        payment_method="paypal",
        items=[
            OrderItem(3, "Clean Code", 45.00, 2),
            OrderItem(4, "Pragmatic Programmer", 40.00, 2),
        ],
    )

    bundle = BundleOrder(
        id=103,
        customer=vip,
        orders=[laptop, books],
    )
    bundle.payment_method = "credit_card"

    return laptop, books, bundle


def build_order_service() -> OrderService:
    pricing = RuleBasedDiscountCalculator(
        [
            VipDiscountRule(),
            BulkDiscountRule(),
            WelcomeCouponDiscountRule(),
        ]
    )

    payment = PaymentProcessor(
        [
            CreditCardPayment(),
            PayPalPayment(),
            BitcoinPayment(),
        ]
    )

    return OrderService(
        validator=DefaultOrderValidator(),
        pricing=pricing,
        shipping=StandardShippingService(),
        payment=payment,
        repository=MySqlDatabase(),
        notifiers=[
            EmailNotifier(),
            SmsNotifier(),
        ],
        receipt_printer=ConsoleReceiptPrinter(),
    )


def main() -> None:
    service = build_order_service()

    laptop, books, bundle = build_demo_orders()

    print(">>> Checkout a simple order")
    service.process_order(laptop)

    print("\n>>> Checkout a bundle of two orders")
    service.process_order(bundle)


if __name__ == "__main__":
    main()
```

### چه چیزهایی از فایل خراب اصلاح شد؟

اولین خط:

```python
from store.models import BundleOrder, Customer, Order, OrderItemffrom store.notification ...
```

به دو import صحیح تبدیل شد:

```python
from store.models import BundleOrder, Customer, Order, OrderItem
from store.notification import EmailNotifier, SmsNotifier
```

همچنین `CashPayment` و `CashPayment()` فعلاً حذف شدند چون checkpoint فعلی باید قبل از Cash باشد.

بخش انتهای فایل خراب هم کامل حذف شد و `main()` صحیح فقط service را می‌سازد و laptop و bundle را پردازش می‌کند.

### حالا در PowerShell

```powershell
cd .\02-Principles-OOD-Applied
py -m store.main
py -m unittest discover -s tests -v
```

اگر هنوز Golden Test fail شد، Golden Test را تغییر نده و اختلاف جدید را بررسی کن.

برای پیدا کردن Cash در کد:

```powershell
Get-ChildItem .\store -Recurse -Filter *.py |
    Select-String "CashPayment"
```

و در تست‌ها:

```powershell
Get-ChildItem .\tests -Recurse -Filter *.py |
    Select-String "cash"
```

هدف:

```text
02-Principles-OOD-Applied

SOLID refactoring    ✅
Bundle LSP fix       ✅
Payment Strategy     ✅
Discount Rules       ✅
Notifier split       ✅
Dependency Injection ✅
Regression Tests     ✅

Cash Payment         ❌ فعلاً نه
```

بعد از پاس شدن همه تست‌ها:

```powershell
cd ..

git add .\02-Principles-OOD-Applied

git commit -m "refactor: apply SOLID principles to second version"

git push
```

و:

```powershell
git tag solid-before-cash
git push origin solid-before-cash
```

---

## کاربر

خب حالا readme گذارش کامل رو بهم بده. و سایر readme های مورد نیاز. و همچنین بگو دیگه چیا نیازه که پر بشن اون ها رو هم انجام ده. خروجی پروژه رو هم اپلود کردم

> فایل پروژه‌ی آپلودشده: `SELab-Exp2-SOLID-OpenCode.zip`

---

## دستیار

آره. پروژه‌ای که آپلود کردی را بررسی کردم و بر اساس **کد واقعی فعلی پروژه**، نه یک قالب فرضی، گزارش را کامل کردم. طبق صورت آزمایش، گزارش نهایی باید مطالب تمام گام‌ها را به‌ترتیب در README داشته باشد و فرایند اصلی شامل Cash روی نسخه اولیه، Refactoring، Cash مجدد و مقایسه دو حالت است. همچنین گزارش باید فارسی باشد و نباید به‌صورت PDF تحویل شود.

یک نکته مهم را هم در خود پروژه اصلاح کردم: نسخه نهایی `02-Principles-OOD-Applied` دوباره Cash را به‌صورت Strategy دارد و در Composition Root ثبت شده، بنابراین **نسخه نهایی واقعاً Cash را اجرا می‌کند**. Golden Test را هم متناسب با خروجی نهایی به‌روزرسانی کردم. بعد از این تغییرات کل تست‌ها را اجرا کردم و نتیجه نهایی **40 تست، همگی Pass، `OK`** شد.

فایل‌های آماده این‌ها هستند:

- [دانلود پروژه کامل نهایی و اصلاح‌شده](sandbox:/mnt/data/SELab-Exp2-SOLID-OpenCode-final.zip) — پیشنهاد می‌کنم همین نسخه را با پروژه فعلی‌ات مقایسه/جایگزین کنی و سپس Push کنی.
- [README نهایی گزارش فارسی](sandbox:/mnt/data/SELab-Exp2-README-FINAL.md) — گزارش کامل شامل هدف، مراحل، Cash قبل از SOLID، تحلیل پنج اصل، Skill، Plan، تصمیم‌های انسانی، Refactoring، Cash بعد از SOLID، مقایسه، تست‌ها، ارزیابی OpenCode و نتیجه‌گیری.
- [PROMPTS.md نهایی](sandbox:/mnt/data/SELab-Exp2-PROMPTS-FINAL.md) — پرامپت‌های اصلی OpenCode، تصمیم `Substitution wins`، Build، Cash بعد از SOLID و مستندسازی استفاده از ChatGPT.
- [چک‌لیست نهایی تحویل](sandbox:/mnt/data/SELab-Exp2-FINAL-CHECKLIST.md) — دقیقاً مشخص کرده چه چیزهایی حاضر است و چه مواردی فقط خودت می‌توانی تکمیل کنی.
- داخل ZIP همچنین `01-Principles-OOD-Without/README.md` و `02-Principles-OOD-Applied/README.md` را اضافه کردم؛ این دو الزام مستقل صورت سؤال نیستند، اما برای توضیح دو نسخه خیلی مفیدند. علاوه بر آن `docs/AI_USAGE.md`، `docs/TEST_REPORT.md`، `docs/VIDEO_SCRIPT.md`، نسخه اصلاح‌شده `REFACTORING_PLAN.md`، `AGENTS.md` و Skill هم وجود دارند. فایل‌های `__pycache__` و `.pyc` را هم از بسته نهایی حذف و `.gitignore` را برای Python/Windows اصلاح کردم.

در README نهایی تحلیل واقعی پروژه آمده است. مثلاً برای SRP توضیح داده شده که `OrderService` اولیه هم‌زمان validation، pricing، shipping، payment، persistence، notification و receipt را انجام می‌داد. برای OCP، تفاوت بین `elif cash` در نسخه اولیه و `CashPayment` Strategy در نسخه SOLID توضیح داده شده. برای LSP هم تغییر واقعی Order 103 از **5.00 دلار** به **955.99 دلار** با دلیل کامل مستند شده است. تصمیمی که در OpenCode گرفتی، یعنی **`Substitution wins`**، نیز به‌عنوان یک تصمیم انسانی مهم در گزارش ثبت شده است.

بخش OpenCode هم به‌صورت جدی نوشته شده، چون صورت آزمایش صرفاً استفاده از Agent را نمی‌خواهد؛ می‌خواهد خروجی Agent را بررسی و در صورت نیاز اصلاح یا رد کنی و فرایند تعامل را مستند کنی. همچنین Plan باید بررسی شود و Build بعد از آن برای اعمال اصلاحات استفاده شود. من موارد واقعی‌ای که در روند تو اتفاق افتاد هم ثبت کردم: سؤال OpenCode درباره Bundle، انتخاب Substitution، خراب‌شدن یک نسخه میانی `main.py`، ورود زودهنگام Cash و failure تست Golden، و اصلاح این موارد توسط خودت.

تنها چیزهایی که **عمداً نتوانستم از خودم پر کنم** این‌ها هستند: شماره دانشجویی‌ات؛ نام دقیق مدل و Providerای که واقعاً داخل OpenCode استفاده کردی و نحوه اتصال آن؛ هر Prompt دیگری که واقعاً در OpenCode فرستادی ولی در گفتگو/ZIP اثری از آن نداریم؛ و Git commit hash/Tagهای واقعی، چون ZIP ارسالی پوشه `.git` نداشت. لینک فیلم نهایی هم طبیعتاً بعد از ضبط مشخص می‌شود. این‌ها داخل README و `FINAL_CHECKLIST.md` با عبارت مشخص علامت‌گذاری شده‌اند تا چیزی از قلم نیفتد.

در بخش AI، استفاده از **ChatGPT / GPT-5.6 Sol** را هم مستند کردم، چون دستورالعمل آزمایشگاه می‌خواهد استفاده از ابزارهای AI شفاف گزارش شود و فقط نوشتن «از OpenCode استفاده شد» کافی نیست. مسئولیت نهایی تحلیل و صحت تصمیم‌ها نیز طبق صورت آزمایش با دانشجو است.

برای مرحله آخر روی ویندوز، بعد از جایگزینی فایل‌ها فقط از Root پروژه این‌ها را بررسی کن:

```powershell
git status
```

بعد:

```powershell
cd .\02-Principles-OOD-Applied
py -B -m unittest discover -s tests -v
```

باید انتهای خروجی:

```text
Ran 40 tests

OK
```

باشد. سپس:

```powershell
py -B -m store.main
```

و باید سه Demo ببینی: Order 101 با `819.99` دلار، Bundle 103 با `955.99` دلار، و Cash Order 104 با `35.00` دلار.

بعد به Root برگرد:

```powershell
cd ..
git add .
git commit -m "docs: complete experiment 2 report and final verification"
git push
```

فقط قبل از این Commit مطمئن شو که در Git history خودت واقعاً یک Commit از **نسخه SOLID قبل از Cash** داری؛ چون ZIP شامل `.git` نبود و من نمی‌توانستم این بخش را از روی فایل‌ها تأیید کنم. این checkpoint برای مقایسه خواسته‌شده در مسئله مهم است.

---

## کاربر

فایل markdown این چتمون را کامل بده بهم

---

## یادداشت پایان رونوشت

این فایل تا درخواست بالا، رونوشت گفت‌وگوی قابل‌مشاهده را نگه می‌دارد. ضمیمه‌های باینری (PDF/ZIP/تصویر) داخل فایل Markdown جاسازی نشده‌اند.
