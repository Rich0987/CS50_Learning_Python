import csv

students = []

with open("names.csv") as file:
    reader = csv.reader(file)       #reader in csv will do the work for you
    for row in reader:
        students.append({"name": row[0], "city": row[1]})
                        #changed between row and "name": name... still doesn't work right
                        #maybe a file issue cuts off at , even in quotes
                        #works... spaces in csv file caused issues
for student in sorted(students, key=lambda student: student["name"]):            #lambda for 1 time use
    print(f"{student['name']} is in {student['city']}")


