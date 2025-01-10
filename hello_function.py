def main():                     # Hello world
    name = input("What is your name?\n")
    hello(name)                   # Hello Rich



def hello(to="world"):        # if no input world will print
    print("Hello,", to)       # To will move to the name variable


main()
hello()