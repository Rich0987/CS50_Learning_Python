def main():
    print_square(5)


def print_square(size):

    #for each row in square
    for i in range(size):

        #for each brick in row
        for j in range (size):   #bricks in column

            #print brick
            print("#", end="")   #bricks in row
        print() #this will print a line at the end of the loop


main()