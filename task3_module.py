

def car_old(obj):
    return "Old" if obj.model_year < 2000 else "New"


def car_price(obj):
    return "Expensive" if obj.car_type == "Mercedes" else "Cheap"


def print_car_info(obj):
    print(f"""
    Country: {obj.country}
    Type: {obj.car_type}
    Model Year: {obj.model_year}""")
