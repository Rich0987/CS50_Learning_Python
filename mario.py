def main():
    height_number = height_input()
    length_number = length_input()
    column(length_number)
    row(height_number)

def length_input():
    while True:
        n = int(input("What is length? "))
        if n > 0:
            break
    return n

def height_input():
    while True:
        n = int(input("What is height? "))
        if n > 0:
            break
    return n

def column(n):
    for height in range(n):
        print("#")

def row(n):
    for length in range(n):
        print("?", end="")

main()
