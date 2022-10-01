from turtle import *

# pencolor("red")
# fd(100)
# rt(90)
# fd(100)

def draw_rectangle(fcolor):
    pencolor("green")
    fillcolor(fcolor)
    begin_fill()
    for krok in range(4):
        fd(200); lt(90)
    end_fill()

draw_rectangle("darkmagenta")

# wstrzymuje zamnknięcie okna
# mainloop()
# done()

# zamyka okno po kliknięciu w nie myszką
exitonclick()