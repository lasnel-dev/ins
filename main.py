# def Checker(var_1):
#     if type(var_1) != str:
#         raise TypeError()
#
#     else:
#         return var_1
#
# var = 10
# try:
#     Checker(var)
# except TypeError:
#     print("Ми створили помилку")
#
#
# class BuildingError(Exception):
#     def __str__(self):
#         return f"With so much material the house cannot build!"
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material >= limit_value:
#         return "Enough material"
#     else:
#         raise BuildingError(amount_of_material)
#
# material = 250
# try:
#     print(check_material(material, 300))
# except BuildingError:
#     print("Де матеріали?")



#
# import warnings
#
# warnings.simplefilter("ignore", SyntaxWarning)
# warnings.simplefilter("error", ImportWarning)
#
# warnings.warn("Warning, no code here", SyntaxWarning)
#
# try:
#     warnings.warn("error", ImportWarning)
#
# except:
#     print("end")

from math import floor


class SoHighValue(Exception):
    def __str__(self):
        return f"So big value"

def check_count(year):
    try:
        num = 2024 - int(year)
    except:
        raise TypeError()

    if int(year) > 2024:
        raise SoHighValue()
    else:
        return floor(num/4)

while True:
    try:
        print(check_count(input()))
    except SoHighValue:
        print("Завелике значення")
    except TypeError:
        print("Вказане не число")