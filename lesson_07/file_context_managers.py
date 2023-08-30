filename = "/Users/marinalysenko/Projects/HILLEL_08_2023/hillel_08_2023/lesson_07/names.txt"

with open(filename, mode="r") as file:
    lines = file.readlines()


class FileBase:
    def __init__(self, file: str) -> None:
        self.file: str = file

    def close(self):
        print(f"Closing file {self.file}")


class FileReader(FileBase):
    def readlines(self):
        print("Reading all lines from the file")

    def write(self):
        print("Readonly!!!")


class FileWriter(FileBase):
    def readlines(self):
        print("Only for writing")

    def write(self, data: str):
        print(f"Writing the {data}")


# Цей клас імітує роботу вбудованої функції open і дозволяє
# використовувати конструкцію with для роботи з файлами.
# Він визначає методи __enter__ та __exit__, які роблять його контекстним менеджером.
class open:
    # Клас, який імітує роботу вбудованої функції open
    def __init__(self, filename: str, mode: str) -> None:
        self._filename: str = filename
        self._mode: str = mode

    def __enter__(self):
        # Ініціалізація екземпляра FileReader або FileWriter залежно від режиму
        if self._mode == "r":
            self._file_mode_instance = FileReader(self._filename)
        elif self._mode == "w":
            self._file_mode_instance = FileWriter(self._filename)
        else:
            # Якщо режим невідомий, викликаємо виключення
            raise NotImplementedError

        return self._file_mode_instance

    def __exit__(self, *args, **kwargs):
        # Закриваємо файл після завершення роботи в контекстному блоку
        self._file_mode_instance.close()
