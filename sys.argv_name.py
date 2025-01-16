import sys
### add arguments/variables from commandline to be fed in as a list
### kinda like bash $1 $2 $3...?

# try:
#     print("hello, my name is", sys.argv[1])         #python3 sys.argv_name.py rich
#                                                 #hello, my name is rich
# except IndexError:
#     print("too few arguments")

#or

# if len(sys.argv) < 2:                 # 2 because 0 and 1... 0=script, 1=name/variable/input
#     sys.exit("Too few arguments")       # rather than print
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")       # rather than print
#
# print("Hello, my name is", sys.argv[1])   # rather than if, elif, else print... exit when there is an error


#iterate over multiple inputs/arguments
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)    #this will print 0 / sys.argv_name.py
                                        # so slice [1:] ...start at 1 and continue on
                                        # slice the end of a list... [1:-1]