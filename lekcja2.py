from turtle import *

# pencolor("red")
# fd(100)
# rt(90)
# fd(100)

def kwadrat(bok=100, wypelnienie="gray"):
    pencolor("gray")
    fillcolor(wypelnienie)
    begin_fill()
    for krok in range(4):
        fd(bok); lt(90)
    end_fill()

kwadrat(601,"darkmagenta")

# wstrzymuje zamnknięcie okna
# mainloop()
# done()

# zamyka okno po kliknięciu w nie myszką
exitonclick()