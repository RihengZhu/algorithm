class PrioQueue:
    def __init__(self,elist=[]):
        self._elems=list(elist)
        if elist:
            self.buildheap()
    def is_empty(self):
        return not self._elems
    def buildheap(self):
        end=len(self._elems)
        for i in range(end//2,-1,-1):
            self.siftdown(self._elems[i],i,end)
    def enqueue(self,e):
        self._elems.append(None)
        self.shiftup(e,len(self._elems)-1)
    def shiftup(self,e,last):
        elems,i,j=self._elems,last,(last-1)//2
        while i>0 and e<elems[j]:
            elems[i]=elems[j]
            i,j=j,(j-1)//2
        elems[i]=e
    def dequeue(self):
        if self.is_empty():
            print("the queue is empty")
        elems=self._elems
        e0=elems[0]
        e=elems.pop()
        if len(elems)>0:
            self.siftdown(e,0,len(elems))
        print(elems)
        return e0
    def siftdown(self,e,begin,end):
        elems,i,j=self._elems,begin,begin*2+1
        while j<end:
            if j+1<end and elems[j+1]<elems[j]:
                j+=1
            if e<elems[j]:
                break
            elems[i]=elems[j]
            i,j=j,2*j+1
        elems[i]=e
lst=[1,2,3,4,5,6,7]

trse=PrioQueue(lst)
print(trse.dequeue())
