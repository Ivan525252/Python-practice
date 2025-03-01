import random
sign = input("Выбирете: камень, ножницы или бумага:")
random_sign = random.randint( 1, 3 )

if random_sign == 1:
    random_sign = "камень"
elif random_sign == 2:
    random_sign = "ножницы"
elif random_sign == 3:
    random_sign = "бумага"

print(f"Я выбрал: {sign}")
print(f"Комьютер выбрал: {random_sign}")

if not (sign in {"камень", "ножницы", "бумага"}):
    print("Ошыбка, пожалуста впишытие знак")
elif sign == random_sign:
    print("Ничья!")
elif ((sign == "камень" and random_sign == "бумага") 
    or (sign == "ножницы" and random_sign == "камень") 
    or (sign == "бумага" and random_sign == "ножницы")):
    print("Вы проиграли!")
else:
    print("Вы выиграли!")
