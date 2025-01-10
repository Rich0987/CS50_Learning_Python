# + plus
# - minus
# * multiply
# / divide
# % modulo (remainder)

# int and floats
# Nesting... does inside then outside
x = float(input("What's x?\n"))
y = float(input("What's y?\n"))

z = round(x + y, 2) # to 2 digits

print(f"{z:,}")   # Using the comma as a thousands separator: ...found under "string" doc
print(f"{z:.2f}")  # you only want 2 digits to print like line 12


