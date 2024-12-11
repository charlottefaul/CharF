
import turtle

screen= turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('LightCyan')

t = turtle.Turtle()
t2 = turtle.Turtle()
t2.penup()
t2.hideturtle()
t.penup()


t.goto(0,100)
t.write("My Favorites",font=('arial',28,'bold'),align="center")



t.goto(0,-100)

t.write("Introduction",font=('arial',28,'bold'),align="center")

t2.goto(-100,0)
turtle.addshape('sushi.gif')
t2.shape('sushi.gif')
a = t2.stamp()
t2.goto(-100,0)

enter = input("Press enter to continue.")

t.clear()
t2.clear()
screen.bgcolor('lavender')

t.goto(0,100)
t.write("page 2",font=('arial',28,'bold'),align="center")

t.goto(0,-100)

t.write("My favorite foods are pasta, pizza, and sushi",font=('arial',28,'bold'),align="center")

enter = input("Press enter to continue.")

t.clear()
t2.clear()
screen.bgcolor('hotpink')

t.goto(0,100)
t.write("page3",font=('arial',28,'bold'),align="center")


t.goto(0,-100)

t.write("My favorite hobbies are running, drawing, shopping, and hanging out with friends",font=('arial',28,'bold'),align="center")

t2.goto(-100,0)
turtle.addshape('sushi.gif')
t2.shape('sushi.gif')
a = t2.stamp()
t2.goto(-100,0)

enter = input("Press enter to continue.")

t.clear()
t2.clear()
screen.bgcolor('plum')

t.goto(0,100)
t.write("page 4",font=('arial',28,'bold'),align="center")

t.goto(0,-100)

t.write("My favorite movie is Coraline",font=('arial',28,'bold'),align="center")

t2.goto(-100,0)
turtle.addshape('movie.gif')
t2.shape('movie.gif')
a = t2.stamp()
t2.goto(-100,0)

enter = input("Press enter to continue.")

t.clear()
t2.clear()
screen.bgcolor('tomato1')

t.goto(0,100)
t.write("page 5",font=('arial',28,'bold'),align="center")

t.goto(0,-100)

t.write("My favorite sport is Track",font=('arial',28,'bold'),align="center")

t2.goto(-100,0)
turtle.addshape('track.gif')
t2.shape('track.gif')
a = t2.stamp()
t2.goto(-100,0)

enter = input("Press enter to continue.")

t.clear()
t2.clear()
screen.bgcolor('SlateBlue')