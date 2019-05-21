

class RBTreeNode():
    def __init__(self,x):
        self.key=x
        self.left=None
        self.right=None
        self.parent=None
        self.color="black"


class solution():
    def tree_minimum(self,x):
        while x.left !=None:
            x=x.left
        return x
    def leftroate(self,T,x):
        y=x.right
        x.right=y.left
        if y.left !=T.nil:
            y.left.parent=x
        y.parent=x.parent
        if x.parent==T.nil:
            T.root=y
        elif x==x.parent.left:
            x.parent.left=y
        else:
            x.parent.right=y
        y.left=x
        x.parent=y
    def rightrotate(self,T,x):
        y=x.right
        x.left=y.right
        if y.right !=T.nil:
            y.right.parent=x
        y.parent=x.parent
        if x.parent==T.nil:
            T.root=y
        elif x==x.parent.right:
            x.parent.right=y
        else:
            x.parent.left=y
        y.right=x
        x.parent=y
    def RBinsert(self,T,z):
        z.left=T.nil
        z.right=T.nil
        z.parent=T.nil
        y=T.nil
        x=T.root
        while x!=T.nil:
            y=x
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        z.parent=y
        if y==T.nil:
            T.root=z
        elif z.key<y.key:
            y.left=z
        else:
            y.right=z
        z.left=T.nil
        z.right=T.nil
        z.color='red'
        self.RBinsertfixup(T,z)
    def RBinsertfixup(self,T,z):
        while z.parent.color=='red':
            if z.parent==z.parent.parent.left:
                y=z.parent.parent.right
                if y.color=='red':
                    z.parent.color='black'
                    y.color='black'
                    z.parent.parent.color='red'
                    z=z.parent.parent
                else:
                    if z==z.parent.right:
                        z=z.parent
                        self.leftroate(T,z)
                    z.parent.color='black'
                    z.parent.parent.color='red'
                    self.rightrotate(T,z.parent.parent)
            else:
                y=z.parent.parent.left
                if y.color=='red':
                    z.parent.color='black'
                    y.color='black'
                    z.parent.parent.color='red'
                    z=z.parent.parent
                else:
                    if z==z.parent.left:
                        z=z.parent
                        self.rightrotate(T,z)
                    z.parent.color='black'
                    z.parent.parent.color='red'
                    self.leftroate(T,z.parent.parent)
        T.root.color='black'
    def RB_translate(self,T,u,v):
        if u.p==T.nil:
            T.root=v
        elif u==u.p.left:
            u.p.left=v
        else:
            u.p.right=v
        v.p=u.p
    def RBdelete(self,T,z):
        y=z
        y_original_color=y.color
        if z.left==T.nil:
            x=z.right
            self.RB_translate(T,z,z.right)
        elif z.right==T.nil:
            x=z.left
            self.RB_translate(T,)
        else:
            y=self.tree_minimum(z.right)
            y_original_color=y.color
            x=y.right
            if y.p==z:
                x.p=y
            else:
                self.RB_translate(T,)










