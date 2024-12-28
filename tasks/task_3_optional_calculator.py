first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
operator = (input("Введите оператор (+, -, *, /):"))

ответ_1 = first_number + second_number
if operator == "+" :
    print(f"Результат:{ответ_1}")

ответ_2 = first_number - second_number
if operator == "-" :
    print(f"Результат:{ответ_2}")

ответ_3 = first_number * second_number
if operator == "*" :
    print(f"Результат:{ответ_3}")

ответ_4 = first_number / second_number
if operator == "/" :
    print(f"Результат:{ответ_4}")