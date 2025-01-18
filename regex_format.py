import re

# name = input("What's your name? ").strip()
# if "," in name:
#     last,first = name.split(", ") #what is there is no space after the comma or they dor rich smed, jr
#     name = f"{first} {last}"                                          # can't use ? with split
# print(f"hello, {name}")

### next approach = import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)?", name) #capturing the .+ with (.+) and matches variable
if matches:                                                             #can add ? with re or * for multiple spaces
    last, first = matches.groups()    # the following 2 lines could just be...
    name = f"{first} {last}"          # name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")               # if last, first was split as: last = matches.group(1)
                                                                #   first = matches.group(2)

