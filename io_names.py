# names = []      # empty list
#
# for _ in range(3):
#     name = input("What is your name? ")
#     names.append(name)
#
# for name in sorted(names):
#     print(f"hello, {name}")             # here you can enter 3 names... but it isn't saved
#                                         # use open

name = input("What's your name? ")

file = open("names.txt", "a")   #this is where you want to store the data and w is to write / a to append
file.write(f"{name}\n")
file.close()

             # pythonic way would be get rid of file.close() and type "with open("names.txt", "a") as file:"...
