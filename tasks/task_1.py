age = int(input("Напишите свой age  "))
is_admin = input("Проверка на админа, true or false")
 
if 20 <= age and is_admin == "true":
    print("Доступ разрешён. Добро пожаловать администратор!")
elif 20 <= age and is_admin == "false":
    print("Доступ разрешён")
else :
    print("Доступ запрещён")


