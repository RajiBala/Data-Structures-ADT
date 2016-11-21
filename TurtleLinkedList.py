from node1 import *
import turtle
class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        
    def size(self):
        self.size=size
        print (self.size)

        
    def insertfirst(self,elem):
        new=node(elem)
        new.next=self.head
        self.head=new
        self.size=self.size+1
        print (self.head.data)

        
    def insertlast(self,elem):
        new=node(elem)
       #new.next=None
        self.tail.next=new
        self.tail=new
        new.next=None
        self.size=self.size+1
        print (self.tail)

        
    def first(self):
        if self.isempty()==1:
            print ("the list is empty")
        else:
            print ("first element is ")
            print (self.head.data)

            
    def last(self):
        p=self.head
        while p!=None:
            if p.next==None:
                print ("last element is ")
                print (p.data)
            p=p.next

            
    def removefirst(self):
        if self.isempty()==1:
            print ("list is empty")
        else:
            print ("the firstelement removed  is:",self.head.data)
            self.head=self.head.next
            self.size=self.size-1
            #n=node(self.head)
        
    #def removelast(self):
    def insertafter(self,p,elem):
        node1=self.head
        while(node1):
            if(node1.data==p):
                new=node(elem)
                x=node1.get_next()
                #new.data=elem
                new.next=x
                node1.next=new
                self.current=new
                break
            else:
                node1=node1.next
                self.size=self.size+1
        print ("the element",elem," is insertd after",p)


    def find(self,elem):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == elem:
               
                found = True
            else:
                current = current.get_next()
        if found==False:
            print ("false")
            print ("the element "),elem,("is not found")
        else:
             print ("true")
             print ("the element ",elem,"is found")
                
        
    def display(self):
        print("DISPLAY:")
        p=self.head
        while p.next!=None:
            print (p.data)
            p=p.next
        print (p.data)
        
    def isempty(self):
        if self.head==None:
            return 1
        else:
            return 0
        
    def remove(self,elem):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == elem:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        print ("the element ",elem,"is removed")

    def removeafter(self,elem):
         current = self.head
         found = False
         while current != None and not found:
             if current.get_data() == elem:
                 found = True
            
                 print ("the elemnt found is"),elem
             else:
                 current = current.get_next()
                
         if found==True:
             p=current.get_next()
             self.head=p.get_next()
             
             print ("the element is removed")
         else:
             print ("the element is not found")
    def disturtle(self):
        node1 = self.head
        i=0
        while (node1):
            if(node1.next!=None):
                i+=10
                turtle.goto(5*i,0)
            else:
                i+=10
                turtle.goto(5*i,0)
            turtle.pendown()
            turtle.write(node1.data)
            turtle.forward(30)
            turtle.left(90)
            turtle.forward(30)
            turtle.left(90)
            turtle.forward(30)
            turtle.left(90)
            turtle.forward(30)
            turtle.left(90)
            node1=node1.next
    def tutrremove(self,elem):
        node1 = self.head
        
        count=0
        while(node1):
            if(node1.next!=None):
                if(count==elem):
                    turtle.pendown()
                    turtle.forward(30)
                    turtle.pencolor("white")
                    turtle.left(90)
                    turtle.forward(30)
                    turtle.left(90)
                    turtle.forward(30)
                    turtle.left(90)
                    turtle.forward(30)
                    turtle.left(90)
                    turtle.penup()
                    turtle.pencolor("black")
                    node1=node1.next
                
                #turtle.goto(50*count,0)
            else:
                
                turtle.goto(50*count,0)
            turtle.penup()
            #turtle.write(node1.data)
            turtle.forward(30)
            turtle.left(90)
            turtle.forward(30)
            turtle.left(90)
            turtle.forward(30)
            turtle.left(90)
            turtle.forward(30)
            turtle.left(90)
            node1=node1.next
            count=count+1
        
        
        





m=linked_list()
print("*** insertfirst function is called***")
m.insertfirst(23)
m.insertfirst(24)
m.insertfirst(25)
m.insertfirst(26)
m.insertfirst(27)
m.insertfirst(28)
m.insertfirst(29)
m.display()
print ("*****list ends****")
print ("\n")
m.disturtle()
#turtle.reset()
print ("**** first() function called***")
m.first()
print ("\n")
print ("**** last() function called***")
m.last()
print ("\n")
print ("***find() function called***")
m.find(24)
print ("\n")
print ("***find() function called***")
m.find(50)
print ("\n")
print("*** remove() function is called***")
#m.remove(26)
m.tutrremove(3)
print ("\n")
m.display()
print ("****list ends****")
print ("\n")
print("*** removefirst() function is called***")
m.removefirst()
print ("\n")
#m.disturtle()
#turtle.reset()
print("*** insertafter() function is called***")
m.insertafter(25,25.5)
print ("\n")
m.display()
print ("****list ends****")
print ("\n")
#m.disturtle()
#turtle.reset()
turtle.exitonclick()
