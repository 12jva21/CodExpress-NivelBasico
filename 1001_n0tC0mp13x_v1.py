#Calculadora precisa
#Implementa + − × ÷ con redondeo comercial a 2 decimales usando decimal.Decimal y ROUND_HALF_UP. División por cero: imprime ERROR:DIV0.
#Entrada: a op b (ej.: 5.005 + 2) · Salida: número a 2 decimales.

from decimal import *
getcontext().prec=3

while True:

    opcion= int(input('''
                    !Bienvenido a la calculadora precisa! elija la operacion que quiere hacer:
                        -1-)Sumar
                        -2-)Restar
                        -3-)Multiplicar
                        -4-)Dividir
                        -5-)salir
                    '''))

    if opcion==1:          
        n1= Decimal(input("Ingrese el primer numero para sumarlo con el otro: "))
        n2= Decimal(input("Ingrese el segundo numero para sumarlo con el otro: "))
        suma= n1+n2
        print(f"su resultado es {suma}")   

    elif opcion==2:
        n1= Decimal(input("Ingrese el primer numero al que se le va a restar el otro: "))
        n2= Decimal(input("Ingrese el segundo numero para restarselo al primero: "))
        resta= n1-n2
        print(f"su resultado es {resta}")

    elif opcion==3:
        n1= Decimal(input("Ingrese el primer numero para multiplicarlo con el otro: "))
        n2= Decimal(input("Ingrese el segundo numero para multiplicarlo con el otro: "))
        multiplicacion= n1+n2
        print(f"su resultado es {multiplicacion}")

    elif opcion==4:
        try:
            n1= Decimal(input("Ingrese el dividendo: "))
            n2= Decimal(input("Ingrese el divisor: "))
            division= n1+n2
            print(f"su resultado es {division}")
        except ZeroDivisionError:
            print("ERROR: DIV0")

    elif opcion==5:
        break

    else:
        print("La opcion seleccionada no es valida, intentelo nuevamente.")

