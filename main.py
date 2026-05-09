#Menu principal del programa, que permite al usuario interactuar con el sistema operativo y gestionar los procesos.
from sistema_operativo import SistemaOperativo

def main():
    sistema = SistemaOperativo()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar Proceso")
        print("2. Modificar Estado de Proceso")
        print("3. Eliminar Proceso")
        print("4. Mostrar Procesos")
        print("5. Ejecutar Procesos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema.agregar_proceso()
        elif opcion == "2":
            id_proceso = int(input("Ingrese el ID del proceso a modificar: "))
            if type(id_proceso) != int:
                print("ID de proceso no válido. Por favor, ingrese un número entero.")
                continue
            nuevo_estado = input("Ingrese el nuevo estado del proceso: ")
            sistema.modificar_estado_proceso(id_proceso, nuevo_estado)
        elif opcion == "3":
            id_proceso = int(input("Ingrese el ID del proceso a eliminar: "))
            if id_proceso != int:
                print("ID de proceso no válido. Por favor, ingrese un número entero.")
                continue
            sistema.eliminar_proceso(id_proceso)
        elif opcion == "4":
            sistema.mostrar_procesos()
        elif opcion == "5":
            sistema.ejecutar_procesos()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()