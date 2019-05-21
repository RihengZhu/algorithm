



class treeNode():
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
        self.p=None
class Tree_new():
    def __init__(self):
        self.root=None
    def tree_insert(self,num):
        y=None
        x=self.root
        sig=0
        while x!=None:
            sig=1
            y=x
            z=treeNode(num)
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        if sig==1:
            z.p=y
        else:
            z=treeNode(num)
            z.p=y
        if y==None:
            self.root=z
        elif z.key<y.key:
            y.left=z
        else:
            y.right=z
    def tree_search(self,x,k):
        if x==None or k==x.key:
            return x
        if k<x.key:
            return self.tree_search(x.left,k)
        else: return self.tree_search(x.right,k)
    def tree_minimum(self,x):
        while x.left !=None:
            x=x.left
        return x
    def tree_maximum(self,x):
        while x.right !=None:
            x=x.right
        return x
    def tree_successor(self,x):
        if x.right !=None:
            return self.tree_insert(x.right)
        y=x.p
        while y!=None and x==y.right:
            x=y
            y=y.p
        return y
    def transplant(self,u,v):
        if u.p==None:
            self.root=v
        elif u==u.p.left:
            u.p.left=v
        else:
            u.p.right=v
        if v!=None:
            v.p=u.p

    def tree_delete(self,z):
        if z.left==None:
            self.transplant(z,z.right)
        elif z.right==None:
            self.transplant(z,z.left)
        else:
            y=self.tree_minimum(z.right)
            if y.p!=z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

test=Tree_new()
test.tree_insert(5)
test.tree_insert(2)
test.tree_insert(3)
test.tree_insert(4)
test.tree_insert(1)
test.tree_insert(6)