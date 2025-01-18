import re

#walrus format/operator :=

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), ?(.+)?", name):  #to assign something from right to left and...
    name = matches.group(2) + " " + matches.group(1)     #you want to ask an if or elif question
print(f"hello, {name}")