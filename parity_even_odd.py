# % modulo
# remainder
from operator import truediv


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:        # if n divided by 2 has no remainder then it is even
        return True
    else:
        return False
                           #can just type "return n %2 == 0"
main()