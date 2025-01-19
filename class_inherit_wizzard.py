#remove redundancy with inheritance since some classes share attributes... you dont want to copy and paste code

#student and professor are both wizards so how do we link them together:

class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("missing Name")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)                 # refers to the parent/super class so...
        self.house = house                     # if not name: raise ValueError don't have to be copy and pasted to each

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)                  # refers to the parent/super class also
        self.subject = subject

    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense against the Dark Arts")




