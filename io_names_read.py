# with open("names.txt", "r") as file:
#     lines = file.readlines()
from lxml.doctestcompare import strip

# or below works too

# file = open("names.txt", "r")
# lines = file.readlines()
# file.close()
#
# for line in lines:
#     print("Hello,", line ,end="")

# OR the cleanest way...

# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,", line.strip())

# names = []
#
# with open("names.txt") as file:                   ### DONT NEED THE R... read is default
#     for line in file:
#         names.append(line.strip())         ### not appending to file but to names = []  placeholder
# for name in sorted(names):
#     print(f"hello, {name}")

# or sort the file 1st...

with open("names.txt") as file:
    for line in sorted(file):
        print("Hello," , line.strip())

