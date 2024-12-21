x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))
if x > y and x > z:
    print(f"Самое большое число:{x}")
elif y > x and y > z:
    print(f"Самое большое число:{y}")                                                                                                           
else:
    print(f"Самое большое число:{z}")