import task2_module


class Details:
    def __init__(self, name, age, title):
        self.name = name
        self.age = age
        self.title = title


class One:
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.title = input("Enter title: ")


obj = One()
obj1 = Details(obj.name, obj.age, obj.title)
