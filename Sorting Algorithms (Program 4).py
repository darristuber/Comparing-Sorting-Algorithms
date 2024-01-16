#DARRI STUBER
#CSC 201 DATA STRUCTURES AND ALGORITHM ANALYSIS
#PROGRAM 4
#JUST TO NOTE I USED 100 IN MY LISTS INSTEAD OF 5OO (WAS GETTING ERROR OF MAXIMUM RECURSION DEPTH REACHED) 

#use node and linked files
import random
from Node import Node
from LinkedList import LinkedList
import time

#build 6 lists
#list 1 is 50 random integers ranging from 1-49
list1 = LinkedList()
w = 1
while w <= 50:
    n = Node(random.randint(1,49))
    list1.append(n)
    w +=1
#list 2 50 integers in order 1-50
list2 = LinkedList()
for i in range(1,51):
    n = Node(i)
    list2.append(n)   
#list 3 is 50 integers in reverse order 50-1
list3 = LinkedList()
for i in range(1,51):
    n = Node(51-i)
    list3.append(n)
#print(list3)
#list 4 is 500 random integers from 1-999
list4 = LinkedList()
w = 1
while w <= 100:
    n = Node(random.randint(1,999))
    list4.append(n)
    w += 1 
#list 5 is 500 random integers in order (1-999)
list5 = LinkedList()
for i in range(1,100):
    n = Node(i)
    list5.append(n)
#list 6 is 500 int in reverse order 500-1
list6 = LinkedList()
for i in range(1,101):
    n = Node(101-i)
    list6.append(n)

def InsertionSort(linklist): #sorts by value
    #print (linklist)
    size = linklist.getSize() 
    linklist.goBeginning()
    linklist.goNext()
    while linklist.getPos() != size: #move through every value in list
        while linklist.getCurr() != None:  #move back with smaller value until we hit head or smaller value
            pos = linklist.getPos() #save position so we can move to the next once current node is sorted
            temp = linklist.getCurr().data #save original current node as temp variable
            linklist.goPrev()
            #curr now moved back
            before = linklist.getCurr().data #save previous node as before variable
            while int(temp) < int(before): #if the value at the current index is smaller than the value at the previous index   
                linklist.setData(temp) #set original before to original current
                linklist.goNext()
                linklist.setData(before) #set original current to original before
                linklist.goPrev() #moves curr back to continue sorting until the node is in the right place
                temp = linklist.getCurr().data
                if linklist.getCurr() == None:
                    break
                linklist.goPrev()
                before = linklist.getCurr().data   
            linklist.setCurr(linklist.getTail().link)
            
        linklist.setPos(pos+1) #move the position to the next spot to begin the list again
    return linklist

## OPTIMIZED BUBBLE SORT
    #inspired by bubble sort code on geeks for geeks
def bubbleSort(linklist):
    done = linklist.getSize()-1#getPos() +1
    end = done #for use in the loop
    linklist.goBeginning()#setCurr(linklist.getHead())
    round = 0 #linklist.getPos()
    
    while round <= end: #traverse through elements (may need to add a coutner)
        swapped = False
        #for each element in linklist
        while linklist.getPos() != done: #if the node we are about to sort has not already been sorted to the back
        #cycle the next biggest index through linklist until you have hit sorted data  
            temp = linklist.getCurr().data
            linklist.goNext()
            after = linklist.getCurr().data
            if temp >= after:
                linklist.setData(temp) #set after pos to temp
                linklist.goPrev() #go back to original curr
                linklist.setData(after) #set current pos to after
                linklist.goNext() #move current up
                swapped = True
            #if after is greater it becomes the next temp
        #we want to set done to the pos last sorted element (should move in increments of 1 as we proceed)   
        if swapped == False: #after this you can just put break - the if/else just shows if it is optimized or not
            if linklist.getPos() == done:
                break
            else:
                print('stopped early')
                break
        done -= 1 #we have sorted one more so the position of done moves up
        round += 1 #
        linklist.goBeginning()#set link list to get head to start again
    return linklist



## MERGE SORT
def mergeSort(linklist):
   
    size = linklist.getSize()
    if size > 1: #base case if the list is less than one we want to return it not recursify further
        mid = size//2 #find midpoint position
        linklist.goBeginning()
        right = LinkedList()
        left = LinkedList()
        
        for i in range (0,mid):
            node = Node(linklist.getCurr().data)
            left.append(node)
            linklist.goNext()
        
        for i in range (mid, size):
            node = Node(linklist.getCurr().data)
            right.append(node)
            linklist.goNext()
            
        left = mergeSort(left) #recurisfy until len(left is =1)
        right = mergeSort(right) #recurisfy until len(right is =1)
       
        left.goBeginning()
        right.goBeginning()
        
        sortlist = LinkedList()
        
        
        while (right.isEmpty() == False) and (left.isEmpty() == False): #while both arrays arent at the end
            #if left smallest value is smaller add to list
            if left.getData() < right.getData(): #if left is bigger add to end
                node = Node(left.getData())
                sortlist.append(node)
                left.remove()
            else: #add right smallest value to list
                node = Node(right.getData())
                sortlist.append(node)
                right.remove()
                
        #we have compared right/left sides until one is gone, check both sides to add any extra values to end of ll
        while left.isEmpty() != True:
            node = Node(left.getData())
            sortlist.append(node)
            left.remove()
        while right.isEmpty() != True:
            node = Node(right.getData())
            sortlist.append(node)
            right.remove()
    else:
        return linklist
    return sortlist


## QUICK SORT
def quickSort(linklist):
    size = linklist.getSize()
    if size >= 2: #base case if the list is less than one we want to return it not recursify further
        linklist.goBeginning()
        pivot = linklist.getCurr().data
        linklist.goNext() #we dont want to count the head of the linked list 
        lessThan = LinkedList()
        greaterThan = LinkedList()
        
        #add to less and greater than lists
        while linklist.isEnd() == False:
            node = Node(linklist.getData())
            if linklist.getData() < pivot:
                lessThan.append(node)
            else:
                greaterThan.append(node)
            linklist.goNext()
        
        linklist.goEnd() #we were missing the last value because the loop stops when it gets there
        node = Node(linklist.getData())
        if linklist.getData() < pivot:
            lessThan.append(node)
        else:
            greaterThan.append(node)
            linklist.goNext()
        if lessThan.isEmpty() == False:
            lessThan = quickSort(lessThan) #recurisfy until len(left is =1)
        if greaterThan.isEmpty() == False:
            greaterThan = quickSort(greaterThan)
        lessThan.goBeginning()
        greaterThan.goBeginning()
        
            
        if lessThan.isEmpty() == False:
            lessThan.goBeginning()
            while lessThan.isEnd() ==False:
                lessThan.goNext()
            node = Node(pivot)
            lessThan.goEnd()
            lessThan.append(node)

            if greaterThan.isEmpty() == False:
                lessThan.getTail().link = greaterThan.getHead()
                lessThan.setTail(greaterThan.getTail())
            return lessThan
        if lessThan.isEmpty() == True:
            node = Node(pivot)
            greaterThan.goBeginning()
            greaterThan.insertBefore(node)
            return greaterThan
              
    else: 
        return linklist
    
#print time for insertion sort on all lists (for now - at end save to file) 
all_lists = [list1, list2, list3, list4,list5,list6]
#my computer is old so i am only using lists 1-4
#all_lists = [list1, list2, list3, list4]


lines = []
num = 1
for l in all_lists:
    insertion_start = time.perf_counter()
    insertionlist = InsertionSort(l)
    insertion_end = time.perf_counter()
    insertion_time = 'Time for insertion sort on list {}: {:.4f} ms'.format(num, ((insertion_end - insertion_start)*1000))
    print (insertion_time)
    lines.append(insertion_time)
    num +=1
    
num = 1
for l in all_lists:
    bubble_start = time.perf_counter()
    bubblelist = bubbleSort(l)
    bubble_end = time.perf_counter()
    bubble_time = 'Time for bubble sort on list {}: {:.4f} ms'.format(num, (bubble_end - bubble_start)*1000)
    print (bubble_time)
    lines.append(bubble_time)
    num +=1
    
num = 1
for l in all_lists:
    merge_start = time.perf_counter()
    mergelist = mergeSort(l)
    merge_end = time.perf_counter()
    merge_time = 'Time for merge sort on list {}: {:.4f} ms'.format(num, (merge_end - merge_start)*1000)
    print (merge_time)
    lines.append(merge_time)
    num +=1
    
num = 1
for l in all_lists:
    quick_start = time.perf_counter()
    quicklist = quickSort(l)
    quick_end = time.perf_counter()
    quick_time = 'Time for quick sort on list {}: {:.4f} ms'.format(num, (quick_end - quick_start)*1000)
    print (quick_time)
    lines.append(quick_time)
    num +=1

#from geeks for geeks https://www.geeksforgeeks.org/writing-to-file-in-python/
with open('program4file.txt', 'w') as f:
    for line in lines:
        f.write(line + '\n')
with open('program4file.txt', 'r+') as file1:
    print(file1.read())