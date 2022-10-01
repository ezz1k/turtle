from turtle import *

def kwadrat(bok):
    pencolor("green")
    fillcolor("gold")
    begin_fill()
    for i in range(4):
        fd(bok); lt(90)
    end_fill()

def poziom(ile):
    for i in range(ile):
        kwadrat(30)
        fd(31)

setposition(-400,0)
poziom(20)
ht()
# zamyka okno po kliknięciu w nie myszką
exitonclick()