
# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
#-----game configuration----
screen = trtl.Screen()
screen.bgcolor("red")
trtl.color("green")
trtl.shape("turtle")
trtl.turtlesize(5)
font_setup = ("Arial", 20, "normal")
score = 0
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name:")
#-----initialize turtle-----
score_writer = trtl.Turtle()
score_writer.goto(-250, 250)
#-----game functions--------

#-----countdown writer-----
counter =  trtl.Turtle()
counter.goto(-230,250)
#-----game functions-----
# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global trtl

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, trtl, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, trtl, score)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <=0:
    counter.write("Time's Up", font=font_setup) 
    timer_up = True 
    manage_leaderboard() 
  else: 
    ...
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def turtle_clicked(x, y):
    if timer_up is False:
        trtl.penup()
        trtl.goto(rand.randint(-200,200),rand.randint(-200,200))
        trtl.pendown()
        update_score()
    else:
       trtl.hideturtle()
def update_score():
    global score
    score = score+1
    print("Score:", score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)
#-----events----------------
wn = trtl.Screen()
trtl.onclick(turtle_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
