
def llistInsertSort(origList):
    #print(origList.data)
    if origList is None:
        return None
    
    newList=None
    while origList is not None:
        curNode= origList
        #print(curNode.data)
        origList =origList.next
        curNode.next=None
        newList=addToSortedList(newList,curNode)   
    curr=newList
    while curr is not None:
        print(curr.data)
        curr=curr.next    
       
        

def addToSortedList(newList,newNode):   
    pre=None
    curr=newList
    if curr is None:       
        newList=newNode
        #print(newList.data)
        return newList
    
    if newNode.data < curr.data:
        newNode.next=curr
        newList=newNode
        return newList
    
    while curr is not None and curr.data < newNode.data:
        pre=curr
        curr=curr.next
    newNode.next=curr
    pre.next=newNode
    return newList

"""
def addToSortedList(newList,newNode):   
    pre=None
    curr=newList
    if newNode.data < curr.data:
        newNode.next=curr
        newList=newNode
        return newList
    
    while curr is not None and curr.data < newNode.data:
        pre=curr
        curr=curr.next
    newNode.next=curr
    pre.next=newNode
    return newList

""" 


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(23)
b=Node(2)
c=Node(51)
d=Node(18)
e=Node(4)
f=Node(31)

a.next=b
b.next=c
c.next=d
d.next=e
e.next=f

#new=Node(15)

llistInsertSort(a)





