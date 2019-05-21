import  numpy as np
## if the input is the integer use the max(value)+1 as the array
def bucket_sort(A):
    n=max(A)+1
    B=[[] for _ in range(n)]
    for data in A:
        index=int(data)
        B[index].append(data)
    for i in range(n):
        B[i].sort()
    index=0
    for i in range(n):
        for j in range(len(B[i])):

            A[index]=B[i][j]
            index+=1

    return A
lst=[5,4,3,6,5,3]
result=bucket_sort(lst)
##if the input is the decimal
def bucket_sort(A,n):
    B = [[] for _ in range(n)]
    for data in A:
        index = int(data*10)
        B[index].append(data)
    for i in range(n):
        B[i].sort()
    index = 0
    for i in range(n):
        for j in range(len(B[i])):
            A[index] = B[i][j]
            index += 1

    return A
lst1=[0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
n=len(lst1)
print(n)
result=bucket_sort(lst1,n)
print(lst1)