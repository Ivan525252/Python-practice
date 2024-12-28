first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
operator = (input("Введите оператор (+, -, *, /):"))

if operator == "+":
    result = first_number + second_number
    print(f"Результат:{result}")
elif operator == "-":
    result = first_number - second_number
    print(f"Результат:{result}")
elif operator == "*":
    result = first_number * second_number
    print(f"Результат:{result}")
elif operator == "/":
    result = first_number / second_number
    print(f"Результат:{result}")
else:
    print("Ошыбка, пожалуста ведите оператор")
