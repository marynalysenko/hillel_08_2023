class MyContext:
    def __enter__(self):
        print("Entering the context" )

    def foo(self):
        print("I am foo")

with MyContext() as context        