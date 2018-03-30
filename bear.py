from shapes import *

def changeFigure(transx, transy ,transz, scalex, scaley, scalez, rotatex, rotatey, rotatez, legMove = False, time = 0, scaleFactor = 0): 
    pushMatrix()
    scale(scalex, scaley, scalez)
    translate(transx, transy, transz)
    rotateX(rotatex)
    rotateY(rotatey)
    rotateZ(rotatez)
    figure(legMove, time, scaleFactor)
    popMatrix()
    

def figure(legMove=False, time=0, scaleFactor=0):
    ears()
    nose()
    eyes()
    head()
    body()
    arms()
    legs(legMove, time, scaleFactor)
    tail()
    hat()
    cane()
    
    
def ears():
    # right ear
    fill (255, 204, 153)
    pushMatrix()
    #rotateY(-time)
    translate (10, -30, 1)
    rotateY(PI/2.0)
    scale(0.35,0.75,0.75)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(3)
    popMatrix()
    
     # left ear
    fill (255, 204, 153)
    pushMatrix()
    #rotateY(-time)
    translate (-10, -30, 1)
    rotateY(PI/2.0)
    scale(0.35,0.75,0.75)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(3)
    popMatrix()

def nose():
     #snout
    fill (255, 204, 153)
    pushMatrix()
    #rotateY(-time)
    translate (0, -22, 10)
    rotateY(PI/2.0)
    rotateX(PI/2.0)
    scale(0.75,1.25,1.05)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(3)
    popMatrix()
    
    #nose 
    fill (0, 0, 0)
    pushMatrix()
    #rotateY(-time)
    translate (0, -22.5, 12)
    rotateY(PI/2.0)
    rotateX(PI/2.0)
    scale(0.75,1.25,1.05)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(0.75)
    popMatrix()
    
def eyes():
    # left eye
    fill (255, 255, 255)
    pushMatrix()
    #rotateY(-time)
    translate (-3, -26, 9)
    rotateY(PI/2.0)
    rotateX(PI/2.0)
    scale(0.75,1.25,1.5)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(1)
    popMatrix()
    
    #right eye
    fill (255, 255, 255)
    pushMatrix()
    #rotateY(-time)
    translate (3, -26, 9)
    rotateY(PI/2.0)
    rotateX(PI/2.0)
    scale(0.75,1.25,1.5)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(1)
    popMatrix()
    
    #left pupil
    fill (0, 0, 0)
    pushMatrix()
    #rotateY(-time)
    translate (-3.35, -25.65, 9.5)
    rotateY(PI/2.0)
    rotateX(PI/2.0)
    scale(0.75,1.25,1.5)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(0.55)
    popMatrix()
    
    #right pupil
    fill (0, 0, 0)
    pushMatrix()
    #rotateY(-time)
    translate (3.35, -25.65, 9.5)
    rotateY(PI/2.0)
    rotateX(PI/2.0)
    scale(0.75,1.25,1.5)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(0.55)
    popMatrix()
    
def head():
    # head
    fill (102, 51, 0)
    pushMatrix()
    #rotateY(-time)
    translate (0, -25, 0)
    scale(1,1.05,1)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(10)
    popMatrix()

def body():
    # body
    fill (102, 51, 0)
    pushMatrix()
    #rotateY(-time)
    scale(1.05,1.35,1)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(13.25)
    popMatrix()
    
    # body
    fill (255, 204, 153)
    pushMatrix()
    #rotateY(-time)
    translate(0,0,2.75)
    scale(1.05,1.35,1)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(11)
    popMatrix()

def hat(): 
    #brim
    fill (0, 0, 0)
    pushMatrix()
    translate (0, -32, 0)
    #rotateY (-time)
    rotateX(PI/2.0)
    scale (10, 10, 0.25)
    cylinder()
    popMatrix()
    
    #top
    fill (0, 0, 0)
    pushMatrix()
    translate (0, -38, 0)
    #rotateY (-time)
    rotateX(PI/2.0)
    scale (6, 6, 5)
    cylinder()
    popMatrix()
    
def arms(): 
    fill (102, 51, 0)
    pushMatrix()
    translate(0,-5,0)
    #rotateY(-time)
    rotateX(PI/3.0)
    scale(7,2,2)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(3)
    popMatrix()
    
def legs(legMove,time, scaleFactor): #when leg move is true, move the left leg up with center at the top 
    #left leg
    if (legMove == False):  
        fill (102, 51, 0)
        pushMatrix()
        translate(-7,15,0)
        rotateX(PI)
        scale(2,5.5,2)
        sphereDetail(60)  # this controls how many polygons are used to make a sphere
        sphere(3)
        popMatrix()
    else: 
        #make changes to make it kick 
        fill (102, 51, 0)
        pushMatrix()
        rotateX(scaleFactor*sin(time/3.0))
        translate(-7,15,0)
        rotateX(PI)
        scale(2,5.5,2)
        sphereDetail(60)  # this controls how many polygons are used to make a sphere
        sphere(3)
        popMatrix()
    
    #right leg 
    fill (102, 51, 0)
    pushMatrix()
    translate(7,15,0)
    rotateX(PI)
    scale(2,5.5,2)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(3)
    popMatrix()
    
def tail(): 
    fill (102, 51, 0)
    pushMatrix()
    #rotateY(-time)
    translate (0, 8, -12)
    rotateY(PI/2.0)
    scale(1,1,1)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(2)
    popMatrix()

def cane(): 
    fill (250, 0, 0)
    pushMatrix()
    #rotateY (-time)
    translate (-16, 0, 4.5)
    rotateX(PI/2.0)
    scale (0.5, 0.5, 25)
    cylinder()
    popMatrix()
        