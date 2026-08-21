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

class OrderValidator(ABC):
    @abstractmethod
    def validate(self, order) -> None:
        raise NotImplementedError

class ShippingService(ABC):
    @abstractmethod
    def calculate(self, order, subtotal: float) -> float:
        raise NotImplementedError

class Notifier(ABC):
    @abstractmethod
    def send(self, customer, message: str) -> None:
        raise NotImplementedError

class OrderRepository(ABC):
    @abstractmethod
    def save_order(self, order) -> None:
        raise NotImplementedError

    @abstractmethod
    def load_order(self, order_id: int):
        raise NotImplementedError

class ReceiptPrinter(ABC):
    @abstractmethod
    def print_receipt(
        self,
        order,
        subtotal,
        discount,
        shipping,
        total,
        receipt,
    ) -> None:
        raise NotImplementedError