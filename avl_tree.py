class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.height=1
class AVL_Tree:
    def __init__(self):
        self.root=None
    def insert(self,root,key):
        if not root:
            return TreeNode(key)
        elif key<root.val:
            root.left=self.insert(root.left,key)
        else :
            root.right=self.insert(root.right,key)

        root.height= 1+ max(self.getheight(root.left),self.getheight(root.right))
        balance = self.getbalance(root)

        if balance >1 and key <root.left.val:
            return self.rightRotate(root)
        if balance <-1 and key>root.right.val:
            return self.leftRotate(root)
        if balance >1 and key>root.left.val:
            root.left=self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance <-1 and key< root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    def leftRotate(self,z):
        y=z.right
        T2=y.left
        #after 
        y.left=z
        z.right=T2

        z.height=1+max(self.getheight(z.left),self.getheight(z.right))
        y.height=1+max(self.getheight(y.left),self.getheight(y.right))
        return y
    def rightRotate(self,z):
        y=z.left
        T3=y.right
        #after
        y.right=z
        z.left=T3

        z.height=1+max(self.getheight(z.left),self.getheight(z.right))
        y.height=1+max(self.getheight(y.left),self.getheight(y.right))
        return y
    def getheight(self,root):
        if not root:
            return 0
        return root.height
    def getbalance(self,root):
        if not root:
            return 0
        return self.getheight(root.left)-self.getheight(root.right)
    def preorder(self,root):
        if not root:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

T=AVL_Tree()
root=None
root=T.insert(root,10)
root=T.insert(root,20)
root=T.insert(root,30)
root=T.insert(root,40)
root=T.insert(root,50)
root=T.insert(root,25)

T.preorder(root)
    