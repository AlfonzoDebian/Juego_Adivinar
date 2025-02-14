import random

n = int(input("introducir valor: "))
i = 0
i = i + 1

maq = random.randrange(1, 100)
while n != maq:
    if n < maq:
        print("El valor es -")
        n = int(input("Introducir: "))
    else:
        print("El valor es +")
        n = int(input("Introducir: "))
else:
    print("Ganastes. ")
i = i + 1

print("intentos: ", i)