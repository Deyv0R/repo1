import turtle as tr

s = tr.Screen()

tr.setup(800, 800)
s.bgcolor('#262626')
tr.pencolor('#540d6e')
tr.speed(3)
tr.tracer(100)
tr.pensize(1)
col = ('White', 'Blue', 'White', 'Blue')

for i in range(1):
    for n in range(400):
        tr.color(col[n%4])
        tr.circle(190-n/2,90)
        tr.left(80)
        tr.circle(190-n/2,90)
        tr.color(col[n%4])
    tr.left(30)
s.exitonclick()
#FF7F3F
#FBDF07
#89CFFD
#F94892 
