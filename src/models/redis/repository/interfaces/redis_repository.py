from abc import ABC, classmethod


class RedisRepositoryInterface(ABC):

    @classmethod
    def insert(self, key: str, value: any) -> None:
        pass

    @classmethod
    def get_key(self, key: str) -> str:
        pass

    @classmethod
    def insert_hash(self, key: str, field: str, value: any) -> None:
        pass

    @classmethod
    def get_hash(self, key: str, field: str) -> any:
        pass

    @classmethod
    def insert_ex(self, key: str, value: any, ex: int) -> None:
        pass

    @classmethod
    def insert_hash_ex(self, key: str, field: str, value: any, ex: int) -> None:
        pass
