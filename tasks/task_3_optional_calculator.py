first_number = float(input("Введите первое число: "))
sekond_number = float(input("Введите второе число: "))
operator = (input("Введите оператор (+, -, *, /):"))

ответ_1 = first_number + sekond_number
if operator == "+" and first_number + sekond_number:
    print("Результат:{ответ_1}")

ответ_2 = first_number - sekond_number
if operator == "-" and first_number - sekond_number:
    print("Результат:{ответ_2}")

ответ_3 = first_number * sekond_number
if operator == "*" and first_number * sekond_number:
    print("Результат:{ответ_3}")

ответ_4 = first_number / sekond_number
if operator == "/" and first_number / sekond_number:
    print("Результат:{ответ_4}")