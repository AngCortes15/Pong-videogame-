import turtle
#import winsound

wn = turtle.Screen()
wn.title("Ping pong by Angel")
wn.bgcolor("black");
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0;
score_b = 0;

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2 #Moves 1 pixeles
ball.dy = -0.2 #Moves to pixeles

# Pen
pen = turtle.Turtle()
pen.speed(0) #Animations speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador-1: 0 Jugador-2: 0", align="center", font=("Courier", 24, "normal"))
#Function
def paddle_a_up():
    y = paddle_a.ycor() #returns the coordinates
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor() #returns the coordinates
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor() #returns the coordinates
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor() #returns the coordinates
    y -= 20
    paddle_b.sety(y)
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w");
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
#Main game loop
while True:
    wn.update()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290: #Rebotar arriba
        ball.sety(290)
        ball.dy *= -1
        #Add sounds ! 
        #winsound.PlaySound("example.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290: #Rebotar abajo
        ball.sety(-290)
        ball.dy *= -1 #Rebotar
    if ball.xcor() >390: #Reiniciar
        ball.goto(0,0)
        ball.dx *= -1;
        score_a += 1
        pen.clear() #Limpiar pantalla de score
        pen.write("Jugador-1: {} Jugador-2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390: #Reiniciar
        ball.goto(0,0)
        ball.dx *= -1;
        score_b += 1
        pen.clear() #Actualizar score
        pen.write("Jugador-1: {} Jugador-2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collisions 
    #Paddle b (derecha)
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340);
        ball.dx *= -1
    #Paddle a (izquierda)
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340);
        ball.dx *= -1
        

