# Hillel Project - August 2023

## Before First Launch

### Setting up the Project with venv (Lessons 1-2 only)
1. `python3 -m venv env`
2. `. env/bin/activate`

### Setting up the Project with Pipenv (Lesson 3 onwards)
1. `pipenv install`
2. `pipenv shell`

## Task 1: Setup
- Install Python 3.10 or newer.
- Set up your preferred editor (e.g., VSCode, PyCharm).

## Task 2: Code Quality
- Prepare a Pull Request on GitHub. 
- Use the `code-quality` branch for this (needs to be created beforehand).
- Ensure GitHub Actions include checks for tools like `black`, `isort`, and either `flake8` or `ruff`.

[View Pull Request](https://github.com/marynalysenko/hillel_08_2023/pull/3)

## Task 3: Iterators, Generators, and Code Debugging
- Complete the examples discussed during class.
- Download the `rockyou` file.
- Create a variable named `results = []`.
- For each line in the file, check if the word "user" exists.
- Based on user input, decide if the line should be added to the `results`.
- After reading the entire file, the application should return both the `results` and the count of added lines.

[View Pull Request](https://github.com/marynalysenko/hillel_08_2023/pull/4)

## Task 4: Functions (lesson 5)
Complete all functions:
- show_players
- add_player
- remove_player

[View Pull Request](https://github.com/marynalysenko/hillel_08_2023/pull/6)

## Task 5: Decorators (lesson 6)
- Check the [code](https://github.com/parfeniukink/hillel_08_2023/blob/main/homeworks/decorators.md)
- The task of the "Reverse string" decorator is to create a decorator that, when applied to functions, reverses the output of the function if the output is a string. If the output is not a string, the decorator should return None.
- The task of the "Replace dict value" decorator is to create a decorator that takes a target key and an optional replacement value. When applied to functions that return dictionaries, the decorator should replace the value of the specified target key in the returned dictionary with the provided replacement value.

[View Pull Request](https://github.com/marynalysenko/hillel_08_2023/pull/7)

## Task 6: Context managers (lesson 7)
- Check the [code](https://github.com/parfeniukink/hillel_08_2023/blob/main/lesson_07/hw.md)
- Write a context manager that measures and logs the execution time of a code block inside it. Use the time module for timing and the logging module for logging.
- Test it with different pieces of code.

[View Pull Request](https://github.com/marynalysenko/hillel_08_2023/pull/9)

## Task 7: Dunder methods (lesson 9)
Create a class Price

class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

Acceptance criteria:
If I create 2 instances of a Price class I want to do operations between them:
-  add prices with same currency
-  do a subtraction of prices with same currency

*Additional: operations between prices with different currencies:
-  If price instances currencies are different I want to do a double conversion
USD is a middle currency
-  If right price is USD the regular conversation (not double) is happening
-  If prices currencies is the same conversion is not happening
-  Result currency after the operation is a currency of the price that is on the left or USD (for your decision)

[View Pull Request](https://github.com/marynalysenko/hillel_08_2023/pull/10)
