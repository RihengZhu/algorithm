


class Node():
    def __init__(self,data):
        self.data=data
        self.pre=None
        self.next=None
class doublelinklist():
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head == None

    def length(self):
            # 如果链表为空返回0
        if self.is_empty():
            return 0

        count = 1
        cur = self.__head

        while cur.next != self.__head:
            count += 1
            cur = cur.next

        return count

    def add(self,item):
        node=Node(item)
        node.next=self.head
        if not self.is_empty():
            self.head.prev=node
        self.head=node
    def append_item(self,item):
        node=Node(item)
        if self.is_empty():
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
            node.pre=cur
    def insert(self,pos,item):
        cur=self.head
        count=0
        if pos<=0:
            self.add(item)
        elif pos>self.length()-1:
            self.append_item(item)
        else:
            while  count<pos-1:
                count+=1
                cur=cur.next
            node=Node()
            node.next=cur.next
            cur.next.pre=node
            cur.next=node
            node.pre=cur
    def remove(self,item):
        if self.is_empty():
            return
        else:
            cur=self.head
            while cur !=None:
                if cur.data==item:
                    if not cur.prev:     ##head
                        if not cur.next:
                            self.head=None
                        else:
                            cur.next.pre=None
                            self.head=cur.next
                    else:
                        if cur.next:
                            cur.pre.next=cur.next
                            cur.next.pre=cur.pre
                        else:
                            cur.pre.next=None
                    break
                else:
                    cur=cur.next

