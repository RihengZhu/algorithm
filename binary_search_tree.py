

class treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class operationtree():
    def __init__(self):
        self.root=None

    def insert(self,vale,node=None):
        if node==None:
            node = self.root
        if self.root==None:
            self.root=treenode(vale)

        else:

            if vale<node.val:
                if node.left==None:
                    node.left=treenode(vale)
                else:
                    node.left=self.insert(vale,node.left)
            elif vale>=node.val:
                if node.right==None:
                    node.right=treenode(vale)
                else:
                    node.right=self.insert(vale,node.right)
        return node
    def query(self,vale,node):
        if node==None:
            node=self.root
        if self.root==None:
            print(" the result is empty")
            return False
        else:
            if node.val == vale:
                print("find the value")
                return True
            elif vale < self.root.val:
                return self.query(vale,node.left)
            elif vale > self.root.val:
                return self.query(vale,node.right)
    def findmin(self,node=None):
        if node==None:
            node=self.root
            if node==None:
                print("the tree is empty")
                return None
        if node.left:
            return self.findmin(node.left)
        else:
            return node
    def delnode(self,val,node=None):
        if node==None:
            node=self.root
        if node==None:
            print("the tree is empty")
            return
        else:
            if node.val>val:
                node.left=self.delnode(val,node.left)
            elif node.val<val:
                node.right=self.delnode(val,node.right)

            else:
                if node.right and node.left:
                   tmp=self.findmin(node.right)
                   node.val=tmp.val
                   node.right=self.delnode(tmp.val,node.right)
                elif node.right==None and node.left==None:
                    node=None
                elif node.right==None:
                    node=node.left
                elif node.left==None:
                    node=node.right
        return node









op=operationtree()
op.insert(5)
op.insert(2)
op.insert(3)
op.insert(4)
op.insert(1)
op.insert(6)




