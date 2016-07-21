#Paste in processing to work! Make sure you are in python mode!
def smiley(x,y):
    #face
    fill(255, 255, 0)
    ellipse(x, y, 200, 200)
    #eyes
    fill(0, 0, 0)
    ellipse(x-33, y-25, 15, 15)
    ellipse(x+27, y-25, 15, 15)
    #mouth
    arc(x, y+20, 100, 100, 0, PI)

def setup():
    size(1000, 1000)
def draw():
    if mousePressed:
        smiley(mouseX, mouseY)