class jugador:
    def __init__(self, jugador_id, jugador_nombre, jugador_plante):
        self.jugador_id = jugador_id
        self.jugador_nombre = jugador_nombre
        self.jugador_plante = jugador_plante

    def get_id(self):
        return self.jugador_id

    def get_nombre(self):
        return self.jugador_nombre

    def get_dinero(self):
        return self.jugador_plante

    def agregar_dinero(self, valor):
        self.jugador_plante = self.jugador_plante + valor

    def retirar_dinero(self, valor):
        self.jugador_plante = self.jugador_plante - valor
