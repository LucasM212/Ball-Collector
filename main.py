import time
import random
x1=100
x2=100
y1=430
y2=25
y = 0
x = 240
score = 0
game_started = False

def setup():
    size(640, 480)
    
def draw():
    global score
    global x1,y1,x2,y2
    global x, y
    global game_started
    if keyCode == 32:
        game_started = True
    if game_started == True:
        background(0)
        text(score, 20, 255)
        fill(155)
        rect(x1, y1, x2, y2)
        fill(255)
        ellipse(x, y, 25, 25) 
        if y >= 640:
            y = 0
        y += 4 
        if (x >= x1 and x <= x1 + 100) and (y >= y1 and y <= y1 + 50):
            y = 0
            x = random.randint(0, 480)
            score += 10
        
        if y >= 480:
            fill(250,250)
            rect(20,160,600,120)
            textSize(100)
            fill(34,34,255)
            text("GAME OVER!",20, 255)
            textSize(20)
            fill(255)
            text("Press escape to exit",240, 130)
            time.sleep(1.5)
            try:
                if keyCode == 9:
                    sys.exit
            except:
                print("There was an error in closing the game.")
    else:
        fill(255,0,0)
        rect(140, 180, 380, 120)
        fill(0)
        textSize(30)
        text("PRESS SPACE TO BEGIN", 155, 270)    
        
 
def keyReleased():
    global x1, y1, x2, y2
    if (key==CODED):
        if (keyCode == LEFT):
            x1=x1-28
        elif (keyCode == RIGHT):
            x1=x1+28
