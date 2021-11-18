"""
Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""

number = input("Введите число: ")
if number.isdigit():
    print(f"Число {number} целое")
elif number.upper() == number:
    print(f"Число {number} дробное")
    i = 0
    lef = ""
    rig = ""
    for _ in number:
        if _.isdigit() and i == 0:
            lef += str(_)
        elif _.isdigit() and i > 0:
            rig += str(_)
        else:
            i += 1
    print(int(lef) == int(rig))
else:
    print(f"{number} не число!")

