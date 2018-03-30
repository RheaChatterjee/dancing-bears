#Bears Can Do The Can Can 
###Featuring Valentine, Valentino, and Valentina the Dancing Bear Triplets! They are great at Can-Canning, but they tend to lose control when they start spinning! :D 

#Object instantiated = bear
#Additional light source = pointLight
#Object Animation = translation & rotation 

from shapes import *
from bear import *
add_library('minim')



time = 0   # use time to move objects from one frame to the next
timeStage = 0 #use to move the stage 
frameCounter = 0 #use to end the scene 
hatcount = 0  #use to move the hat 
transcount = 0 #use to move the bears off screen 
s = PShape()

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
    #stage object 
    global s 
    s = loadShape("stage.obj") #source: https://free3d.com/3d-model/stage-60639.html
    
    #background music  
    global sf 
    minim=Minim(this)
    sf=minim.loadFile("CanCan.mp3") #source: https://www.youtube.com/audiolibrary_download?vid=9da1ee78da162cb1
    sf.play()
    
def draw():
    global time
    global frameCounter 
    global timeStage
    global hatcount 
    global transcount
    time += 1
    frameCounter+= 1 

    camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position the virtual camera

    background (50,50,50)  # clear screen and set background to dark gray 
    
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(155, 155, 155)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    #ADDITIONAL LIGHT SOURCE 
    pointLight(51, 102, 110, 35, 40*sin(time/2.0), 36) 

    noStroke()
    specular (180, 180, 180)
    shininess (0.25)
    
    #move stage 
    if timeStage < 100:
        timeStage+=1
    camera (100-(timeStage), 0, 100, 0, 0, 0, 0, 1, 0)
    stage()

    
    #move hat 
    if time >=125 and time < 255: 
        if hatcount <= 100:
            camera(70.0, 35.0, 120.0, 50.0, 50.0, 0.0, 0.0, 1.0, 0.0)
            pushMatrix()
            translate(50, 100-(hatcount/5.0), 0)
            scale(2,2,2)
            rotateX(-PI/6)
            rotateY(PI/3)
            hat()
            popMatrix()
            hatcount+=1
            
    #bears kicking 
    if time >=175 and time < 900:
         camera (0, 0, 100, 0, 0, 0, 0, 1, 0)
         scaleFactor = 1.25
         changeFigure(0,0,0, 0.5,0.5,0.5, 0, 0, 0, True, time/2.0, scaleFactor)
    if time >=575 and time < 900:
        camera (0, 0, 100, 0, 0, 0, 0, 1, 0)
        scaleFactor = 1.25
        changeFigure(-40,0,0, 0.5,0.5,0.5, 0, 0, 0, True, time/2.0, scaleFactor)
    if time >=800 and time < 900: 
        camera (0, 0, 100, 0, 0, 0, 0, 1, 0)
        scaleFactor = 1.25
        changeFigure(40,0,0, 0.5,0.5,0.5, 0, 0, 0, True, time/2.0, scaleFactor)
        
    #bears spinning  
    if time >=900 and time < 1050: 
        camera (0, 0, 100, 0, 0, 0, 0, 1, 0)
        changeFigure(40,0,0, 0.5,0.5,0.5, 0, time/2.0, 0)
    if time >= 950 and time < 1050:
         camera (0, 0, 100, 0, 0, 0, 0, 1, 0)
         changeFigure(0,0,0, 0.5,0.5,0.5, 0, time/2.0, 0,)
    if time >= 1000 and time < 1050:
         camera (0, 0, 100, 0, 0, 0, 0, 1, 0)
         changeFigure(-40,0,0, 0.5,0.5,0.5, 0, time/2.0, 0)
    
    #bears leaving 
    if time >=1050 and time < 1185: 
        if transcount <= 200: 
            camera (0, 0, 100, 0, 0, 0, 0, 1, 0)
            changeFigure(0,-(transcount/3.0),0, 0.5,0.5,0.5, 0, time/2.0, 0,)
            transcount+=1
    if time >=1050 and time < 1185: 
        if transcount <= 400: 
            camera (0, 0, 100, 0, 0, 0, 0, 1, 0)
            changeFigure(-40-(transcount/3.0), 0, 0, 0.5,0.5,0.5, 0, time/2.0, 0,)
            transcount+=1
    if time >=1050 and time < 1185: 
        if transcount <= 400: 
            camera (0, 0, 100, 0, 0, 0, 0, 1, 0)
            changeFigure(40+(transcount/3.0),0,0, 0.5,0.5,0.5, 0, time/2.0, 0,)
            transcount+=1
   
    #end show      
    if frameCounter > 1185: 
            exit()
            

#create the stage                 
def stage(): 
    global s 
    fill(255,255,255)
    scale(5,-5,5)
    translate(1,-5,0)
    shape(s,0,0)
    
        