# Ask user for their name
name = input("What is your name?\n")   #or put   ".strip().capitalize().title()"   ...on the end up here
#remove spaces on either end capitalize name ...dont need .capitalize() if using .title()
name = name.strip().capitalize().title()
# split the first and last name
first, last = name.split(" ")
# Greet user by name
print("Hello,", name)
# OR
print("Hello, " + name)
# OR f string / format
print(f"Hello, {name}")

# using first name ...type full name or it will error.
print(f"Hello, {first}")
