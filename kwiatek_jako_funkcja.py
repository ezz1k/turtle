from turtle import *


def romb(dlugosc_boku, kolor_wypelnienia, kat_pierwszego_boku=135):
    """ Rysuje romb w kierunku zadanym zmienną kat_pierwszego_boku """
    setheading(kat_pierwszego_boku)
    fillcolor(kolor_wypelnienia)
    begin_fill()
    for i in range(4):
        fd(dlugosc_boku); rt(90)
    end_fill()

def kwiatek(wspolzedna_x=0,wspolzedna_y=0,skala=1):
    """ Rysuje kwiatek w zadanym punkcie wedeeug zadanej skali """
    pu(); setposition(wspolzedna_x,wspolzedna_y); pd();
    romb(int(120*skala),"red")
    setheading(270)
    fd(int(100*skala))
    romb(int(40*skala),"green",225)
    romb(int(40*skala),"green",45)
    setheading(270)
    fd(int(150*skala))
    ht()

# testowe kwiatki
kwiatek(-350,0,0.1)
kwiatek(-300,0,0.2)
kwiatek(-150,0,0.5)
kwiatek(0,0,1)
kwiatek(300,0,1.5)


# zamyka okno po kliknięciu w nie myszką
exitonclick()