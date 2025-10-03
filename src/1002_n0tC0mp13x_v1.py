#Ecuación de 2º grado
#Resuelve ax^2+bx+c=0. Si a=0 → lineal. Imprime delta=.... Si Δ es cuadrado perfecto, raíces enteras exactas; si no, usa Decimal a 4 decimales (ROUND_HALF_UP). Si Δ<0: sin raices reales.
#Entrada: a b c · Salida: delta=... r1=... r2=... o sin raices reales.

from decimal import *
getcontext().prec=5

a= int(input("Ingrese el coeficiente de la variable elevada al cuadrado: "))
b= int(input("Ingrese el coeficiente de la variable elevada a uno: "))
c= int(input("Ingrese el coeficiente de la variable elevada a cero: "))

if a==0:
    try:
        resultado_a_cero= -c/b
        print(f"la solucion de su ecuacion de segundo grado es {resultado_a_cero} y es lineal")
    except ZeroDivisionError:
        print("ERROR: DIV0")

if a>0:
    discriminante= b**2 - 4*a*c
    print(f"delta= {discriminante}") 
     
    if discriminante>=0:

        resultado_positivo=Decimal((-b + discriminante**0.5)/2*a) 
        resultado_negativo=Decimal((-b - discriminante**0.5)/2*a )
        print(f"r1= {resultado_positivo}, r2= {resultado_negativo}")


    if discriminante<0:
        print("Sin raices reales")




    



