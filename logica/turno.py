from random import randint

class turno:
    def __init__(self, id_turno, jugador_nombre):
        self.id_turno = id_turno
        self.jugador_nombre = jugador_nombre
        self.valor_sacado = self.retornar_valor_sacado()


    def retornar_valor_sacado(self):
        valores = ['Toma1', 'Toma2', 'Pon1', 'Pon2', 'TodosPonen', 'TomaTodo']
        valor_opcion = randint(0, 5)
        return valores[valor_opcion]
