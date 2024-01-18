# LinkedList class
#DARRI STUBER
from Node import Node

class LinkedList:
    def __init__(self):
        self._head = Node()
        self._tail = Node()
        self._curr = Node()
    
    #changes or returns where the pointers are pointing
    #we use these instead of normal getters/setters so folks don't mess with our pointers
    # here = a Node object
    #Below are given until isBeginning
    def setHead(self, here):
        self._head.link = here
    def getHead(self):
        return self._head.link
    def setTail(self, here):
        self._tail.link = here
    def getTail(self):
        return self._tail.link
    def setCurr(self, here):
        self._curr.link = here
    def getCurr(self):
        return self._curr.link
    
    def isEmpty(self): #last given
        if self.getHead() == None:
            return True
        return False
    
    def isBeginning(self): 
        return (self.getHead() == self.getCurr())
    
    def isEnd(self):
        if self.getTail() == self.getCurr():
            return True
        return False
    
    def goBeginning(self):
        self.setCurr(self.getHead())
    
    def goEnd(self):
        self.setCurr(self.getTail())
        
    def getSize(self):
        if self.isEmpty() == True:
            return 0
        elif self.getHead() == self.getTail(): 
            return 1
        temp = self.getHead()
        size = 0
        while temp != None:
            size += 1
            temp = temp.link
        return size    
    def getPos(self): #given by professor
        #returns the current position as a number
        if self.isEmpty():
            return -1
        elif self.getHead() == self.getCurr():
            return 0
        temp = self.getHead()
        pos = 0
        while temp != self.getCurr():
            pos += 1
            temp = temp.link
        return pos
    
    def setPos(self, pos):
    #loop through and move cur # of position times
        self.setCurr(self.getHead())
        for i in range (0, pos):
            self.setCurr(self.getCurr().link)
    def goNext(self):
        if self.isEmpty() == True:
            pass
        elif self.getTail() == self.getCurr():
            pass
        else:
            index = self.getPos()
            newIndex = index+1
            self.setPos(newIndex)
    
    def goPrev(self):
        #check for beginning
        #Check for end
        #get position
        #set position to 1-position
        if self.isEmpty() == True:
            pass
        elif self.getHead() == self.getCurr():
            pass
        else:
            index = self.getPos()
            newIndex = index-1
            self.setPos(newIndex)

    def getData(self):
        #return self.getCurr().data
        return self.getCurr()
    def setData(self, d):
        self.getCurr().data = d
    
    def insert(self, n):
        #insertAfter
        #inserts a new node, n, after the curr.link node
        if self.isEmpty() == True:
            #this is an empty list we are adding to therefore: 
            self.setHead(n) #head points to n
            self.setTail(n) #tail points to n
            self.setCurr(n) #current points to n
        else: 
            #first make the new node point to the one after current
            #n.link = self.getCurr().link
            self.setCurr(n)
            #now make current point to new node
            self.getCurr().link = n

            
    def append(self, n):
        if self.isEmpty() == True:
            #this is an empty list we are adding to therefore: 
            self.setHead(n) #head points to n
            self.setTail(n) #tail points to n
            self.setCurr(n) #current points to n
        else:    
            #inserts at the end of the existing list
            self.setCurr(self.getTail()) #curr points to previously existing last node
            #print(self.getData())
            self.getCurr().link = n #last node now points to new node
            self.setTail(n) #tail now points to new node (new last)
            self.setCurr(n) #curr now points to new node (new last)
    def insertBefore(self, n):
        # inserts before curr
        if self.isEmpty() == True:
            #this is an empty list we are adding to therefore: 
            self.setHead(n) #head points to n
            self.setTail(n) #tail points to n
            self.setCurr(n) #current points to n
        elif self.isBeginning():
            #we are at beginning of list
            n.link = self.getCurr()
            self.setHead(n)
            self.setCurr(n)
        else:
            self.goPrev() #moves curr one node back
            self.insert(n)
                    
            
    def remove(self):
        #removes the node at curr
        if self.isEmpty() == True:
            pass
        elif self.getTail() == self.getHead():
            self.setHead(None)
            self.setTail(None)
            self.setCurr(None)
        else:
            if self.getCurr() == self.getHead():
                self.setHead(self.getHead().link)
                self.setCurr(self.getHead())
            else:
                self.goPrev()
                self.getCurr().link = self.getCurr().link.link
           
    
    def copy(self): #given by professor
        #copies the list and returns a new list
        self.setCurr(self._head.link)
        temp = LinkedList()
        while self._curr.link != None:
            n = Node(self._curr.link.data)
            temp.append(n)
            self.setCurr(self._curr.link.link)
        return temp
    
    def __str__(self): #given by professor
        self.setCurr(self._head.link)
        s = ""
        while self._curr.link != None:
            s += str(self._curr.link.data)
            s += "  "
            self.setCurr(self._curr.link.link)
        return s
