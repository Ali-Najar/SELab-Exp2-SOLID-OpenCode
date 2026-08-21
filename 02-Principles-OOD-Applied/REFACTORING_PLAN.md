# Refactoring Plan — SOLID Checkout (checkpoint before cash)

## Approved decisions

1. **LSP / BundleOrder**: substitution wins — a bundle is priced by its flattened
   contents. Order 103 changed from the broken `$5.00` charge to real totals
   (subtotal $1,194.99, VIP −$239.00, shipping $0.00, total $955.99). All other
   receipts stay byte-identical to baseline. Demo data untouched.
2. **Storage naming**: keep `MySqlDatabase` with `save_order`/`load_order`;
   introduce `OrderRepository` contract around it.
3. **Discounts**: converted to an ordered first-match-wins rule list
   (VIP 20% > bulk ≥10 items 10% > WELCOME10 10%); exactly one discount ever
   applies, matching baseline precedence.
4. **Cash payment**: out of scope for this checkpoint; added only after this
   state is committed.

## Applied structure

- `store/contracts.py` — abstract contracts: `PaymentMethod`, `PaymentService`,
  `OrderValidator`, `ShippingService`, `Notifier`, `OrderRepository`,
  `ReceiptPrinter`.
- `store/payment.py` — one strategy per method (`CreditCardPayment`,
  `PayPalPayment`, `BitcoinPayment`) registered into `PaymentProcessor`; new
  methods plug in without editing the processor.
- `store/pricing.py` — discount rules + `RuleBasedDiscountCalculator`
  (default ruleset reproduces baseline precedence).
- `store/notification.py` — single-channel notifiers (`EmailNotifier`,
  `SmsNotifier`, `PushNotifier`); no implementation is forced to support
  channels it cannot perform.
- `store/validation.py`, `store/shipping.py`, `store/receipt.py` — extracted
  responsibilities; error messages, threshold ($100) and receipt layout are
  byte-compatible with baseline.
- `store/storage.py` — `MySqlDatabase` implements `OrderRepository`.
- `store/order_service.py` — orchestration only; all collaborators injected.
- `store/main.py` — composition root wiring concrete implementations.

## Provenance note

An earlier partial refactor of these files existed in the working tree before
this checkpoint (not produced by this session). It was kept ("repair &
converge") and corrected where it violated the approved decisions: restored
baseline receipt formatting, restored `MySqlDatabase` naming/methods, fixed
broken `main.py` wiring, added pricing default ruleset.

## Verification

From inside this folder:

```
python -B -m store.main
python -B -m unittest discover -s tests -v
```

38 regression tests cover models/bundle substitution, discount precedence,
payment strategies, notifier independence, repository roundtrip, validation,
end-to-end order flow, and a golden test of full demo output.
