

def quicksort(A,p,r):
    if 3<r-p:
        pre=median3(A,p,r)

        q=Partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
    else:
        insert_sort(A,p,r)
def Partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
def median3(A,p,r):
    center=(p+r)//2
    if A[p]>A[center]:
        max=A[p]
        sig=0
    else:
        max=A[center]
        sig=1
    if A[r]<max:
        if sig==0:
            A[r], A[p] = A[p], A[r]
        if sig==1:
            A[r], A[center] = A[center], A[r]


def insert_sort(A,p,r):
    for i in range(p+1,r+1):
        x=A[i]
        j=i
        while j>0 and A[j-1]>=x:
            A[j]=A[j-1]
            j=j-1
        A[j]=x

lst=[2,8,7,1,3,5,6,4]
a=quicksort(lst,0,len(lst)-1)
print(lst)



