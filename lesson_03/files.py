from pathlib import Path 

THIS_FILE = Path(__file__).absolute
ROOT_DIR = Path(__file__).absolute().parent

#file = open("lesson_03/text.txt") - вариант с указанием абсолютного пути
file = open(ROOT_DIR / "text.txt")

lines: list[str] = file.readlines()
print(lines)
