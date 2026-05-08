
from clase_procesos import Proceso

cola_listos = []

#Ingresar datos del nuevo proceso.
t_llegada = int(input("Ingrese el tiempo de llegada del proceso: "))
t_ejecucion = int(input("Ingrese el tiempo de ejecución del proceso: "))
nombre = input("Ingrese el nombre del proceso: ")
estado = "Listo"


nuevo_proceso = Proceso(t_llegada, t_ejecucion, estado, nombre)
cola_listos.append(nuevo_proceso)

print("Proceso agregado a la cola de listos:")
print(cola_listos)