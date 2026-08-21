from store.contracts import ReceiptPrinter


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
            print(f"  {item.name:20s} x{item.quantity}  ${item.line_total:.2f}")
        print(f"  Subtotal    ${subtotal:.2f}")
        print(f"  Discount   -${discount:.2f}")
        print(f"  Shipping    ${shipping:.2f}")
        print(f"  TOTAL       ${total:.2f}")
        print(f"  Payment     {receipt}")