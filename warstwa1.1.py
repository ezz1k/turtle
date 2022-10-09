from turtle import *
def kwadrat(bok,kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok); lt(90)
    end_fill()


def kafelek(bok):
    kwadrat(bok,"yellow")
    kwadrat(bok / 2,"purple")
    fd(bok/2); lt(90); fd(bok/2); rt(90)
    kwadrat(bok / 2,"purple")
    bk(bok/2); rt(90); fd(bok/2); lt(90)

ht()
kafelek(120)


exitonclick()