print ("Fibonacci Iterativo")
def Iterativo_Fibonacci (Posicion, Out_Salida):
    Ejecuta_Ahora = 0
    Ejecuta_Despues = 1
    for i in range (Posicion + 1):
        if Out_Salida:
            print(str(Ejecuta_Ahora)+ ", ", end = "")
        Valor_Temporal = Ejecuta_Ahora
        Ejecuta_Ahora = Ejecuta_Despues
        Ejecuta_Despues = Ejecuta_Despues + Valor_Temporal
    return Valor_Temporal

Posicion = int(input("Ingrese la posición a calcular: "))

print(f"Imprimiendo Fibonacci hasta {Posicion}")
Iterativo_Fibonacci(Posicion, True)





print ("Fibonacci Recursivo")
def Recursivo_Fibonacci (Posicion):
    if Posicion < 2:
        return Posicion
    return Recursivo_Fibonacci (Posicion - 1) + Recursivo_Fibonacci (Posicion - 2)

# IMPRIMIENDO HASTA LLEGAR AL RESULTADO
print(f"Imprimiendo serie hasta posición {Posicion}")
Iterativo_Fibonacci (Posicion, True)
# CALCULANDO EL VALOR
valor = Iterativo_Fibonacci (Posicion, False)
print(f"\nFibonacci de {Posicion} con método iterativo es {valor}")
# DE MANERA ITERATIVA
valor = Recursivo_Fibonacci (Posicion)
print(f"Fibonacci de {Posicion} con método recursivo es {valor}")





#Fibonacci MEMORIA
contenedor = {}
def Memoria_Fibonacci(num):
        if  (num < 2):
                return 1
        elif (num in contenedor):
                return contenedor[num]
        else:
                x = Memoria_Fibonacci(num - 1) + Memoria_Fibonacci(num - 2)
                contenedor[num] = x
                return x

#Corrigiendo el input del valor a calcular
Ingreso = (int(input("El orden a calcular: ")))
IngresoCorregido = Ingreso - 1
print(Memoria_Fibonacci(IngresoCorregido))

