class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.parent=None
class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,key,value):
        new_node=Node(key,value)           
        if self.root is None:
            self.root=new_node           
            return
        current=self.root
        current.parent=current
        while current is not None:
            if key < current.key:
                if current.left is None:   
                    current.parent=current                 
                    current.left=new_node                    
                    return
                else :
                    current.parent=current
                    current=current.left
                #print('#',current.key,self.parent.key)
            else:
                if current.right is None:    
                    current.parent=current                
                    current.right=new_node                    
                    return
                else :
                    current.parent=current
                    current=current.right
                #print('@',current.key,self.parent.key)
        
    def search(self,key):
        if self.root is None:
            return
        current=self.root
        while current is not None:
            if key == current.key:
                return self.parent
            elif key< current.key:
                current=current.left
            else :
                current=current.right
        return None
    
    def _find_parent(self,key):
        if self.root is None:
            return
        current=self.root
        while current is not None:
            if key==current.key:
                print('$$$',current.parent.key,current.key)
                return current.parent
            if key< current.key:
                current=current.left
            else :
                current=current.right
       
                

    def delete(self,key):
        node_to_delete=self.search(key)
        if node_to_delete is None:
            return
        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete ==self.root:
                self.root=None
                return
            parent =self._find_parent(key)            
            if parent.left==node_to_delete:
                parent.left=None
            else:
                parent.right=None
        if node_to_delete.left is None or node_to_delete.right is None:
            if node_to_delete ==self.root:
                if node_to_delete.left is not None:
                    self.root=node_to_delete.left
                else :
                    self.root=node_to_delete.right
                return
            parent =self._find_parent(key)
            if node_to_delete.left is not None:
                if parent.left==node_to_delete:
                    parent.left=node_to_delete.left
                else :
                    parent.right=node_to_delete.right
                return
            else :
                if parent.left==node_to_delete:
                    parent.left=node_to_delete.right
                else :
                    parent.right=node_to_delete.right
                return
        if node_to_delete.left is not None and node_to_delete.right is not None:
            successor=self._find_successor(node_to_delete)
            node_to_delete.key=successor.key
            node_to_delete.value=successor.value
            parent=self._find_parent(successor.key)
            if parent.left==successor:
                parent.left=None
            else:
                parent.right=None
            return
    def preorder(self,node):
        current=node
        if current is None:
            return
        print(current.value)
        self.preorder(current.left)
        self.preorder(current.right)


x=BinarySearchTree()
x.insert(60,60)
x.insert(12,12)
x.insert(90,90)
x.insert(4,4)
x.insert(41,41)
x.insert(71,71)
x.insert(100,100)
x.insert(1,1)
x.insert(29,29)
x.insert(84,84)
x.insert(23,23)
x.insert(37,37)
#x.delete(100)
x._find_parent(29)
x.preorder(x.root)

        
