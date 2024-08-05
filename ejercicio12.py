def dividir_numeros(numerador, denominador):
    try:
        resultado = numerador / denominador
        print("El resultado de la división es:", resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
dividir_numeros(num1, num2)
