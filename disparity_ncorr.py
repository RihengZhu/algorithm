

def hoare_partition(A,p,r):
    x=A[p]
    i=p
    j=r
    while True:

        while A[j]>=x :
            if j>=1:
                j-=1
            else:
                break
        while A[i]<=x :
            if i<=(r-1):
                i+=1
            else:
                break
        if i<j:
            A[i],A[j]=A[j],A[i]
        else:
            A[p], A[j] = A[j], A[p]
            return j
def quicksort(A,p,r):
    if p<r:
        q=hoare_partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
lst=[13,19,9,5,12,8,7,4,11,2,6,21]
result=quicksort(lst,0,len(lst)-1)
print(lst)


