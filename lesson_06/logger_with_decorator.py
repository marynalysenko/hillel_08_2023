from typing import Any, Callable


def logger(func: Callable) -> Callable:
    print(f"Running the {func.__name__}...")

    def inner(name: str):
        results: Any = func(name)
        if results:
            print(f"results: {results}")
        else:
            print("There is no results...")

    return inner  #


@logger  # @ - викликається на етапі ініціалізації програми
def greeting(name: str) -> None:
    print(f"Hey,{name}!")


greeting("John")

# декоратор - виконав функцію і додав ще якусь логіку (логи)
# logger(greeting)(name = 'John')
