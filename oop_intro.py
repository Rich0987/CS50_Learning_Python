# def main():
#     name, city = get_student()         # as stated below name, city could just be student
#     print(f"{name} from {city}")       # print(f"{student[0]} from {student[1]}")
#
# def get_student():
#     name = input("Name: ")
#     city = input("City: ")
#     return (name, city)                 # tuple: return multiple values, 1 tuple with 2 things inside...
#                                         # can rename the tuple rather than listing out each value the tuple has
#                                         # eg name, city   would just be   student
# if __name__ == "__main__":
#     main()
#######################################################################
# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")
#                                                             #tuple values can not be changed even if you try:
#                                                             # if student[1] == "rich":
#                                                             #     student[2] = "middletown"
#                                                             # this wont change bear to middletown, tuple is immutable
#                                                             # use a list if you want to change it
# def get_student():
#     name = input("Name: ")
#     city = input("City: ")
#     return (name, city)
#
# if __name__ == "__main__":
#     main()
###############################################################
def main():
    student = get_student()
    if student ["name"] == "rich":
        student ["city"] = "middletown"                       # wrote rich and bear but middletown came out
    print(f"{student['name']} from {student['city']}")        # this wouldn't have happened with a tuple

def get_student():
    student = {}      #keys below will go in here
    student ["name"] = input("name: ")
    student ["city"] = input("city: ")
    return student

if __name__ == "__main__":
    main()


