# https://trinket.io/python/e415a253ef

from turtle import *
fillcolor("gold")
begin_fill()
for i in range(4):
  fd(100); rt(90)
end_fill()
pu(); bk(25); pd()
#trójkąt
fillcolor("tomato")
begin_fill()
for i in range(3):
   fd(150); lt(120)
end_fill()
pu(); fd(55); rt(90); fd(30); pd()
#kwadracik
fillcolor("grey")
begin_fill()
for i in range(4):
  fd(40); lt(90)
end_fill()

pu(); fd(20); pd(); lt(90); fd(40);
pu(); bk(20); lt(90); fd(20); bk(40); pd(); fd(40); ht();
# zamyka okno po kliknięciu w nie myszką
exitonclick()