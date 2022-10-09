from turtle import *
def kwadrat(bok,kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok); lt(90)
    end_fill()
def kafelek(bok):
    kwadrat(bok,"tomato")
    kwadrat(bok / 2,"olivedrab")

def warstwa(bok,ile):
    for i in range(ile):
        kafelek(bok); fd(bok)
    bk(bok*ile)
warstwa(60,3)
ht()

exitonclick()