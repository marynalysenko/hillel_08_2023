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


def connect(func):
    def inner(printer, document):
        open_connection(printer)
        func(printer, document)
        close_connection(printer)

    return inner


@connect
def print_document(printer: Printer, document: str):
    print(f"document: {document}")


hp_black = Printer(name="HP Black", ip="10.10.10.2", port=33145)
hp_white = Printer(name="HP White", ip="10.10.10.15", port=33145)

print_document(hp_black, "Some text 2")
