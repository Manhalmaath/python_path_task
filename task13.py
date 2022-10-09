from task12 import Employee


class Manager(Employee):
    def __init__(self):
        super().__init__(input("Enter your name: "),
                         input("Enter your age: "),
                         input("Enter your dept: "),
                         input("Enter your phone: "))
        self.title = input("Enter your title: ")
        self.salary = input("Enter your salary: ")
        self.field = input("Enter your field: ")

    def print_cv(self):
        print(f"""
        Name: {self.name}
        Age: {self.age}
        Dept: {self.dept}
        Phone: {self.phone}
        Title: {self.title}
        Salary: {self.salary}
        Field: {self.field}""")


test = Manager()
test.print_cv()
