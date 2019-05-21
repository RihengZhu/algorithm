


class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return self.data
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    def __len__(self):
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter
    def insertToFront(self,data):
        if data is None:
            return None
        node = Node(data,self.head)
        self.head = node
        return node

    def append(self,data):

        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head

        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node
#test=LinkedList()
#test.append(1)
#test.append(2)
#test.append(3)
#test.append(4)
#test.append(5)
#test.insertToFront(6)
#print(test.__len__())
#print(test.head.data)
##################################
class ListNode():
    def __init__(self,data):
        self.data=data
        self.next=None
class unorderedlist():
    def __init__(self):
        self.head=None
    def isempty(self):
        return self.head==None
    def gethead(self):
        return self.head.data
    def add(self,data):
        if data==None:
            return None
        node=ListNode(data)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def append_num(self,data):
        node=ListNode(data)
        if self.head==None:
            self.head=node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=node


test1 = unorderedlist()
test1.append_num(1)
test1.append_num(2)
test1.append_num(3)
print(test1.head.data)


########
class OrderedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def search(self, item):
        stop = False
        found = False
        current = self.head
        while current is not None and not found and not stop:
            if current.getData() > item:
                stop = True
            elif current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def add(self, item):
        previous = None
        current = self.head
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        node = ListNode(item)
        if previous is None:
            node.getNext(current)
            self.head = node
        else:
            previous.setNext(node)
            node.setNext(current)
