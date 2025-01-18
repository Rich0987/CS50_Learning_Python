class Student:
    def __init__(self, name, city):
        if not name:
            raise ValueError("Missing Name")
        if city not in ["bear", "middletown", "hockessin", "odessa"]:
            raise ValueError("Invalid City")
        self.name = name
        self.city = city

    def __str__(self):                     # add this to do print(student)    # dunder str
        return f"{self.name} from {self.city}"

def main():
    student = get_student()
    print(student)                 #prints <class '__main__.Student'> ... add __str__

def get_student():
    name = input("name: ")
    city = input("city: ")
    return Student(name, city)

if __name__ == "__main__":
    main()