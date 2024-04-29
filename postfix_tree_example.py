
class Stack:
    def __init__(self):
        self.list=[]
        self.count=0
    def push(self,data):
        self.list.append(data)
        self.count +=1
    def pop(self):
        x=self.list.pop()
        return x
        
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.roght=None
    
    
expr = "4 5 + 5 3 - *".split()
print(expr)
stack=Stack()
for i in expr:
    if i in "+-*/":
        node =TreeNode(i)
        node.right=stack.pop()
        node.left=stack.pop()
    else:    
        node=TreeNode(int(i))
    print(node.data)
    stack.push(node)
    #print(i)
    
def calc(node):
    if node.data == "+":
        return calc(node.left)+calc(node.right)
    elif node.data == "-":
        return calc(node.left)-calc(node.right)
    elif node.data == "*":
        return calc(node.left)*calc(node.right)
    elif node.data == "/":
        return calc(node.left)/calc(node.right)
    else:
        return node.data

root=stack.pop()
r=calc(root)
print(r)