# https://refactoring.guru/uk/design-patterns/iterator
#Ітератор — це поведінковий патерн проектування, що дає змогу послідовно обходити елементи складових 
#об’єктів, не розкриваючи їхньої внутрішньої організації.

###############################

#example 1

#names = ["1","2"]
#for name in names:
#    print(f"{name=}")

###############################

#example 2 

#names: list[str] = ["1","2"]
#_names = iter(names)

#for name in names:
#    print(f"{name=}")

###############################

#example 3 

#names: list[str] = ["1","2"]
#_names = iter(names)

#while True:
#    try:
#        value = next(_names)
#        print(f"{value=}")
#    except StopIteration:
#        break    

###############################

#example 4
#names: list[str] = ["1","2"]
#_names = iter(names)
#print(next(_names)) 
#print(next(_names)) 

###############################

#example 5
#names: list[str] = ["1","2"]
#_names = iter(names)
#print(_names.__next__()) 
#print(_names.__next__()) 
#print(_names.__next__())  # StopIteration

###############################

#example 6

class Iterator:
    def __iter__(self):
        pass 
    def __next__(self):
        pass 
instances = Iterator()    

