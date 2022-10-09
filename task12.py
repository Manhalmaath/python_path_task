class Employee:
    def __init__(self, name, age, dept, phone):
        self.name = name
        self.age = age
        self.dept = dept
        self.phone = phone

    def check_age(self):
        if self.age > 30:
            return "You are old"
        elif 18 <= self.age <= 30:
            return "You are young"
        else:
            return "You are a illegal"

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Dept: {self.dept}, Phone: {self.phone}"


ahmed = Employee("Ahmed", 25, "IT", "01000000000")
print(ahmed.check_age())
