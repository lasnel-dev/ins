def Checker(var_1):
    if type(var_1) != str:
        raise TypeError()

    else:
        return var_1

var = 10
try:
    Checker(var)
except TypeError:
    print("Ми створили помилку")


class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannot build!"

def check_material(amount_of_material, limit_value):
    if amount_of_material >= limit_value:
        return "Enough material"
    else:
        raise BuildingError(amount_of_material)

