# Aqui hacemos una declaración de variables indicando que ambas trabajaran como enteros, pidiendo introduccion de numeros, si no se declarasen de tipo entero no se sumarian ambas variables se unirian los valores de a y b
a = int(input("Introduzca numero 1:"))
b = int(input("Introduzca numero 2:"))
#Declaracion de variable para calculo sumatorio de variables a y b
suma = a+b
#Mostramos al usuario el resultado de la suma 
print(suma)
# Trabajamos con el condicional para la comparacion de la variable suma con 0 y comprobar si es negativa, positiva o cero la suma
if suma < 0:
    print("Suma negativa")

if suma > 0:
    print("Suma positiva")

if suma == 0:
    print("Suma cero")
