from pathlib import Path

THIS_FILE = Path(__file__).absolute
ROOT_DIR = Path(__file__).absolute().parent

###############################
# example 1 маленький файл

# file = open("lesson_03/text.txt") - вариант с указанием абсолютного пути
# file = open(ROOT_DIR / "text.txt")

# lines: list[str] = file.readlines()
# print(lines)

###############################

# example 2 великий файл
# file = open(ROOT_DIR / "rockyou.txt")
# lines: list[str] = file.readlines()
# print(len(lines))

###############################

# example 3: читаємо файл як строку

# file = open(ROOT_DIR / "rockyou.txt")

# text: str = file.read() #читає файл цілком і забиває в 1 файл
# print(len(text))

###############################

# example 4: читаємо файл щоб майже не використати памяті - читаємо почергово
file = open(ROOT_DIR / "rockyou.txt")
text: str = file.readline()  # читає 1 рядок
counter = 0
while True:
    try:
        word = file.readline()
        counter += 1
        print(word)
    except Exception:
        break

file.close()

print(counter)
