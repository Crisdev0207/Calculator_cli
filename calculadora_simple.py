### Un programa que simula una calculadora básica con las operaciones: suma, resta, multiplicación y división.

def calculadora():
    print("Selleccione el tipo de operación que desea realizar: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = input("Introduce la opción entre (1/2/3/4): ")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if operacion == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacion == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operacion == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operacion == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: División entre el número 0 no es permitida")
    else:
        print("Opción inválida")


calculadora()