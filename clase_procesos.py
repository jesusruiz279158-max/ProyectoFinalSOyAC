class Proceso:
    contador = 0
    def __init__(self, t_llegada, t_ejecucion, estado="Listo", nombre="Proceso"):
        Proceso.contador += 1
        self.id = Proceso.contador
        self.t_llegada = t_llegada
        self.t_ejecucion = t_ejecucion
        self.estado = estado #Puede ser "Listo", "En Ejecución" o "Terminado"
        self.nombre = nombre
        self.t_espera = 0
        self.t_finalizacion = 0
