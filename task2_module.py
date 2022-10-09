def check_neme(name):
    return name[0].upper() == name[-1].upper()


def check_age(age):
    if age > 30:
        return "Old"
    elif 20 <= age <= 30:
        return "Young"


def name_len(name):
    return len(name)

