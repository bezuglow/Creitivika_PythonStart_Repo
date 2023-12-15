q=0

def setup():
    size(1000,1000)
    noStroke()
        
    
def draw():
    background(49,175,188)#небо
    global q 
    
    fill(105,99,106)
    rect(0,450,200,250)#пушка
    
    if mouseButton == LEFT:
        ellipse(q,555,100,100) #пуля
        q=q+9      
    
    if q>=1000: 
                        
        fill(255,218,8)                
        ellipse(1010,555,400,400) #бах
         
    if q>=1050: 
       q=0
       
    fill(250,243,15)  
    ellipse(500,100,200,200) #солнце 
       
    fill(255,255,255)  
    ellipse(190,200,200,140)       
    ellipse(270,200,207,140)  
    ellipse(800,200,145,146)
    ellipse(865,200,137,147)
