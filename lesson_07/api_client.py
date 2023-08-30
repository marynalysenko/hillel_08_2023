# Імпортуємо необхідні модулі та функції
from typing import Generic, TypeVar

import requests


# Цей клас представляє простий API клієнт для взаємодії з веб-сервісами
class ApiClient:
    # Дозволені методи для клієнта (наразі тільки GET)
    ALLOWED_METHODS: list[str] = ["get"]

    def __init__(self, base_url: str) -> None:
        # Ініціалізація базової URL для API
        self.base_url: str = base_url

    def get_response(self, method: str, endpoint: str) -> dict:
        # Перевіряємо, чи дозволений обраний метод
        if method not in self.ALLOWED_METHODS:
            raise NotImplementedError(f"Method {method} is not implemented")

        # Отримуємо метод з модуля requests
        callback = getattr(requests, method)
        # Формуємо URL для запиту
        url = "".join([self.base_url, endpoint])
        # Здійснюємо запит
        response = callback(url)

        # Спроба конвертувати відповідь у JSON
        try:
            return response.json()
        except Exception:
            raise Exception("HTTP request Error")


# Тип для клієнта API
_ApiClient = TypeVar("_ApiClient", bound=ApiClient)


class ApiClientContext(Generic[_ApiClient]):
    # Контекстний менеджер для клієнта API

    def __init__(self, base_url: str) -> None:
        # Ініціалізація базової URL
        self._client: _ApiClient | None = None
        self._base_url: str = base_url

    # Метод викликається при вході в контекстний блок
    def __enter__(self) -> _ApiClient:
        self._client = ApiClient(base_url=self._base_url)
        return self._client

    # Метод викликається при виході з контекстного блоку
    def __exit__(self, exc_type, exc_value, tb):
        # Виведення інформації про виняток, якщо він стався
        print(f"⚠️ ⚠️ ⚠️ Unexpected client's response: {exc_value}")
        print("Closing the client")

    # Асинхронний контекстний менеджер (для асинхронних операцій)
    async def __aenter__(self) -> _ApiClient:
        self._client = ApiClient(base_url=self._base_url)
        return self._client

    async def __aexit__(self, exc_type, exc_value, tb):
        print(f"⚠️ ⚠️ ⚠️ Unexpected client's response: {exc_value}")
        print("Closing the client")


# Використання контекстного менеджера для отримання даних з API
with ApiClientContext(base_url="https://pokeapi.co/api/v2") as client:
    ditto_data = client.get_response(method="get", endpoint="/pokemon/dittoss")
    print(f"Fetched pokemon: {ditto_data['name']}")


# Асинхронна функція для отримання даних з API
async def foo():
    async with ApiClientContext(
        base_url="https://pokeapi.co/api/v2"
    ) as client:
        ditto_data = await client.get_response(
            method="get", endpoint="/pokemon/dittosы"
        )
        print(f"Fetched pokemon: {ditto_data['name']}")
