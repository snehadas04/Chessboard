import turtle
sc = turtle.Screen()
cb = turtle.Turtle()

def draw():
    for i in range(4):
        cb.forward(30)
        cb.left(90)
    cb.forward(30)

if __name__ == "__main__" :
    sc.setup(400, 600)
    cb.speed(100)
    for i in range(8):
        cb.up()
        cb.setpos(-100,30*i)
        cb.down()