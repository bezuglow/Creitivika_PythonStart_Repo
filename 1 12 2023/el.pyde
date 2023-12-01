q=0

def setup():
    size(1000,1000)
    noStroke()   
    
   
   
    
def draw():
    background(49,175,188)
    
    
    fill(105,99,106)
    rect(0,450,200,250)
    ellipse(q,555,60,60)
   
     
    global q    
    q=q+5
