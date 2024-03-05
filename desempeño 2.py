#hola mundo
"""
nombre = input("Ingrese su nombre: ")

match nombre.lower():
    case "james" | "ricardo" | "maria" | "jose" | "luis" | "ramon" | "jesus" | "juan" | "alexandra" | "alejandra" |\
         "valentina" | "james" | "alejandro" | "miguel" | "sergio" | "moises":
        print("Hola mundo, soy " + str(nombre))
    case _:
        print("Hola mundo, no reconocí tu nombre")
"""
#SUMA DE NUMEROS

"""
def suma(a, b):
    resultado = a + b
    return resultado
a = float(input("ingrese primer dato: "))
b = float(input("ingrese segundo dato: "))
# Llamada a la funcion con argumentos
resultado_suma = suma(a, b)
print(resultado_suma)

"""
#calcular la edad

"""
import datetime
birthdate = "31-05-2008"
day,month,year = map(int, birthdate.split("-"))
today = datetime.date.today()
age = today.year - year - ((today.month, today.day) < (month, day))
print("Your age is",age,"years.")

"""
#imc

"""
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
"""

#par e impar
"""
n = int(input("Ingrese un número: "))

if n % 2 == 0:
    print(n, "es par.")
else:
    print(n, "es impar.")
"""
#area de un cuadrado
"""
base=int(input("Ingrese la base del cuadrado: "));
altura=int(input("ingrese la altura del cuadrado: "))
area= (base * altura)
print("el area de el cuadrado es",area)
"""
# el area de un triangulo
"""
base=int(input("Ingrese la base del triangulo: "));
altura=int(input("ingrese la altura del triangulo: "))
area= (base * altura)/2
print("el area de el triangulo es",area)
"""