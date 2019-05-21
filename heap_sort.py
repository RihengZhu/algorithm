
def LEFT(i):
    return 2*i+1
def RIGHT(i):
    return 2*i+2
def max_heapify(A,i):
    l=LEFT(i)
    r=RIGHT(i)
    if l<= size and A[l]>A[i]:
        largest=l
    else:
        largest=i
    if r<=size and A[r]>A[largest]:
        largest=r
    if largest !=i:
        A[i],A[largest]=A[largest],A[i]
        max_heapify(A,largest)
A=[16,4,10,14,7,9,3,2,8,1]
size=len(A)-1
length=len(A)-1
def build_max_heap(A):
    for i in range(size//2,-1,-1):
        max_heapify(A,i)
result=build_max_heap(A)
print(A)
for i in range(length,0,-1):
    A[0],A[i]=A[i],A[0]
    size-=1
    max_heapify(A,0)
print(A)


