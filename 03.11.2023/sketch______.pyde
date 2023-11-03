e=500
r=-500
def setup():
    size(1000,1000)
     
    
    
def draw():
    global e
    e=e+5
   # r=r-500
    ellipse(e,500,60,60)    
    ellipse(500,e,60,60)
    ellipse(e,500,60,60)
    
