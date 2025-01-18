# class Student:                     #classes create objects
#     ...                             # Capital S
#
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.city}")
#
# def get_student():
#     student = Student()
#     student.name = input("name: ")        #put inside of class the name and city attribute with .name .city
#     student.city = input("city: ")
#     return student
#
# if __name__ == "__main__":
#     main()
##################################

class Student:
    def __init__(self, name, city):                  # methods / functions
        self.name = name
        self.city = city

def main():
    student = get_student()
    print(f"{student.name} from {student.city}")

def get_student():
    name = input("name: ")
    city = input("city: ")
                                    #below lines could be replaced with "return Student(name, city)"
    student = Student(name, city)     #this way gives more error checking ability / checking validity better
    return student                      # ^constructing the object on the line above( student = Student(name, city)

if __name__ == "__main__":
    main()