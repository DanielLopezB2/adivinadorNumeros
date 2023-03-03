import random

print()
rango_numero = input("Digite un número: ")
print()

if rango_numero.isdigit():
    rango_numero = int(rango_numero)

    if rango_numero <= 0:
        print("Por favor ingrese un número mayor a 0")
        print()
        quit()

else:
    print("Por favor ingrese un número")
    print()
    quit()

numero = random.randint(0, rango_numero)
intentos = 0

while True:

    intentos += 1
    adivinar = input("Adivina el número: ")

    if adivinar.isdigit():
        adivinar = int(adivinar)

    else:
        print("Por favor ingrese un número")
        print()
        continue

    if adivinar == numero:
        print("Adivinaste!")
        print("El número correcto era: ",numero)
        print()
        break

    else:
        print("No adivinaste!")
        print()

print("Lograste adivinar el número en: ",intentos, "intentos")
print()