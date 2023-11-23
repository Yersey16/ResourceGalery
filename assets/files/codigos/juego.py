import turtle
import time
import random

posponer=0.1

#marcador
Score=0
High_Score=0

#configuracion de la ventana
wn=turtle.Screen()
wn.title("juego de snake")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

 #Cabeza
Cabeza=turtle.Turtle()
Cabeza.speed(0)
Cabeza.shape("square")
Cabeza.color("white")
Cabeza.penup()
Cabeza.goto(0,0)
Cabeza.direction = "stop"

#comida
comida=turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(100,100)

#cuerpo
segmento = []

texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0       High Score: 0",align="center",font=("Courier",24,"normal"))



#funciones
def arriba():
    Cabeza.direction="up"
def abajo():
    Cabeza.direction="down"
def izquierda():
    Cabeza.direction="left"
def derecha():
    Cabeza.direction="right"
def pausa():
    Cabeza.direction="stop"

def mov():
    if Cabeza.direction=="up":
        y=Cabeza.ycor()
        Cabeza.sety(y+20)
    if Cabeza.direction=="down":
        y=Cabeza.ycor()
        Cabeza.sety(y-20)
    if Cabeza.direction=="left":
        x=Cabeza.xcor()
        Cabeza.setx(x-20)
    if Cabeza.direction=="right":
        x=Cabeza.xcor()
        Cabeza.setx(x+20)

#teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
wn.onkeypress(pausa, "space")

while True:
    wn.update()

    #borde
    if Cabeza.xcor()>280 or Cabeza.xcor()< -290 or Cabeza.ycor() > 290 or Cabeza.ycor() < -290:
        time.sleep(1)
        Cabeza.goto(0,0)
        Cabeza.direction= "stop"

        #Esconder cuerpo
        for segmentos in segmento:
            segmentos.goto(2000,2000)
        
        #limpieza
        segmento.clear()
        #limpieza Marcador
        Score=0
        texto.clear()
        texto.write("Score: {}      High Score: {}".format(Score, High_Score),align="center",font=("Courier",24,"normal"))


    if Cabeza.distance(comida)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        comida.goto(x,y)

        Nseg=turtle.Turtle()
        Nseg.speed(0)
        Nseg.shape("square")
        Nseg.color("grey")
        Nseg.penup()
        segmento.append(Nseg)

        #marcador 
        Score += 10
        if Score > High_Score:
            High_Score = Score
        texto.clear()
        texto.write("Score: {}      High Score: {}".format(Score, High_Score),align="center",font=("Courier",24,"normal"))



    #animacion del cuerpo
    Tseg=len(segmento)
    for index in range(Tseg -1, 0, -1):
        x=segmento[index-1].xcor()
        y=segmento[index-1].ycor()
        segmento[index].goto(x,y)

    if Tseg>0:
        x=Cabeza.xcor()
        y=Cabeza.ycor()
        segmento[0].goto(x,y)

    mov()
    #colisiones cuperpo
    for segmentos in segmento:
        if segmentos.distance(Cabeza)<20:
            time.sleep(1)
            Cabeza.goto(0,0)
            Cabeza.direction= "stop"

            #Esconder cuerpo
            for segmentos in segmento:
                segmentos.goto(2000,2000)
        
            #limpieza
            segmento.clear()
            #limpieza Marcador
            Score=0
            texto.clear()
            texto.write("Score: {}      High Score: {}".format(Score, High_Score),align="center",font=("Courier",24,"normal"))




    time.sleep(posponer)