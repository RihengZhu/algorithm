
class Node_build1():
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None
class Tree_build1:
    def __init__(self):
        self.root=None
    def add(self,item):
        node=Node_build1(item)
        if self.root==None:
            self.root=node
        else:
            q=[self.root]
            while True:
                pop_node=q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
    def traverse(self):
        if self.root==None:
            return None
        q=[self.root]
        res=[self.root.item]
        while q !=[]:
            pop_mode=q.pop(0)
            if pop_mode.left is not None:
                q.append(pop_mode.left)
                res.append(pop_mode.left.item)
            elif pop_mode.right is not None:
                q.append(pop_mode.right)
                res.append(pop_mode.right.item)
        return res
    def preorder(self,root):
        if self.root==None:
            return None
        result=[root.item]
        left_item=self.preorder(root.left)
        right_item=self.preorder(root.right)
        return result+left_item+right_item
    def inorder(self,root):
        if self.root is None:
            return []
        result=[root.item]




class Node_build2():
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None
class Tree_build2():
    def __init__(self):
        self.root=None
    def add_node(self,key,node=None):
        if node is None:
            node=self.root
        if self.root is None:
            self.root=Node_build2(key)

        else:
            if key<=node.key:
                if node.left is None:
                    node.left=Node_build2(key)
                    node.left.parent=node
                    return
                else:
                    return self.add_node(key,node=node.left)
            else:
                if node.right is None:
                    node.right=Node_build2(key)
                    node.right.parent=node
                    return
                else:
                    return self.add_node(key,node=node.right)


