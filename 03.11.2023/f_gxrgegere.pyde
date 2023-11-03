

x=100
def setup():
    background(10)
    size(1000,1000)

def draw():
    
    rotate(radians(45))
    global x
    x=x+25
    fill(random(0,225)) 
    ellipse(x,100,60,random(60,160))
    
