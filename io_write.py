# import csv
#
# name = input("What's your name? ")
# city = input("What city are you in? ")
#
# with open("write_name.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, city])

### Now with DictWriter

import csv

name = input("What's your name? ")
city = input("What city are you in? ")

with open("write_name.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "city"]) #need to add fieldname to inform dictwriter of the headers
    writer.writerow({"city":city, "name": name} )  #this can be switched around if using dictwriter