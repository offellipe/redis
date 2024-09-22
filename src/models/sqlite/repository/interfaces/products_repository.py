from abc import ABC, classmethod


class ProductsRepositoryInterface(ABC):

    @classmethod
    def find_product_by_name(self, product_name: str) -> tuple:
        pass

    @classmethod
    def insert_product(self, name: str, price: float, quantity: int) -> None:
        pass
