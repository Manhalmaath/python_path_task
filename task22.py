f = True
while f:
    name = input("Enter name: ")
    for char in name:
        if char == "t":
            f = False
