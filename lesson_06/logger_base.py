from typing import Any, Callable


def logger(func: Callable, name: str):
    print(f"Running the {func.__name__}...")
    results: Any = func(name)
    if results:
        print(f"results: {results}")
    else:
        print("There is no results...")


def greeting(name: str) -> None:
    print(f"Hey,{name}!")


# greeting("John")

# декоратор - виконав функцію і додав ще якусь логіку (логи),
# треба для гарночитаємого коду
logger(greeting, name="John")
