from logica.jugador import jugador
from logica.turno import *


class partida:

    def __init__(self, id_partida, valor_partida):
        self.id_partida = id_partida
        self.valor_partida = valor_partida
        self.lista_jugadores = list()
        self.lista_turnos = list()
        self.acumulado = self.calcular_acumulado_inicial()
        self.situacion = "Empezada"

    def add_Jugador(self, jugador_id, jugador_nombre, jugador_plante):
        bandera = False
        for i in self.lista_jugadores:
            id_jugador = getattr(i, 'jugador_id')
            if id_jugador == int(jugador_id):
                bandera = True
        if bandera == True:
            print("Este jugador ya existe")
        else:
            self.lista_jugadores.append(jugador(jugador_id, jugador_nombre, jugador_plante))

    def listar_jugadores(self):
        for juga in self.lista_jugadores:
            dato = getattr(juga, 'jugador_id'), ".",
            nombre = getattr(juga, 'jugador_nombre')
            print(dato)
            print(nombre)

    def calcular_acumulado_inicial(self):
        valor = self.valor_partida * len(self.lista_jugadores)
        return valor

    def add_turno(self, jugador, turno_id):
        self.lista_turnos.append(turno(turno_id, jugador.get_nombre()))

    def buscar_Jugador(self, jugador_id):
        encuentra_jugador = -1
        index = 0
        for t in self.lista_jugadores:
            id_jugador_actual = getattr(t, 'jugador_id')
            if id_jugador_actual == jugador_id:
                encuentra_jugador = index
            index += 1
        return encuentra_jugador

    def get_plante_inicial(self):
        return self.valor_partida

    def get_win(self):
        var = len(self.lista_turnos)
        index = 0
        for turnos in self.lista_turnos:
            if index == var - 1:
                print("Turno: ", getattr(turnos, 'id_turno'))
                print("Jugador: ", getattr(turnos, 'jugador_nombre'))
            index += 1

    def iniciar_partida(self):
        n_jugador = 0
        n_turno = 1
        opc = 0

        if self.situacion != "Empezada":
            print("Esta partida ya a finalizado")
        else:
            while opc>-1:
                print("-------------------------------------------------------------------------------")
                print("Turno", n_turno, "Lanza Jugador", self.lista_jugadores[n_jugador].get_nombre())
                input("ENTER para lanzar ")

                resultado_turno = turno.retornar_valor_sacado(self)
                self.add_turno(self.lista_jugadores[n_jugador],n_turno)

                print("Cayo en: ", resultado_turno)
                if resultado_turno == 'Toma1':
                    self.lista_jugadores[n_jugador].agregar_dinero(100)
                    self.valor_partida = self.valor_partida - 100
                    print('El acumulado de la partida este turno es : ', self.valor_partida)
                    print('El acumulado del jugador es: ', self.lista_jugadores[n_jugador].get_dinero())
                    if self.valor_partida <= 0:
                        opc = -1
                    n_jugador = n_jugador + 1

                if resultado_turno == 'Toma2':
                    self.lista_jugadores[n_jugador].agregar_dinero(200)
                    self.valor_partida = self.valor_partida - 200
                    print('El acumulado de la partida este turno es : ', self.valor_partida)
                    print('El acumulado del jugador es: ', self.lista_jugadores[n_jugador].get_dinero())
                    if self.valor_partida <= 0:
                        opc = -1
                    n_jugador = n_jugador + 1
                if resultado_turno == 'Pon1':
                    self.lista_jugadores[n_jugador].retirar_dinero(100)
                    self.valor_partida = self.valor_partida + 100
                    print('El acumulado de la partida este turno es : ', self.valor_partida)
                    print('El acumulado del jugador es: ', self.lista_jugadores[n_jugador].get_dinero())
                    if self.lista_jugadores[n_jugador].get_dinero() <= 0:
                        print('El jugador ', self.lista_jugadores[n_jugador])
                        print("Esta eliminado, sin plante")
                        self.lista_jugadores.pop(n_jugador)
                    n_jugador = n_jugador + 1
                if resultado_turno == 'Pon2':
                    self.lista_jugadores[n_jugador].retirar_dinero(200)
                    self.valor_partida = self.valor_partida + 200
                    print('El acumulado de la partida este turno es : ', self.valor_partida)
                    print('El acumulado del jugador es: ', self.lista_jugadores[n_jugador].get_dinero())
                    if self.lista_jugadores[n_jugador].get_dinero() <= 0:
                        print('El jugador ', self.lista_jugadores[n_jugador])
                        print("Esta eliminado, sin plante")
                        self.lista_jugadores.pop(n_jugador)
                    n_jugador = n_jugador + 1
                if resultado_turno == 'TodosPonen':
                    j_num = 0
                    for j in self.lista_jugadores:
                        self.lista_jugadores[j_num].retirar_dinero(100)
                        self.valor_partida = self.valor_partida + 100
                        print('El acumulado de la partida este turno es : ', self.valor_partida)
                        jugador_actual=self.lista_jugadores[j_num].get_nombre()
                        print('El acumulado del jugador '+jugador_actual+' es: ', self.lista_jugadores[j_num].get_dinero())
                        if self.lista_jugadores[j_num].get_dinero() <= 0:
                            print('El jugador ', self.lista_jugadores[j_num])
                            print("Esta eliminado, sin plante")
                            self.lista_jugadores.pop(j_num)
                        j_num = j_num + 1
                    n_jugador = n_jugador + 1

                if resultado_turno == 'TomaTodo':
                    self.lista_jugadores[n_jugador].agregar_dinero(self.valor_partida)
                    self.valor_partida = 0
                    print('Felicidades, acabas de ganar el juego.')
                    print("El acumulado del jugador es: ", self.lista_jugadores[n_jugador].get_dinero())
                    opc = -1
                n_turno = n_turno + 1
                if n_jugador == len(self.lista_jugadores):
                    n_jugador = 0
            self.situacion = "Acabada"
