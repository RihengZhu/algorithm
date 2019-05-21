


class loop_queue():
    def __init__(self,length):
        self.length=length
        self.Q=[None]*self.length
        self.tail=0
        self.head=0
    def enqueue(self,x):
        if (self.tail+1)%self.length==self.head :
            print("the queue is full")
        else:
            self.Q[self.tail]=x
            self.tail=(self.tail+1)%self.length


    def dequeue(self):
        if self.head==self.tail:
            print("the queue is empty")
        else:
            x=self.Q[self.head]
            self.Q[self.head]=None
            self.head=(self.head+1)%self.length
            return x
#q=loop_queue(15)
#print(q.Q)
#for i in range(10):
 #   q.enqueue(i)
#print(q.Q)


class queue1():
    def __init__(self,length):
        self.length=length
        self.head=0
        self.tail=1
        self.Q=[]
    def enqueue(self,x):
        if (self.tail==self.length):

            print("the queue is full")
        else:
            self.Q.append(x)
            self.tail=self.tail+1
    def dequeue(self):
        if self.head==self.tail:
            print("the queue is empty")
        else:
            out=self.Q[0]
            self.head=self.head+1
            self.Q.pop(0)

            return out
#use two queue built the stack
q1=queue1(5)
lst=[]
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q2=queue1(5)
for i in range(4):
    while len(q1.Q) != 1:
        q2.enqueue(q1.dequeue())
    print(q2.Q)
    print(q1.Q)
    lst.append(q1.dequeue())
    q1.Q, q2.Q = q2.Q, q1.Q
    q1.head = 0
    q1.tail = len(q1.Q)

    q2.tail = 0
    q2.head = 0
print(lst)
