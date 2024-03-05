#hola mundo
nombre = input("Ingrese su nombre: ")

match nombre.lower():
    case "james" | "ricardo" | "maria" | "jose" | "luis" | "ramon" | "jesus" | "juan" | "alexandra" | "alejandra" | \
         "valentina" | "james" | "alejandro" | "miguel" | "sergio" | "moises":
        print("Hola mundo, soy " + str(nombre))
    case _:
        print("Hola mundo, no reconocí tu nombre")

#calcular edad
import datetime

# Introduce la fecha de nacimiento en formato 'YYYY-MM-DD'
fecha_nacimiento = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")

fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
edad = datetime.datetime.now().year - fecha_nacimiento.year

print("Tu edad es:", edad)


#IMC
def calcular_imc(peso, altura):
    # Fórmula del IMC: peso / (altura^2)
    imc = peso / (altura ** 2)
    return imc

# Ejemplo de uso
peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"El Índice de Masa Corporal (IMC) es: {imc:.2f}")

# f-string
mensaje = (f"Tabla de clasificaciones: \n Desnutricion moderada: 16,01-16,99 .\n Bajo peso: 18,5-22 ."
           f"\n Peso normal: 22,1-24,9 .\n Sobrepeso: 25-29,9")
print(mensaje)



#OPERACION CUADRADO TRIANGULO Y SUMA
def cuadrado (a, b):
    return a* b


def triangulo(a, b):
    return a* b /2

def sumar(a, b):
    return a + b


def mostrar_menu():
    print("Seleccione una operación:")
    print("1. cuadrado")
    print("2. triangulo")
    print("3. suma")
    print("4. es par, es impar")


mostrar_menu()
opcion = input("Ingrese el número correspondiente a la operación deseada: ")


if opcion == '1':
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultado = triangulo(a, b)
    print(f"Resultado: {resultado}")

elif opcion == '2':
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultado = cuadrado(a, b)
    print(f"el area es : {resultado}")

if opcion == '3':
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultado = sumar(a, b)
    print(f"Resultado: {resultado}")

    if opcion == '4':

     a = int(input("Ingrese el número: "))

    if a % 2 == 0:
        print(a, "es par.")
    else:
        print(a, "es impar.")
