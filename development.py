x1=100
x2=100
y1=430
y2=25
y = 0
x = 240


def setup():
    size(640, 480)

def draw():
    background(0)
    global x1,y1,x2,y2
    global x, y
    fill(155)
    rect(x1, y1, x2, y2)
    fill(255)
    ellipse(x, y, 25, 25) 
    if y >= 640:
        y = 0
    y += 1 
    if (x >= x1 and x <= x + 100) and (y >= y1 and y <= y1 + 50):
        y = 0
    
    
    
        
 
def keyReleased():
    global x1, y1, x2, y2
    if (key==CODED):
        if (keyCode == LEFT):
            x1=x1-20
        elif (keyCode == RIGHT):
            x1=x1+20