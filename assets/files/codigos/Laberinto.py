import matplotlib.pyplot as plt

#se crea la clase casilla que tiene la pocision en la que se esta y sus datos
class Casilla:
    def __init__(self,x,y,muro):
        self.x = x
        self.y = y
        self.muro = muro
        self.entrada = ""
        self.up = False
        self.right = False
        self.down = False
        self.left = False
#se crea la clase laberinto que tendrá los metodos para crear el laberinto, pintarlo y resolverlo
class laberinto:
    def __init__(self,ListaN):
        self.nivel = []
        self.inicio = [None,None]
        self.final = [None,None]
        self.camino = []
        #se recorre el nivel
        for x in range (len(ListaN)):
            fila = []
            for y in range(len(ListaN[x])):
                fila.append(Casilla(x, y, ListaN[x][y] == "1")) # si la casilla es un 1 es un muro
                if ListaN[x][y] == "I":
                    self.inicio = [x,y]
                elif ListaN[x][y] == "F":
                    self.final = [x,y]
            self.nivel.append(fila) 
        self.camino.append(self.nivel[self.inicio[0]][self.inicio[1]]) #se agrega el inicio del camino

    # metodo avanzar, valida si ya se camino por un lugar o si puede Caminar y de lo contrario regresa
    def Avanzar(self):
        Camine = self.camino[-1]
        if not Camine.up and Camine.entrada != "up":
            Caminar = self.nivel[Camine.x-1][Camine.y]
            if not Caminar.muro:
                Camine.up = True
                Caminar.entrada = "down"
                self.camino.append(Caminar)
                return
        if not Camine.right and Camine.entrada != "right":
            Caminar = self.nivel[Camine.x][Camine.y+1]
            if not Caminar.muro:
                Camine.right = True
                Caminar.entrada = "left"
                self.camino.append(Caminar)
                return
        if not Camine.down and Camine.entrada != "down":
            Caminar = self.nivel[Camine.x+1][Camine.y]
            if not Caminar.muro:
                Camine.down = True
                Caminar.entrada = "up"
                self.camino.append(Caminar)
                return
        if not Camine.left and Camine.entrada != "left":
           Caminar = self.nivel[Camine.x][Camine.y-1]
           if not Caminar.muro:
               Camine.left = True
               Caminar.entrada = "right"
               self.camino.append(Caminar)
               return
        self.camino.pop()
    
    #metodo que determina si ya se encontro el final del laberinto
    def Finalizado(self):
        if len(self.camino)==0:return True
        Ca = self.camino[-1]
        return Ca.x == self.final[0] and Ca.y == self.final[1]
    
    # se crea de manera visual el laberinto, teniendo que invertir las cordenadas ya que el grafo de la libreria importada tiene el 0,0 abajo y el laberinto arriba
    def Pintar(self):
        for x in range(len(self.nivel)):
            for y in range (len(self.nivel[x])):
                if self.nivel[x][y].muro:
                    plt.plot([y],[len(self.nivel)-x-1],linestyle='None',marker='s',markersize=15,color='black')
        plt.plot([self.inicio[1]],[len(self.nivel)-self.inicio[0]-1],linestyle='None',marker='.',markersize=10,color='blue')
        plt.plot([self.final[1]],[len(self.nivel)-self.final[0]-1],linestyle='None',marker='.',markersize=10,color='green')
        plt.title("LABERINTO")
        for c in self.camino:
            plt.plot(c.y,[len(self.nivel)-c.x-1],linestyle='None',marker='*',markersize=9,color='red')

#creacion de los niveles
l1 =[
"1I1111111111111",
"101111000000001",
"100000011111111",
"111111011011101",
"111111000000001",
"111110111011111",
"100000001011111",
"111110111011111",
"111000000011001",
"111011111111101",
"111000000000001",
"111010110111011",
"111010010111011",
"111011110111011",
"111F11111111111",
]
l2=[
"1I1111111111111",
"101111000000001",
"100000011111111",
"111111011011101",
"111111000000001",
"111110111011111",
"100000001011111",
"111110111011111",
"111000000011001",
"111011111111101",
"111000000000001",
"111010110111011",
"111010010111011",
"111011110111011",
"111011111111111",
"111000000000001",
"111010110111011",
"111010010001011",
"111011110101011",
"1111111111F1111",
]
l3=[
"1I11111111111111111111111111",
"1011110000000001111000000001",
"1000000111111100000011111111",
"1111110110111011111011011101",
"1111110000000011111000000001",
"1111101110111111110111011111",
"1000000010111100000001011111",
"1111101110111111110111011111",
"1110000000110011000000011001",
"1110111111111011011111111101",
"1110000000000011000000000001",
"1110101101110111010110111011",
"1110100101110111010010111011",
"1110111101110111011110111011",
"1110111111111111011111111111",
"1110000000000011000000000001",
"1110101101110111010110111011",
"1110100100010111010010001011",
"1110111101010111011110101011",
"11111111111111111111111F1111",
]
l4=[
"11I11111111111111111111111111111111111111111111111111",
"11011110001101111111111111111111100010111111110000001",
"11000000111100010000000000000111101110000000010101101",
"11011111111101111011011011111011101110111011010111101",
"11000000000001111011011000010000001110111011000001101",
"11101111111101111111011011101111101110111011111101111",
"11101111111101111011011011000100000000111011111101111",
"11100000001101111011011011011111111110111011111100001",
"11101111101101111011011011011111111110110011111101101",
"11100001101101111011011000000001111110110111111101101",
"11101101101101111011011111111101111110111011111111101",
"11101101101101111011000000000101111110111000000001101",
"11101101101101111011011011011100000000111011111101101",
"11101100101101111011011111011101111111111011111101101",
"11101110101101111011011010001101000000011011111101101",
"11101110001101111011011011011101011111011000000101101",
"11101111101101111011011011010111010000010111111101101",
"11100000011101111011011011110111011111110111011111101",
"11111111000000000000000000000000000000000000000000101",
"111111111111111111111111111111111111111111111111111F1",
]

#por ultimo se define si se quiere recorrer o no el laberinto
recorrer = True

l = laberinto(l1)
if recorrer == False:
    while not l.Finalizado():
        l.Avanzar()
else:
    plt.ion()
    l.Pintar()
    plt.draw()
    while not l.Finalizado():
        l.Avanzar()
        plt.clf()
        l.Pintar()
        plt.draw()
        plt.pause(0.01)
    print("ya esta")
    plt.ioff()
l.Pintar()
plt.show()
