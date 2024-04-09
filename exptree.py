class ExpressionTree:
    def __init__(self,expStr):
        self._expTree=None
        self._buildTree(expStr)
    def evaluate(self,varMap):
        return self._evaTree(self._expTree,varMap)
    def __str__(self):
        return self._buildString(self._expTree)
    def _buildString(self,treeNode):
        if treeNode.left is None and treeNode.right is None:
            return str(treeNode.element)
        else:
            expStr='(' 
            expStr +=self._buildString(treeNode.left)
            expStr +=str(treeNode.element)
            expStr +=self._buildString(treeNode.right)
            expStr +=')'
            return expStr
    def _evalTree(self,subtree,varDict):
        if subtree.left is None and subtree.right is None:
            if subtree.element >='0' and subtree.element <='9':
                return int(subtree.element)
            else :
                assert subtree.element in varDict,"Invalid variable"
                return varDict[subtree.element]
        else:
            lvalue=_evalTree(subtree.left,varDict)
            rvalue=_evalTree(subtree.right,varDict)
            return compute0p(lvalue,subtree.element,rvalue)
    def _compute0p(left,op,right):
        pass
    def _buildTree(self,expStr):
        expQ= Queue()
        for token in expStr:
            expQ.enqueue(token)

        self._expTree =_ExpTreeNode(None)
        self._recBuildTree(self._expTree,expQ)
    def _recBuildTree( self,curNode,expQ):
        token=expQ.dequeue()

        if token=='(' :
            curNode.left=_ExpTreeNode(None)
            buildTreeRec(curNode.left,expQ)

            curNode.data=expQ.dequeue()
            curNode.right=_ExpTreeNode(None)
            self._buildTreeRec( curNode.right, expQ)
            expQ.dequeue()

        else :
            curNode.element=token












class _ExpTreeNode:
    def __init__(self,data):
        self.element=data
        self.left=None
        self.right=None

        