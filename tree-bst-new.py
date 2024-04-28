class Node:
    def __init__(self,data):
        self.data=data
        self.right_child=None
        self.left_child=None
class Tree:
    def __init__(self):
        self.root_node=None
    def find_min(self):
        curr=self.root_node
        while curr.left_child:
            curr=curr.left_child
        return curr
    def insert(self,data):
        node=Node(data)
        if self.root_node is None:
            self.root_node=node
            print('#',self.root_node.data)
        else:
            curr=self.root_node
            parent=None
            while True:
                parent=curr
                if node.data<curr.data:
                    curr=curr.left_child
                    if curr is None:
                        parent.left_child=node
                        return self.root_node
                else:
                    curr=curr.right_child
                    if curr is None:
                        parent.right_child=node
                        return self.root_node
    def get_node_with_parent(self,data):
        parent=None
        curr=self.root_node
        if curr is None:
            return (parent, None)
        while True:    
            if curr.data==data:
                return (parent,curr)
            if curr.data < data:
                parent=curr
                curr=curr.right_child
            else: 
                parent=curr
                curr=curr.left_child
        return (parent,curr)
    def remove(self,data):
        parent, node=self.get_node_with_parent(data)

        if parent is None and node is None:
            return False
        
        children_count=0
        if node.left_child and node.right_child :
            children_count=2
        elif node.left_child is None and node.right_child is None:
            children_count=0
        else :
            children_count=1

        if children_count ==0:
            if parent :
                if parent.right_child is node:
                    parent.right_child=None
                else:
                    parent.left_child =None
            else :
                self.root_node = None
        elif children_count==1:
            next_node= None
            if node.left_child:
                next_node=node.left_child
            else:
                next_node=node.right_child
            if parent:
                if parent.left_child is node:
                    parent.left_child=next_node
                else:
                    parent.right_child=next_node
            else:
                self.root_node=next_node
        else:    #children_count =2
            curr=node
            min_node=node.right_child
            while min_node.left_child:
                curr=min_node
                min_node=min_node.left_child
            node.data=min_node.data

            if curr.left_child==min_node:
                curr.left_child=min_node.right_child
            else:
                curr.right_child=min_node.right_child

        return self.root_node
    def search(self,data):
        curr=self.root_node
        while True:
            if curr is None:
                return None
            elif curr.data ==data:
                return curr.data
            elif curr.data > data :
                curr=curr.left_child
            else :
                curr=curr.right_child
            
    def inorder(self,root_node):
        current=root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

T=Tree()
r=T.insert(5)
r=T.insert(3)
r=T.insert(9)
r=T.insert(6)
r=T.insert(13)
r=T.insert(12)
#T.inorder(r)
r=T.remove(9)
T.inorder(r)
x=T.search(6)
print('$',x)


            



    

            

    