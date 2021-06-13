class pirinola:

    def __init__(self, nombre_piri):
        self.nombre_piri = nombre_piri
        self.partidas = list()

    def add_Partida(self, prm_partida):
        self.partidas.append(prm_partida)

    def listar_Partidas(self):
        index = 0
        for x in self.partidas:
            print("#", index + 1, " Id partida: ", self.partidas[index].id_partida, " Estado: ",
                  self.partidas[index].situacion)
            index += 1