#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
letters = ["a","b","c","d","e"]
letter = 0
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
  apple.write(letters[letter], font=("Arial", 74, "bold")) 
def fall():
  global letter
  for i in range(50):
    apple.sety(apple.ycor()-6)
  letter = letter + 1
apple.clear()
#-----function calls-----
draw_apple(apple)
wn.listen()
wn.onkeypress(fall(), letters[letter])
wn.mainloop()