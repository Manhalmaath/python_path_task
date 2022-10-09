import task3_module


class Car:
    def __init__(self, country, model_year, color, fuel_type):
        self.country = country
        self.model_year = model_year
        self.color = color
        self.fuel_type = fuel_type


class ExtraCarInfo(Car):
    def __init__(self, country, model_year, color, fuel_type, car_type, vin_number):
        super().__init__(country, model_year, color, fuel_type)
        self.car_type = car_type
        self.vin_number = vin_number


mercedes = ExtraCarInfo("Germany", 2019, "Black", "Diesel", "Mercedes", "123456789")
ferrari = ExtraCarInfo("Italy", 2020, "Red", "Petrol", "Sport", "987654321")

print(task3_module.car_old(mercedes))
print(task3_module.car_price(mercedes))
task3_module.print_car_info(mercedes)
print(task3_module.car_old(ferrari))
print(task3_module.car_price(ferrari))
task3_module.print_car_info(ferrari)
