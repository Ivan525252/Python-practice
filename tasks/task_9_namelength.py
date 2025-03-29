name = input("Введи имя:")
len_name = len(name)

if len_name > 6:
    print("У тебя длинное имя")
elif len_name <= 6 and len_name != 0:
    print("У тебя короткое имя")
else:
    print("Вы ничого не вписали") 