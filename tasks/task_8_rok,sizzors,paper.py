import random
камннь = 1
ножницы = 2
бумага = 3
random_number = random.randint( 1, 2, 3  )
знак = input("Выберите: камннь, ножницы или бумага: ")
print(f"Компютер выбрал:{random_number}")
if знак == камннь and random_number == камннь:
    print("Ничья!")
elif знак == камннь and random_number == бумага:
    print("Вы проиграли!")
elif знак == камннь and random_number == ножницы:
    print("Вы выграли!")
elif знак == ножницы and random_number == ножницы:
    print("Ничья!")
elif знак == ножницы and random_number == камннь:
    print("Вы проиграли!")
elif знак == ножницы and random_number == бумага:
    print("Вы выграли!")
elif знак == бумага and random_number == бумага:
    print("Ничья!")
elif знак == бумага and random_number == ножницы:
    print("Вы проиграли!")
elif знак == бумага and random_number == камннь:
    print("Вы выграли!")
else:
    print("Вы проиграли!")