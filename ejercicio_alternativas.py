# 5. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, 
# pero no si es divisible por 100, excepto que también sea divisible por 400.

year=int(input("Introduzca Año:"))

if year%4==0 and year%100!=0 or year%400==0:
    print("Bisiesto")
else:
    print("No bisieo")

# 6. Programa que lea un carácter por teclado y compruebe si es una letra mayúscula.

letra=input("Introduzca Letra:")        
if letra>="A" and letra<="Z":
    print("Mayuscula")
else:
    print("No mayuscula")