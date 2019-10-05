xPos=40
yPos=50
xVers=+1
yVers=+1
zRac=265

def setup():
    size(900,500)
    
    
def draw():
    global xPos,yPos,xVers,yVers,zRac
    background("#00FF8A")
    ellipse(xPos,yPos,50,50)
    xPos=xPos+2.5*xVers
    yPos=yPos+2.5*yVers
    
    if xPos>width or xPos<0:
        xVers=xVers*(-1)
        fill(random(0,255),random(0,255),random(0,255))

    if yPos>height or yPos<0:
        yVers*=-1
        fill(random(0,255),random(0,255),random(0,255))
    
    rect(zRac,height-25,90,60)

def keyPressed():
    global zRac
    
    if (keyCode==RIGHT and zRac<width-80):
        zRac+=10
    elif (keyCode==LEFT and zRac>0):
        zRac-=10
    
def tocca(xPos,yPos,xR,yR):
    if yPos>height-25 and xPos+25>width-80 and width-25<width-80+height-25:
        return("true")
        
            
