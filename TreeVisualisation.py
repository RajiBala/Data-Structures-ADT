import turtle

class visNode:
    #self.p = None

    turtle.home()
    curx= 0
    cury= 0
    turtle.setpos(curx,cury)
    
    def createnode(self):
        turtle.begin_poly()
        angle = 360/num
        for i in range(num):
            turtle.fd(dist)
            turtle.rt(angle)
            #turtle.fd(dist/2)
            #turtle.rt(angle)
        turtle.fillcolor("violet")
        turtle.end_poly()
        #self.p = turtle.get_poly()
        return(p)

    def createnode(self):
        #p= turtle.dot(30,"yellow")
        p = turtle.Turtle()
        p.shape("circle")
        p.color("blue")
        
        return(p)

    def createpoly(self,num, dist):
        turtle.begin_poly()
        angle = 360/num
        for i in range(num/2):
            turtle.fd(dist)
            turtle.rt(angle)
            turtle.fd(dist/2)
            turtle.rt(angle)
        turtle.fillcolor("violet")
        turtle.end_poly()
        p = turtle.get_poly()
        return(p)
        
    def drawnode1(self,e):
        p = createnode()
        #turtle.penup()
        turtle.write(e)
        turtle.penup()
        print

    # distance between nodes is proportional to 240/h or based on the maximum number of external node
    # extreme left point is 240 - dist/2, 240 can be replaced by maximum width of the last level
    #
    def drawnode(self, e, level, childno):
        curposy = 0
        if level == 0:
            curposx = 0
        else:
            dist = 240/(pow(2,level-1))
            curposx = -(240-dist/2)
            print "height", level, "dist", dist, "pos", curposx
            i=1
            while i<level+1:
                curposy = curposy-30
                i+=1
           
            i = pow(2,level)
            while (i<childno):
                curposx = curposx+dist
                i+=1
        print curposx, "#", curposy
        turtle.setpos(curposx,curposy)
        tpoly = self.createpoly(4,30)
        turtle.pendown()
        turtle.pen(fillcolor="black", pencolor="green", pensize=5)
        for pt in tpoly:
            turtle.setpos(pt)
        turtle.pen(fillcolor="black", pencolor="black", pensize=8)
        turtle.write(e)
        turtle.penup()


    def drawpoly(self, tpoly):
        turtle.pen(fillcolor="black", pencolor="green", pensize=5)
        for pt in tpoly:
            turtle.setpos(pt)
        

##def main():
##    turtle.home()
##    curx= 0
##    cury= 0
##    turtle.setpos(curx,cury)
##    drawnode(2,0,1)
##    #curx-=30
##    #cury-=30
##    #turtle.setpos(curx,cury)
##    drawnode(3,1,2)
##    #turtle.setpos(30,-30)
##    drawnode(4,1,3)
##    drawnode(5,2,4)
##    drawnode(6,2,5)
##    drawnode(7,2,6)
##    drawnode(8,2,7)
##    drawnode(9,3,8)
##    drawnode(10,3,9)
##    drawnode(11,3,10)
##    drawnode(12,3,11)
##    drawnode(13,3,12)
##    drawnode(14,3,13)
##    drawnode(15,3,14)
##    drawnode(16,3,15)
##    

##if __name__ == '__main__':
##    main()
