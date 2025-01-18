import re

email = input("What is your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")
#
# if username and domain.endswith(".edu"):   #2 separate booleans:   1-username    2-"." in domain   added parentheses
#     print("valid")
# else:
#     print("invalid")

### use re library as coming up with every scenario will create a lot of code
# .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m}   m repetitions
# {m,n} repetitions

# ^   matches the start of a string
# $   matches the end of the string

# []  set of characters
# [^] complementing the set... means you can not match any of the characters... nothing to do with ^ start
# eg [^@]   ...everything except an @ sign

# \w   ...means alphanumerical and underscore   can replace this [a-zA-Z0-9_]
# \W   ...opposite   / not a word character
# \d   decimal digit
# \D   not a decimal digit
# \s   white space character
# \S   not a white space character

# a|b  this or that
# (com|edu|net)  or combined as a group
# (?:...)  non-capturing group

# (\w+\.)?    ...can be there once or not at all

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE):  # r raw string dont interpret the \
    print("valid")                             # ^ and $ for exact match of the regex inbetween the ^ and $
else:
    print("invalid")

        # re.match, re.fullmatch