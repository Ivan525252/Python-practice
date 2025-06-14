x = int(input("Ведите чиотную цыфру для проверки: "))
quantity_of_even = 0
sume = 0
for i in range(0, x, 2):
    sume = sume + i
    quantity_of_even = quantity_of_even +1
print(sume)
print(quantity_of_even)