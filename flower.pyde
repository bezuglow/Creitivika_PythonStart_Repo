x=800
q=910
def setup():
     
    size(1000,1000)
    
    stroke(224,224,224)
    strokeWeight(40)
    fill(251,255,46)
    
def draw():
    global x,q
    background(131,255,246)
    push()
    stroke(0,255,27)
    line(500,910,500,x)             
      
    pop()
    
    ellipse(500,x,150,150)
    
    x=x-20
