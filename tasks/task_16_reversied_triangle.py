x = int(input("Ведите розмер: "))
y = input("Ведите знак: ")
z = 0

for i in range( x, 0, -1):
    for j in range(i): 
        print(y, end="  ")
        z = z + 1
    print()   
print(z)