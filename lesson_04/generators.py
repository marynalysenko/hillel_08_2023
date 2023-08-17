##########
#  example 1
##########

# def foo():
#    print("Hello, I am foo")


# def bar():
#    print("Hello, I am bar")

# print(foo)  #обєкт в пайтоні     <function foo at 0x100d7cc20>
# print(bar)  #обєкт в пайтоні     <function bar at 0x100df8fe0>

# foo.__call__()
# bar.__call__()

# bar(foo)

##########
#  example 2
##########

# def foo():
#    print("Hello, I am foo")


# def bar(function):
#    function.__call__()
#    #print("Hello, I am bar")

# bar(foo)

##########
#  example 3: генератори
##########


def foo():
    print("Hello, I am foo")


def bar(function):
    function.__call__()
    # print("Hello, I am bar")


def baz():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    # pass


a = bar(
    foo
)  # Hello, I am foo бо викликає foo() None (бо bar() нічого не повертає)
print(a)

print(foo)
print(baz)

print(foo())
print(baz())  # <generator object baz at 0x1010a4250>

gen = baz()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) #StopIteration
