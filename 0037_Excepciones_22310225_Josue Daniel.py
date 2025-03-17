#Exepciones

bars = "josue"

try:
    print(bars)

except:
    print("Error encontrado")






ping = True

while ping:
    try:
        num1 = int(input("Introduce un numero para multiplicar: "))
        num2 = int(input("Introduce un numero para multiplicar: "))
    except ValueError:
        print("No has introducido nada")
    else:
        print("El resultado es: ",num1 * num2)
    finally:
        pregunta = input("Quieres seguir multiplicando? introduce S/N:\n")
    if pregunta == "N":
        ping = False
    else:
        print("De acuerdo, vamos a seguir")
