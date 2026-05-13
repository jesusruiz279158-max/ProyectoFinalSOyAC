import time
from clase_procesos import Proceso

#Clase que representa el sistema operativo, que contiene la lista de procesos y métodos para gestionar los procesos.

class SistemaOperativo:
    def __init__(self):
        self.procesos = []

#Crear un nuevo proceso y agregarlo a la cola de listos.
    def agregar_proceso(self):

        try:
            t_llegada = int(input("Ingrese el tiempo de llegada del proceso: "))
            t_ejecucion = int(input("Ingrese el tiempo de ejecución del proceso: "))
        except ValueError:
            print("Debe ingresar números enteros.")
            return

        nombre = input("Ingrese el nombre del proceso: ")

        if nombre.strip() == "":
            print("Nombre de proceso no válido.")
            return

        estado = "Listo"

        nuevo_proceso = Proceso(t_llegada, t_ejecucion, estado, nombre)
        self.procesos.append(nuevo_proceso)

        print(f"Proceso '{nuevo_proceso.nombre}' agregado con ID '{nuevo_proceso.id}'.")


#Modificar el estado de un proceso específico.
    def modificar_estado_proceso(self, id_proceso, nuevo_estado):

        estados_validos = ["Listo", "En Ejecución", "Terminado"]

        if nuevo_estado not in estados_validos:
            print("Estado no válido. Por favor, ingrese 'Listo', 'En Ejecución' o 'Terminado'.")
            return

        for proceso in self.procesos:

            if proceso.id == id_proceso:
                proceso.estado = nuevo_estado

                print(f"Estado del proceso '{proceso.nombre}' (ID: {proceso.id}) modificado a '{nuevo_estado}'.")
                return

        print(f"No se encontró un proceso con ID '{id_proceso}'.")


#Eliminar un proceso de la lista de procesos.
    def eliminar_proceso(self, id_proceso):
        for proceso in self.procesos:
            if proceso.id == id_proceso:
                self.procesos.remove(proceso)
                print(f"Proceso '{proceso.nombre}' (ID: {proceso.id}) eliminado.")
                return
        print(f"No se encontró un proceso con ID '{id_proceso}'.")


#Mostrar la lista de procesos con sus detalles.
    def mostrar_procesos(self):
        if not self.procesos:
            print("No hay procesos en el sistema.")
            return

        print("\n--- Lista de Procesos ---")
        for proceso in self.procesos:
            print(f"ID: {proceso.id}, Nombre: {proceso.nombre}, Tiempo de Llegada: {proceso.t_llegada}, "
                  f"Tiempo de Ejecución: {proceso.t_ejecucion}, Estado: {proceso.estado}, "
                  f"Tiempo de Espera: {proceso.t_espera}, Tiempo de Finalización: {proceso.t_finalizacion}")


#Método para ejecutar los procesos en la cola de listos utilizando el algoritmo de planificación FCFS (First-Come, First-Served).
    def ejecutar_procesos(self):
        self.procesos.sort(key=lambda p: p.t_llegada)  # Ordenar por tiempo de llegada
        tiempo_actual = 0

        procesos_a_ejecutar = [p for p in self.procesos if p.estado != "Terminado"]

        for proceso in procesos_a_ejecutar:
            if proceso.t_llegada > tiempo_actual:
                tiempo_actual = proceso.t_llegada  # Avanzar el tiempo si el proceso llega después del tiempo actual

            if proceso.estado == "Terminado":
                continue  # Saltar procesos ya terminados
            
            #Cambiar el estado del proceso a "En Ejecución" y simular su ejecución.
            proceso.estado = "En Ejecución"
            print(f"Ejecutando proceso '{proceso.nombre}' (ID: {proceso.id})...")
            time.sleep(proceso.t_ejecucion)  # Simular la ejecución del proceso
            proceso.estado = "Terminado"
            proceso.t_finalizacion = tiempo_actual + proceso.t_ejecucion
            proceso.t_espera = tiempo_actual - proceso.t_llegada
            tiempo_actual += proceso.t_ejecucion
            print(f"Proceso '{proceso.nombre}' (ID: {proceso.id}) terminado. Tiempo de finalización: {proceso.t_finalizacion}, Tiempo de espera: {proceso.t_espera}.")


