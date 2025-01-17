import csv

students = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "city": row["city"]})   #dict reader uses header in csv file

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['city']}")

                #errors caused by spaces in the CSV file... works correctly