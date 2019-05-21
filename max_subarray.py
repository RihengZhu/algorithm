import numpy as np
target=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
def find_max_subarray(lst,low,mid,high):
    sum = 0
    left_sum = -np.inf
    for i in range(mid, -1, -1):
        sum += lst[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    sum = 0
    right_sum = -np.inf
    for i in range(mid + 1, high+1):
        sum += lst[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    total = right_sum + left_sum
    return  max_left,max_right,total
def find_max_array(lst,low,high):
    if low == high:
        return(low,high,lst[low])
    else:
        mid=(low+high)//2
        print("left ")
        (left_low,left_high,left_sum)=find_max_array(lst,low,mid)
        (right_low, right_high, right_sum) = find_max_array(lst, mid+1, high)
        (sub_low, sub_high, sub_sum) = find_max_subarray(lst, low, mid,high)
        if left_sum>=right_sum and left_sum>=sub_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>=left_sum and right_sum>=sub_sum:
            return (right_low, right_high, right_sum)
        else:
            return (sub_low, sub_high, sub_sum)
start,end,total=find_max_array(target,low=0,high=len(target)-1)
print(total)
