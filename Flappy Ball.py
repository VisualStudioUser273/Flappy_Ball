import pgzrun

WIDTH=800
HEIGHT=800
GRAVITY = 2000.00 #pixels per second 
class Ball():
    def __init__(self,initialx,initialy,radius,color):
        self.x=initialx
        self.y=initialy
        self.r=radius
        self.c=color
        self.vx = 200
        self.vy = 0



    def drawcircle(self): 
            screen.draw.filled_circle((self.x,self.y),self.r,self.c)


ball1=Ball(50,60,30,'Orange')


def draw():
    screen.fill(color='ForestGreen')
    ball1.drawcircle()



def update(dt):
     uy = ball1.vy
     ball1.vy += GRAVITY * dt    
     ball1.y += (uy + ball1.vy) *0.5* dt

     if ball1.x<0 or ball1.x>800:
          ball1.vx=-ball1.vx



                               
     if ball1.y>800:
          ball1.vy = -ball1.vy*0.9
          ball1.y=800


     ball1.x+= ball1.vx*dt          

    
def on_key_down(key):
     if key == keys.SPACE:
          ball1.vy = -500







            
pgzrun.go()    