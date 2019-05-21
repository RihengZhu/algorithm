import  numpy as np


def randomized_select(A,p,r,i):
    if p==r:
        return A[p]
    q=randomized_partition(A,p,r)

    k=q-p+1
    if i==k:
        return A[q]
    elif i<k:
        return randomized_select(A,p,q-1,i)
    else:
        return randomized_select(A,q+1,r,i-k)
def randomized_partition(A,p,r):
    s=np.random.randint(p,r)
    A[r],A[s]=A[s],A[r]
    return partition(A,p,r)

def partition(A,p,r):
    x=A[r]
    sig=p-1
    for j in range(p,r):
        if A[j]<x:
            sig+=1
            A[j],A[sig]=A[sig],A[j]
    A[sig+1],A[r]=A[r],A[sig+1]
    return sig+1

lst=[2,8,7,1,3,5,6,4]
res=randomized_select(lst,0,len(lst)-1,2)
print(lst)
print(res)