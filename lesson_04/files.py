from pathlib import Path

THIS_FILE = Path(__file__).absolute()
ROOT_DIR = THIS_FILE.parent

# Example 5: Search for the word "user" in each line of the "rockyou.txt" file
file = open(ROOT_DIR / "rockyou.txt")
results: list[str] = []


# example 1
# lines: list[str]= file.readlines()

# for line in lines:
#    user_input = input(f"do you : {line}")
#    if user_input == "yes":
#        results.append(line)
#    else:
#        continue


# недолік в тому що проходячись построчно тримаємо в памяті весь
# список поки юзер не дойде до кінця


# example 2
def get_file_lines(filename: Path):
    file = open(filename)
    while True:
        line = file.readline()
        if not line:
            break
        yield line  # дозволяє зупиняти контекст виконання на цьому рядочку


for line in get_file_lines(ROOT_DIR / "rockyou.txt"):
    user_input = input(f"do you wanna add the line: {line}")
    if user_input == "yes":
        results.append(line)
    else:
        print(f"Line: {line} is added")
        continue
