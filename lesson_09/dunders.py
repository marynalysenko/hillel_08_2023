# __init__
# __new_
# __next__

class Team:
    def __init__(self, name) -> None:
        self.name = name
        self._team = M

    def __getitem__(self, key:str):
        if key not in self._team.keys():
            print("John is not there")
        else:
            print("-")    

school_12 = Team(name = "School 12")    
school_12["Jo"]