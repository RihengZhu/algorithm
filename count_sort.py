import numpy as np

def  count_sort(A,B,min_value,max_value):
    C=np.zeros((max_value-min_value+1),dtype=int)
    for i in range(len(A)):
        C[A[i]]=C[A[i]]+1
    for i in range(1,len(C)):
        C[i]=C[i]+C[i-1]
    for j in range(len(A)):
        B[C[A[j]]-1]=A[j]
        C[A[j]]=C[A[j]]-1
lst=[2,5,3,0,2,3,0,3]
B=np.zeros(len(lst),dtype=int)
result=count_sort(lst,B,min(lst),max(lst))
print(B)