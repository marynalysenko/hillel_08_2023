from pathlib import Path

class FileReader:
    def readlines(self):
        print("Reading")

    def write(self):
        print("Readonly!!!")

class FileWriter:
    def readlines(self):
        print("Only for writing")

    def write(self, data: str):
        print(f"Writing the data {data}")

class FileContextManager:
    def __init__(self, filename: str, mode: str) -> None:
        self._filename = filename
        self._mode = mode
        self._file = None

    def __enter__(self):
        if self._mode == "r":
            self._file = FileReader()
        elif self._mode == "w":
            self._file = FileWriter()
        return self._file

    def __exit__(self, exc_type, exc_value, traceback):
        if self._file is not None:
            self._file = None

filename = "/Users/marinalysenko/Projects/HILLEL_08_2023/hillel_08_2023/lesson_07/names.txt"

with FileContextManager(filename, mode="r") as file:
    file.readlines()
