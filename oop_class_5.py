### properties: @property  decorators... define properties

class Student:
    def __init__(self, name, city):
                                            #if not name:
                                            #   raise ValueError("Missing Name")
                                            #if city not in ["bear", "middletown", "hockessin", "odessa"]:
                                             #   raise ValueError("Invalid City")  # dont need because of getter/setter
        self.name = name      #name and city will now go through the setter functions
        self.city = city

    def __str__(self):
        return f"{self.name} from {self.city}"

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property                       # getter is always @property???
    def city(self):
        return self._city        #add underscore

    # Setter                   ### error checking will be kept in the Getter
    @city.setter
    def city(self, city):
        if city not in ["bear", "middletown", "hockessin", "odessa"]:
            raise ValueError("invalid house")
        self._city = city           # add underscore

def main():
    student = get_student()
    #               student.city = "elkton"    ### setter and getter should prevent this/ pulls error... remove it
    print(student)

def get_student():
    name = input("name: ")
    city = input("city: ")
    return Student(name, city)

if __name__ == "__main__":
    main()