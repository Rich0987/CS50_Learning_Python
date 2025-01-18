# checking for errors
# validating correct user inputs eg. the city exists in my list...

class Student:
    def __init__(self, name, city):
        if not name:
            raise ValueError("Missing Name")     ### dont use sys.exit or other things use raise
        if city not in ["bear", "middletown", "hockessin", "odessa"]:
            raise ValueError("Invalid City")
        self.name = name
        self.city = city

def main():
    student = get_student()
    print(f"{student.name} from {student.city}")

def get_student():
    name = input("name: ")
    city = input("city: ")
    return Student(name, city)

if __name__ == "__main__":
    main()