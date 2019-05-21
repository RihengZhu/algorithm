


class stack():
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def push(self,item):
        self.items.append(item)
    def pop_last(self):
        return self.items.pop()
s1=stack()
s2=stack()
for i in range(5):
    s1.push(i)
print(s1.items)
for j in range(len(s1.items)):
    s2.push(s1.pop_last())
lst=[]
for k in range(len(s2.items)):
    lst.append(s2.pop_last())
print(lst)