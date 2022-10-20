#3. Crea una aplicación que permita adivinar un número. 
#En primer lugar la aplicación solicita un número entero por teclado. 
#A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. 
#El programa termina cuando se acierta el número.

#Solución

#Espacio para hacer mas bonito a la vista
print ("")

#Variables a solicitar
nsecreto = int(input("Numero secreto: "))
num = int(input("Introduce el numero que creas que es el correcto: "))

#Bucle
while num != nsecreto:
    if num > nsecreto:
        print("El numero introducido es mayor que el numero secreto")
    else:
        print("El numero introducido es menor que el numero secreto")
    print ("")
    num = int(input("Introduce otro numero para probar de nuevo: "))

#Fuera del bucle, el numero ya ha sido acertado
print("Has acertado")