class Printer:
    def __init__(self, name: str, ip: str, port: int) -> None:
        self.name: str = name
        self.ip: str = ip
        self.port: int = port

    def __str__(self) -> str:
        return f"{self.name}@{self.ip}:{self.port}"


def open_connection(printer: Printer):
    print("Connection with Driver...")
    print(f"Connection with {printer}...")


def print_with_printer(printer: Printer, text: str):
    print(f"Printing '{text}' with {printer}...")


def close_connection(printer: Printer):
    print(f"Closing connection with {printer}...")


hp_black = Printer(name="HP Black", ip="10.10.10.2", port=33145)
hp_white = Printer(name="HP White", ip="10.10.10.15", port=33145)

open_connection(hp_black)
print_with_printer(hp_black, "Some Text")
close_connection(hp_black)
