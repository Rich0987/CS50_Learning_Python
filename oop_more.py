class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"{self.name} from {self.city}"

    #replace removed with below in class
    @classmethod
    def get(cls):
        name = input("name: ")
        city = input("city: ")
        return cls(name, city)

def main():
    student = Student.get()
    print(student)

                            #remove this                                # def get_student():
                                                                        #     name = input("name: ")
                                                                        #     city = input("city: ")
                                                                        #     return Student(name, city)

if __name__ == "__main__":
    main()