class Student:
    def __init__(self, name, city, skill):      #added skill
        if not name:
            raise ValueError("Missing Name")
        if city not in ["bear", "middletown", "hockessin", "odessa"]:
            raise ValueError("Invalid City")
        self.name = name
        self.city = city
        self.skill = skill                      #added skill

    def __str__(self):
        return f"{self.name} from {self.city}"

    def charm(self):        ### now we create our own
        match self.skill:
            case "stag":
                return "horse emoji"
            case "otter":
                return "otter emoji"
            case "dog":
                return "dog emoji"
            case _:
                return "default emoji"

def main():
    student = get_student()
    print("Here's my skill!")
    print(student.charm())                       # calling attribute with student.charm()     !!!!!!



def get_student():
    name = input("name: ")
    city = input("city: ")
    skill = input("skill: ")                    #added skill
    return Student(name, city, skill)

if __name__ == "__main__":
    main()