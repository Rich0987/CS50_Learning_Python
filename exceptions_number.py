#x = int(input("What's x? "))
#print(f"x is {x}")       ### i wrote "cat" and got a ValueError

# write the code with error handling
# try
# except
#try:
 #   x = int(input("What's x? "))
  #  print(f"x is {x}")                     #shouldnt have multiple things in the try except
#except ValueError:
 #   print("x is not an integer")

# OR

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
#
# print(f"x is {x}")     # got a name error putting in h ... still an int issue

# while True:
#     try:                                        # else
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")

# making it a function
def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

def get_int(prompt):                   # prompt can be any word you want
    while True:
        try:                                        # else
            x = int(input(prompt))
        except ValueError:
            print("x is not an integer")        # pass   ... type pass here instead and it will just ignore wrong input
        else:
            break
    return x

main()