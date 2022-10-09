while True:
    name = input("Enter name: ")
    if len(name) > 7:
        break
    if name[0].upper() == name[-1].upper():
        print("Good")
