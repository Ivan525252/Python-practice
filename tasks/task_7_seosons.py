month = int(input("Введите номер месяца (от 1 до 12): "))

if month == 1 or month == 2 or month == 12:
    print("Этот месяц относится к времени года: зима")
elif month == 3 or month == 4 or month == 5:
    print("Этот месяц относится к времени года: весна")
elif month == 6 or month == 7 or month == 8:
    print("Этот месяц относится к времени года: лето")
elif month == 9 or month == 10 or month == 11:
    print("Этот месяц относится к времени года: осень")
else:
    print("Ошыбка")