# ******    "Reverse string" decorator      ******#

from functools import wraps  # треба для сигнатури


def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        return None

    return wrapper


# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year() -> int:
    return 1957


# TEST OUPUT
print(get_university_name(), get_university_founding_year(), sep="\n")

# ******   "Replace dict value" decorator      ******#


def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, dict) and target_key in result:
                result[target_key] = replace_with
            return result

        return wrapper

    return decorator


# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
