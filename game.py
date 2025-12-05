# create the floor
import turtle as trtl
import time

wn = trtl.Screen()
wn.bgcolor("black")
wn.setup(width=1250, height=1000)
brickfloor = "brick-floor.gif"
wn.addshape(brickfloor)
timer = 0
idle = "player1.gif"
punch1 = "player2.gif"
punch2 = "player4.gif"
punch3 = "player5.gif"
jump1 = "player6.gif"
crouch1 = "player8.gif"
fall1 = "player9.gif"
fall2 = "player10.gif"

wn.addshape(idle)
wn.addshape(punch1)
wn.addshape(punch2)
wn.addshape(punch3)
wn.addshape(jump1)
wn.addshape(crouch1)
wn.addshape(fall1)
wn.addshape(fall2)
floor = trtl.Turtle()
floor.penup()
floor.speed(0)
floor.shape(brickfloor)
player = trtl.Turtle()
player.penup()
playerhealth = 100
player.shape(idle)
player.goto(300,-115)
floor.goto(0,-320)
floor.stamp()
floor.hideturtle()
direction = ""
score = trtl.Turtle()
score.hideturtle()
score.speed(0)
score.color("white")
score.penup()
#create player
def punch():
    global player
    global cpuhealth
    player.shape(punch1)
    player.goto(player.xcor(), -115)
    for i in range(100):
        time.sleep(0.001)
    player.shape(punch2)
    if -100 < player.xcor()-cpu.xcor() < 100:    
        cpucrouch()        
    for i in range(100):
        time.sleep(0.001)
    if -120 < player.xcor()-cpu.xcor() < 120:
        if player.shape() == "crouch1":
            if -60 < player.xcor()-cpu.xcor() < 60:  
                cpuhealth = cpuhealth-10
        else:
            cpuhealth = cpuhealth-10
    player.shape(punch3)
    for i in range(100):
        time.sleep(0.001)
    player.shape(idle)
def left():
    global direction
    if -580 < player.xcor() < 581:
        player.shape(punch3)
        player.goto(player.xcor()-10,player.ycor())
        direction = "left"
        for i in range(5):
            time.sleep(0.01)
        player.shape(idle)
        direction = ""

def right():
    global direction
    player.goto(player.xcor(), -115)
    if -581 < player.xcor() < 580:
        player.shape(punch3)
        player.goto(player.xcor()+10,player.ycor())
        direction = "right"
        for i in range(5):
            time.sleep(0.01)
        player.shape(idle)
        direction = ""

def jump():
    global direction
    player.goto(player.xcor(), -115)
    if player.ycor() < -110:
        if direction == "":
            player.shape(jump1)
            player.goto(player.xcor(),player.ycor()+50)
            player.goto(player.xcor(),player.ycor()+50)
            player.goto(player.xcor(),player.ycor()-50)
            player.goto(player.xcor(),player.ycor()-50)
            player.shape(idle)
        if direction == "left":
            player.shape(jump1)
            player.goto(player.xcor()-50,player.ycor()+50)
            player.goto(player.xcor()-50,player.ycor()+50)
            player.goto(player.xcor()-50,player.ycor()-50)
            player.goto(player.xcor()-50,player.ycor()-50)
            player.shape(idle)            
        if direction == "right":
            player.shape(jump1)
            player.goto(player.xcor()+50,player.ycor()+50)
            player.goto(player.xcor()+50,player.ycor()+50)
            player.goto(player.xcor()+50,player.ycor()-50)
            player.goto(player.xcor()+50,player.ycor()-50)
            player.shape(idle)

def crouch():
    player.goto(player.xcor(), -115)
    if player.ycor() > -140:
        player.shape(crouch1)
        player.goto(player.xcor(), -141)
        time.sleep(0.1)
    player.goto(player.xcor(), -115)
    player.shape(idle)

#create cpu
cpu = trtl.Turtle()
cpu.penup()
cpu.shape(idle)
cpu.goto(-300,-115)
cpudirection = ""
cpuhealth = 100

def cpupunch():
    global cpu
    global playerhealth
    cpu.shape(punch1)
    cpu.goto(cpu.xcor(), -115)
    for i in range(100):
        time.sleep(0.001)
    cpu.shape(punch2)
    if -100 < cpu.xcor()-player.xcor() < 100:    
        cpucrouch()        
    for i in range(100):
        time.sleep(0.001)
    if -120 < cpu.xcor()-player.xcor() < 120:
        if player.shape() == "crouch1":
            if -60 < cpu.xcor()-player.xcor() < 60:  
                playerhealth = playerhealth-10
        else:
            playerhealth = playerhealth-10
    cpu.shape(punch3)
    for i in range(100):
        time.sleep(0.001)
    cpu.shape(idle)
def cpuleft():
    global cpudirection
    if -580 < cpu.xcor() < 581:
        cpu.shape(punch3)
        cpu.goto(cpu.xcor()-10,cpu.ycor())
        cpudirection = "left"
        for i in range(5):
            time.sleep(0.001)
        cpu.shape(idle)
        cpudirection = ""
def cpuright():
    global cpudirection
    if -581 < cpu.xcor() < 580:
        cpu.shape(punch3)
        cpu.goto(cpu.xcor()+10,cpu.ycor())
        cpudirection = "right"
        for i in range(5):
            time.sleep(0.001)
        cpu.shape(idle)
        cpudirection = ""
     
def cpujump():
    if cpu.ycor() < -110:
        if cpudirection == "":
            cpu.shape(jump1)
            cpu.goto(cpu.xcor(),cpu.ycor()+50)
            cpu.goto(cpu.xcor(),cpu.ycor()+50)
            cpu.goto(cpu.xcor(),cpu.ycor()-50)
            cpu.goto(cpu.xcor(),cpu.ycor()-50)
            cpu.shape(idle)
        if cpudirection == "left":
            cpu.shape(jump1)
            cpu.goto(cpu.xcor()-50,cpu.ycor()+50)
            cpu.goto(cpu.xcor()-50,cpu.ycor()+50)
            cpu.goto(cpu.xcor()-50,cpu.ycor()-50)
            cpu.goto(cpu.xcor()-50,cpu.ycor()-50)
            cpu.shape(idle)            
        if cpudirection == "right":
            cpu.shape(jump1)
            cpu.goto(cpu.xcor()+50,cpu.ycor()+50)
            cpu.goto(cpu.xcor()+50,cpu.ycor()+50)
            cpu.goto(cpu.xcor()+50,cpu.ycor()-50)
            cpu.goto(cpu.xcor()+50,cpu.ycor()-50)
            cpu.shape(idle)

def cpucrouch():
    if cpu.ycor() > -140:
        cpu.shape(crouch1)
        cpu.goto(cpu.xcor(), -141)
        time.sleep(0.1)
    cpu.goto(cpu.xcor(), -115)
    cpu.shape(idle)


wn.listen()
wn.onkeyrelease(punch, "space")
wn.onkey(left, "a")
wn.onkey(right, "d")
wn.onkeyrelease(jump, "w")
wn.onkey(crouch, "s")
while True:
    timer = timer + 0.01
    score.goto(cpu.xcor(), cpu.ycor()+100)
    score.write(cpuhealth, move=False, align='center', font=('Arial', 48, 'normal'))
    score.goto(player.xcor(), player.ycor()+100)    
    score.write(playerhealth, move=False, align='center', font=('Arial', 48, 'normal'))
    if (cpu.xcor()-player.xcor()) < -90:
        cpuright()
    elif (cpu.xcor()-player.xcor()) > 90:
        cpuleft()
    else:
        cpupunch()
    score.clear()
    if playerhealth < 1:
        player.shape(fall1)
        time.sleep(.3)
        player.shape(fall2)
        player.goto(player.xcor(), -162)
        score.write("Cpu Wins!", move=False, align='center', font=('Arial', 96, 'normal'))
        trtl.done()
    if cpuhealth < 0:
        cpu.shape(fall1)
        time.sleep(.3)
        cpu.shape(fall2)
        cpu.goto(cpu.xcor(), -162)
        score.write("Player Wins!", move=False, align='center', font=('Arial', 96, 'normal'))
        while True:
            user_input = trtl.textinput("enter your initials", "please enter 3 letters:")
            if len(user_input) == 3:
                break
            else:
                pass
        
        with open("scoreboard.txt", 'r+') as f:
            for line in f:
                if line[3:] < score:
                    f.write(input, timer)
                    break
                else:
                    f.write(input, timer)
                    pass
        trtl.done()
