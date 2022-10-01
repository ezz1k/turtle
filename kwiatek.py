from turtle import *


def romb(dlugosc_boku, kolor_wypelnienia, kat_pierwszego_boku=135):
    """ Rysuje romb w kierunku zadanym zmienną kat_pierwszego_boku """
    setheading(kat_pierwszego_boku)
    fillcolor(kolor_wypelnienia)
    begin_fill()
    for i in range(4):
        fd(dlugosc_boku); rt(90)
    end_fill()


# początek
romb(120,"red")
setheading(270)
fd(100)
romb(40,"green",225)
romb(40,"green",45)
setheading(270)
fd(150)
ht()


# zamyka okno po kliknięciu w nie myszką
exitonclick()