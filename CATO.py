import turtle
t = turtle.Turtle()
t.speed(20)

posicion_circulo = [0]

jugadas_totales = []

jugador1 = []
jugador2 = []

posiciones_ganadoras = [1,2,3,4,7]

dif_valida_vert = 3
dif_valida_hor = 1
dif_valida_dia = 4
dif_valida_dia2 = 5

Analizar = 0    

No_ganador = True


class DibujosTablero:

    def __init__(self, width, height):
        self.width = width
        self.height= height
    def Tablero(self):
        screen = turtle.Screen()

        screen.setup(self.width, self.height)

        R1W = self.width/6
        R1H = self.height/6

        t.penup()

        t.goto(-self.width/2, R1H)
        t.pendown()
        t.forward(self.width)
        t.penup()

        t.goto(-self.width/2, -R1H)
        t.pendown()
        t.forward(self.width)
        t.penup()

        t.goto(-R1W, self.height/2)
        t.pendown()
        t.goto(-R1W,-self.height/2)
        t.penup()

        t.goto(R1W, self.height/2)
        t.pendown()
        t.goto(R1W, -self.height/2)

        for y in range(1,-2, -1):
            for x in range(-1,2):
                t.penup()
                t.goto((self.width/3)*x, (self.height/3)*y)
                t.pendown()
                t.dot(10, "red")
                posicion_actual = t.position()
                posicion_circulo.append(posicion_actual)

class Figuras:
    def __init__(self, tablero, cuadrante):
        self.cuadrante = cuadrante
        self.tablero = tablero
        self.abajo_ir = 0
        self.tamaño_figuras= self.tablero.height/8

    def Circulo(self):
        
        t.penup()
        t.goto(posicion_circulo[self.cuadrante])
        #posicion_llegada = t.position()
        #print(posicion_llegada)
        t.right(90)
        t.forward(self.tamaño_figuras)
        t.left(90)
        #self.abajo_ir = [posicion_llegada[0], posicion_llegada[1] - (self.tablero.height)/6]
        #t.goto(self.abajo_ir)
        t.pendown()
        t.circle(self.tamaño_figuras)
        t.penup()
    
    def Tacha(self):
        t.penup()
        t.goto(posicion_circulo[self.cuadrante])
        for _ in range(4):
            t.right(45)
            t.pendown()
            t.forward(self.tamaño_figuras)
            t.backward(self.tamaño_figuras)
            t.right(45)
            t.penup()

class Comprobador:
    def __init__(self, jugadas1, jugadas2 ):
        self.jugadas1 = jugadas1
        self.jugadas2 = jugadas2
        self.No_ganador = No_ganador
    
    def Comprobador_jugador1(self):
        for i in range(0,4):   #Verificador para el jugador 1 (5 jugadas)
            if not(self.No_ganador):
                break

            elim2 = i+1
            for x in range(elim2,5):
                jugada_eliminada2 = self.jugadas1.pop(x)
                jugada_eliminada = self.jugadas1.pop(i)
                jugada1 = self.jugadas1[0]

                if jugada1 in posiciones_ganadoras:
                    Resta1 = self.jugadas1[Analizar+1] - self.jugadas1[Analizar]
                    Resta2 = self.jugadas1[Analizar+2] - self.jugadas1[Analizar+1]
                    Verificar_hor = Resta1 == Resta2 and Resta1 == dif_valida_hor
                    Verificar_ver = Resta1 == Resta2 and Resta1 == dif_valida_vert
                    Verificar_dia = Resta1 == Resta2 and Resta1 == dif_valida_dia
                    Verificar_dia2 = Resta1 == Resta2 and self.jugadas1[1] == 5

                    if Verificar_hor or Verificar_ver or Verificar_dia or Verificar_dia2:
                        self.No_ganador = False
                        print(f"Posicipon ganadora: {self.jugadas1}")
                        
                        t.penup()
                        t.goto(posicion_circulo[self.jugadas1[0]])
                        t.pendown()
                        t.goto(posicion_circulo[self.jugadas1[2]])
                        t.penup

                        print(not(self.No_ganador))
                        break

                self.jugadas1.insert(i, jugada_eliminada)
                self.jugadas1.insert(x, jugada_eliminada2)

    def Comprobador_jugador2(self):
        for i in range(0,4):   #Verificador para el jugador 2 (4 jugadas)
    
            jugada_eliminada = self.jugadas2.pop(i)
            jugada1 = self.jugadas2[0]

            if jugada1 in posiciones_ganadoras:

                Resta1 = self.jugadas2[Analizar+1] - self.jugadas2[Analizar]
                Resta2 = self.jugadas2[Analizar+2] - self.jugadas2[Analizar+1]

                Verificar_hor = Resta1 == Resta2 and Resta1 == dif_valida_hor
                Verificar_ver = Resta1 == Resta2 and Resta1 == dif_valida_vert
                Verificar_dia = Resta1 == Resta2 and Resta1 == dif_valida_dia
                Verificar_dia2 = Resta1 == Resta2 and self.jugadas2[1] == 5
    
                if Verificar_hor or Verificar_ver or Verificar_dia or Verificar_dia2:
                    self.No_ganador = False
                    print(f"Posicipon ganadora jugador 2: {self.jugadas2}")
                    t.penup()
                    t.goto(posicion_circulo[self.jugadas2[0]])
                    t.pendown()
                    t.goto(posicion_circulo[self.jugadas2[2]])
                    t.penup

                    print(not(self.No_ganador))
                    break

            self.jugadas2.insert(i, jugada_eliminada)
    
    def Comprobador_3_1(self):
        for i in range(0,4):   #Verificador para 3 jugadas del j1
            jugada1 = self.jugadas1[0]

            if jugada1 in posiciones_ganadoras:

                Resta1 = self.jugadas1[Analizar+1] - self.jugadas1[Analizar]
                Resta2 = self.jugadas1[Analizar+2] - self.jugadas2[Analizar+1]

                Verificar_ver = Resta1 == Resta2 and Resta1 == dif_valida_vert
                Verificar_dia = Resta1 == Resta2 and Resta1 == dif_valida_dia
                Verificar_hor = Resta1 == Resta2 and Resta1 == dif_valida_hor
                Verificar_dia2 = Resta1 == Resta2 and self.jugadas1[1] == 5
    
                if Verificar_hor or Verificar_ver or Verificar_dia or Verificar_dia2:
                    self.No_ganador = False
                    print(f"Posicipon ganadora jugador 2: {self.jugadas1}")

                    t.penup()
                    t.goto(posicion_circulo[self.jugadas1[0]])
                    t.pendown()
                    t.goto(posicion_circulo[self.jugadas1[2]])
                    t.penup

                    print(not(self.No_ganador))
                    break

def main():

    limite_jugadas = 4
    num_jugada = 1

    tablero = DibujosTablero(500,500)
    tablero.Tablero()
    
    No_ganador = True

    while True:
        try:
            Jugada1 = int(input("Ingresa la jugada uno de los círculos: "))
            if 1<= Jugada1 <= 9:
                jugador1.append(Jugada1)
                jugadas_totales.append(Jugada1)
                Jugada1 = Figuras(tablero, Jugada1)
                Jugada1.Circulo()
                break
            else:
                print(f"Ingrese un número de cuadrante correcto (1-9)")
        
        except ValueError:
            print(f"Ingrese un número de cuadrante correcto (1-9)")
    
    while limite_jugadas >= 1 and No_ganador == True:

        jugador2.sort()
        jugador1.sort()

        while True:
            try:
                Jugada = int(input(f"Ingresa la jugada {num_jugada} de las tachas: "))
                if 1 <= Jugada <= 9 and Jugada not in jugadas_totales:
                    jugador2.append(Jugada)
                    jugadas_totales.append(Jugada)
                    Jugada = Figuras(tablero, Jugada)
                    Jugada.Tacha()
                    break
                else:
                    print(f"Ingrese un número de cuadrante correcto (1-9)")
            except ValueError:
                print(f"Ingrese un número de cuadrante correcto (1-9)")

        cant_jugadas2 = len(jugador2)
        cant_jugadas1 = len(jugador1)

        jugador2.sort()
        jugador1.sort()

        if cant_jugadas1 == 3 and cant_jugadas2 == 2: #Comprobar J1 en 3 jugadas
            jugadores_final = Comprobador(jugador1, jugador1)
            jugadores_final.Comprobador_3_1()
            No_ganador = jugadores_final.No_ganador
        elif cant_jugadas1 == 3 and cant_jugadas2 == 3: #Comprobar J2 en 3 jugadas
            jugadores_final = Comprobador(jugador2, jugador2)
            jugadores_final.Comprobador_3_1()
            No_ganador = jugadores_final.No_ganador
        elif cant_jugadas1 == 4 and cant_jugadas2 == 3: #Comprobar J1 en 4 jugadas
            jugadores_final = Comprobador(jugador1, jugador1)
            jugadores_final.Comprobador_jugador2()
            No_ganador = jugadores_final.No_ganador
        elif cant_jugadas1 == 4 and cant_jugadas2 == 4: #Comprobar J2 en 4 jugadas
            jugadores_final = Comprobador(jugador2, jugador2)
            jugadores_final.Comprobador_jugador2()
            No_ganador = jugadores_final.No_ganador

        if No_ganador == True:
            while True:
                try:    
                    Jugada = int(input(f"Ingresa la jugada {num_jugada+1} de los círculos: "))
                    if 1 <= Jugada <= 9 and Jugada not in jugadas_totales:
                        jugador1.append(Jugada)
                        jugadas_totales.append(Jugada)
                        Jugada = Figuras(tablero, Jugada)
                        Jugada.Circulo()
                        break
                    else:
                        print(f"Ingrese un número de cuadrante correcto (1-9)")
                except ValueError:
                    print(f"Ingrese un número de cuadrante correcto (1-9)")

            jugador2.sort()
            jugador1.sort()

            cant_jugadas2 = len(jugador2)
            cant_jugadas1 = len(jugador1)

            if cant_jugadas1 == 3 and cant_jugadas2 == 2: #Comprobar J1 en 3 jugadas
                jugadores_final = Comprobador(jugador1, jugador1)
                jugadores_final.Comprobador_3_1()
                No_ganador = jugadores_final.No_ganador
            elif cant_jugadas1 == 3 and cant_jugadas2 == 3: #Comprobar J2 en 3 jugadas
                jugadores_final = Comprobador(jugador2, jugador2)
                jugadores_final.Comprobador_3_1()
                No_ganador = jugadores_final.No_ganador
            elif cant_jugadas1 == 4 and cant_jugadas2 == 3: #Comprobar J1 en 4 jugadas
                jugadores_final = Comprobador(jugador1, jugador1)
                jugadores_final.Comprobador_jugador2()
                No_ganador = jugadores_final.No_ganador
            elif cant_jugadas1 == 4 and cant_jugadas2 == 4: #Comprobar J2 en 4 jugadas
                jugadores_final = Comprobador(jugador2, jugador2)
                jugadores_final.Comprobador_jugador2()
                No_ganador = jugadores_final.No_ganador


        num_jugada += 1
        limite_jugadas -= 1


    if No_ganador == True:
        jugadores_final = Comprobador(jugador1, jugador2)
        jugadores_final.Comprobador_jugador1()
        No_ganador = jugadores_final.No_ganador
        if jugadores_final.No_ganador == True:
            jugadores_final.Comprobador_jugador2()
            No_ganador = jugadores_final.No_ganador

    turtle.done()

main()