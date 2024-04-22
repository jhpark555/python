class Node:
    def __init__(self):
        self.value=Value 
        self.edges=[]
class Edges:
    def __init__(self,start,end):
        self.start=start
        self.end=end

def dfs(root):
    if root is None:
        return
    print(root.value)
    for edge in root.edges:
        dfs(edge.end)

def insert(root,value):
    if root is None:
        return Node(value)
    if value< root.value:
        root.left=insert(root.left)
    else :
        root.right=insert(root.right)
    return root

def delete(root,value):
    if root is None:
        return
    if value< root.value:
        root.left=delete(root.left,value)
    elif value> root.value:
        root.right = delete(root.right,value)
    else :
        if root.left is None:
            temp=root.right
            root.right=None
            return temp
        elif root.right is None:
            temp=root.left
            root.left=None
            return temp
        temp=minValueNode(root.right)
        root.value=temp.value
    return root

def bfs(root):
    if root is None:
        return
    queue=[root]
    while queue:
        node=queue.pop(0)
        print(node.value)
        for edge in node.edges:
            queue.append(edge.end)

def preorder_traversal(root):
    if root is None:
        return
    print(root.value)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.value)


    
