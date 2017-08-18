"""Bonnie Gilsenan"""

name = ""

while name == "":
    name = input("What is your name? ")

length = len(name)

if length > 1:
    print(name[1::2])

