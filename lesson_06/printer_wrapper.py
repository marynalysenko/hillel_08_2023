class Printer:
    def __init__(self, name: str, ip: str, port: int) -> None:
        self.name: str = name
        self.ip: str = ip
        self.port: int = port

    def __str__(self) -> str:
        return f"{self.name}@{self.ip}:{self.port}"


def open_connection(printer: Printer):
    print(f"Connection with {printer}...")


def close_connection(printer: Printer):
    print(f"Closing connection with {printer}")


def connect(printer: Printer):
    def wrapper(func):
        def inner(document: str):
            open_connection(printer)
            func(document)
            close_connection(printer)

        return inner

    return wrapper


hp_black = Printer(name="HP Black", ip="10.10.10.2", port=33145)
hp_white = Printer(name="HP White", ip="10.10.10.15", port=33145)


@connect(printer=hp_black)
def print_document(document: str):
    print(f"document: {document}")


print_document("Some text 2")
