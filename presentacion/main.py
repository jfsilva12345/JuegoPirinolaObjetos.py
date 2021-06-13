from logica.partida import partida
from logica.pirinola import *

piri = pirinola("nombre_pirinola")

part = partida(1, 5000)
part.add_Jugador(1, "James", 20000)
part.add_Jugador(2, "Silva", 30000)
piri.add_Partida(part)

opc = 0

while opc != 4:

    if opc != 0 and opc != 1 and opc != 2 and opc != 3 and opc != 4:
        print("-------------------------------------------------------------")
        print("Digite una opcion valida")

    print("1) Nueva Partida")
    print("2) Iniciar Partida")
    print("3) Consultar Ganador")
    print("4) Salir.")

    opc = input("Digite una opcion...")
    if opc.isdigit():
        opc = int(opc)

    if opc == 1:
        try:
            print("-------------------------------------------------------------")
            ide = int(input("Ingrese la id de la partida: "))
            valor = int(input("el valor de la partida: "))
            piri.add_Partida(partida(ide, valor))
            numero_jugadores = int(input("Numero de jugadores: "))
            partida_actual = len(piri.partidas)
            for i in range(numero_jugadores):
                id_jugador = int(input("Ingrese el id del jugador numero "+i+": "))
                nombre = input("Ingrese el nombre del jugador "+i+": ")
                dinero = int(input("Ingrese la cantidad de dinero "+i+": "))
                if dinero >= valor:
                    piri.partidas[partida_actual - 1].add_Jugador(id_jugador, nombre, dinero)
                else:
                    print("el plante de el jugador "+i+" es muy poco")
        except:
            print("Fallo al ingresar nueva partida 1")

    if opc == 2:
        print("-------------------------------------------------------------")
        try:
            piri.listar_Partidas()
            index = int(input("Seleccione la partida que desea jugar: "))
            piri.partidas[index - 1].iniciar_partida()
        except:
            print("Valor incorrecto")

    if opc == 3:
        print("-------------------------------------------------------------")
        try:
            piri.listar_Partidas()
            index = int(input("Seleccione la partida que desea consultar: "))
            piri.partidas[index - 1].get_win()
        except:
            print("Valor incorrecto")
