age = int(input("Напишите свой age  "))
is_admin = input("Проверка на админа, true or false  ")

if 20 <= age and is_admin == "false":
    print("Доступ разрешён") 

if 19 >= age:
    print("Доступ запрещён")

if 20 < age and is_admin == "true":
    print("Доступ разрешён. Добро пожаловать администратор!")


