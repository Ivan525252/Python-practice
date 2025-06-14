x = int(input("Ведите розмер: "))
y = input("Ведите знак: ")

for i in range(1, x + 1):
    for j in range(i):
        print(y, end="")
    print()    
