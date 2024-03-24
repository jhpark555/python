
class Node:
    def __init__(self,data):
        self.data=data
        self.right_child=None
        self.left_child=None

class Tree:
    def __init__(self):
        self.root_node=None
    def insert(self,data):
        node =Node(data)
        if self.root_node is None:
            self.root_node=node 
            return self.root_node
        else:
            current= self.root_node
            parent =None
            while True:
                parent=current
                if node.data<parent.data:
                    current=current.left_child
                    if current is None:
                        parent.left_child=node 
                        return self.root_node
                else:
                    current=current.right_child
                    if current is None:
                        parent.right_child=node 
                        return self.root_node

    def inorder(self,root_node):
        current=root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

    def search(self,data):
        current= self.root_node
        while True:
            if current is None:
                print("Item not found")
                return None
            elif current.data is data:
                print("Item found",data)
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

    def get_node_with_parent(self,data):
        parent= None
        current=self.root_node

        if current is None:
            return (parent,None)

        while True:
            if current.data ==data:
                return (parent,current)
            elif current.data>data:
                parent=current
                current=current.left_child
            else:
                parent=current
                current=current.right_child

        return (parent,current)


    def remove(self,data):
        parent, node=self.get_node_with_parent(data)
        #print(parent.data,node.data)
        if parent is None and node is None:
            return False

        children_count=0
        if node.left_child and node.right_child:
            children_count=2
        elif (node.left_child is None) and (node.right_child is None):
            children_count =0
        else:
            children_count =1 

        if children_count ==0:
            if parent:
                if parent.right_child is node:
                    parent.right_child=None
                else:
                    parent.left_child=None 
            else:
                self.root_node=None
        elif children_count==1:
            print("$$")
            next_node=None
            if node.left_child:
                next_node=node.left_child
            else:
                next_node=node.right_child
                #print("@",next_node.data)

            if parent:
                if parent.left_child is node:
                    parent.left_child=next_node
                else:
                    parent.right_child=next_node
                    #print("#",parent.right_child.data)
            else:
                self.root_node=next_node

        else: 
            parent_of_leftmost_node =node
            leftmost_node=node.right_child


            while leftmost_node.left_child:
                parent_of_leftmost_node=leftmost_node
                leftmost_node=leftmost_node.left_child


            node.data=leftmost_node.data    #swap
            #print("!",parent_of_leftmost_node.data,leftmost_node.data)

            if parent_of_leftmost_node.left_child==leftmost_node:
                parent_of_leftmost_node.left_child=leftmost_node.right_child
                #print("*",parent_of_leftmost_node.left_child)
            else:
                parent_of_leftmost_node.right_child=leftmost_node.right_child
                print("#",parent_of_leftmost_node.right_child.data)
        return self.root_node

    def find_min(self):
        current=self.root_node
        while current.left_child:
            current=current.left_child
        return current.data

    def find_max(self):
        current=self.root_node
        while current.right_child:
            current=current.right_child
        return current.data

class Minheap:
    def __init__(self):
        self.heap=[0]
        self.size=0
    def arrange(self,k):
        while k//2 >0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k],self.heap[k//2]=self.heap[k//2],self.heap[k]  #swap
            k //=2
    def insert(self,item):
        self.heap.append(item)
        self.size +=1
        self.arrange(self.size)
    def minchild(self,k):
        if k*2+1 > self.size:
            return k*2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k*2
        else:
            return k*2+1
        
    def sink(self,k):
        while k*2 <=self.size:
            mc = self.minchild(k)
            if self.heap[k]>self.heap[mc]:
                self.heap[k],self.heap[mc]=self.heap[mc],self.heap[k]
            k=mc
            #print(k)
    def delete_at_root(self):
        item=self.heap[1]
        self.heap[1]=self.heap[self.size]  #swap at the last
        self.size -=1
        self.heap.pop()
        self.sink(1)
        return item
    def delete_at_location(self,location):
        item=self.heap[location]
        self.heap[location]=self.heap[self.size]
        self.size -=1
        self.heap.pop()
        self.sink(location)
        return item
    def heap_sort(self):
        sorted_list=[]
        for node in range(self.size):
            n=self.delete_at_root()
            sorted_list.append(n)
        return sorted_list
            
        
        
        


tree=Tree()
r= tree.insert(5)
r= tree.insert(3)
r= tree.insert(9)
r= tree.insert(6)
r= tree.insert(13)
r= tree.insert(12)

tree.inorder(r)
print("**************")
r=tree.remove(9)
#tree.search(0)
tree.inorder(r)
x=tree.find_min()
y=tree.find_max()
#print("min:",x,"max:",y)

print("*******************")
h=Minheap()
#for i in (4,8,7,2,9,10,5,1,3,6):
#    h.insert(i)
    
#print(h.heap)
#n=h.delete_at_root()
#print(n)
#print(h.heap)
#n=h.delete_at_location(3)
#print(h.heap)
unsorted_list=[4,8,7,2,9,10,5,1,3,6]
for i in unsorted_list:
    h.insert(i)
print("Unsorted list:{}".format(unsorted_list))
print("Sorted list: {}".format(h.heap_sort()))









