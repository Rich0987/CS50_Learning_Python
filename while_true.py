#while True:
 #   number = int(input("what is number? "))
  #  if number > 0:
   #     break

#for _ in range(number):
 #   print("meow")


def main():
    number = get_number()
    chirp(number)

def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    return n

def chirp(n):
    for _ in range(n):
        print("chirp")

main()