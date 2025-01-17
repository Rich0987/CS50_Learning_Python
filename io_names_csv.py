# with open("names.csv") as file:
#     for line in file:
#         row = line.rstrip().split(", ")       # ", " comma and space as the delimiter
#         print(f"{row[0]} is in {row[1]}")
#
# or

# with open("names.csv") as file:
#     for line in sorted(file):           ### added sorted
#         name, city = line.rstrip().split(", ")       # ", " comma and space as the delimiter
#         print(f"{name} is in {city}")

# what if you want to sort my a specific variable... name or city or age

students = []

with open("names.csv") as file:
    for line in file:
        name, city = line.rstrip().split(", ")
        student = {}                ### create a dictionary
        student["name"] = name         # or student = {"name": name, "city": city}   ...turning 3 lines to 1
        student["city"] = city
        students.append(student)

def get_city(student):          # this is where the KEY is defined
    return student["city"]      # can change this to name or city to sort by or make a new function "def get_city()"

for student in sorted(students, key=get_city, reverse=True):               # key to sort by... name or city
    print(f"{student['name']} is in {student['city']}")           #single or double quotes worked



