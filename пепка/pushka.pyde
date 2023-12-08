q=0

def setup():
    size(1000,1000)
    noStroke()
          
    
def draw():
    background(49,175,188)
    global q 
    
    fill(105,99,106)
    rect(0,450,200,250)
    
    if mouseButton == LEFT:
        ellipse(q,555,60,60) #пуля
        q=q+5      
    
    if q>=1000: 
                        
        fill(255,218,8)                
        ellipse(1010,555,400,400) #бах
         
    if q>=1040: 
       q=0
       
    fill(250,243,15)  
    ellipse(500,100,200,200)  
       

                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                              
