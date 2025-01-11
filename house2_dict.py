students = {"ben": "delaware",
            "tom": "maryland",
            "bill": "maryland",
            "ken": "delaware",
            }
       #dict     key                   value/maryland
print(students["tom"]) # only prints state... cant put the state it will error

     #key        dictionary
for student in students:
    print(student, students[student], sep=", ")
           #key         keys value    