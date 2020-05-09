"""
You are given an unordered array consisting of consecutive integers  
[1, 2, 3, ..., n] without any duplicates. 
You are allowed to swap any two elements. 
You need to find the minimum number of swaps required 
to sort the array in ascending order.



For example, given the array arr= [7,1,3,2,4,5,6]  we perform the following steps:

i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took 5 swaps to sort the array.


Function Description

Complete the function minimumSwaps in the editor below. 
It must return an integer representing the minimum number of swaps 
to sort the array.

minimumSwaps has the following parameter(s):

arr: an unordered array of integers

enumerate part-
temp[val - 1] = idx
idx: [0,1,2,3] => idx:[0,1,2,3]
arr: [4,3,1,2] => tmp:[2,3,1,0]

4-1=3  idx: 3
3-1=2  idx: 2
1-1=0  idx: 0
2-1=1  idx: 1

"""

def swp_min_2(l):
    count = 0
    temp = [0] * len(l)
    for idx, val in enumerate(l):
        temp[val - 1] = idx
    # check sort
    for i in range(len(l)):
        # i + 1 b/c constraint 1....n for ans
        if l[i] != i + 1:
            t = temp[i]
            l[i], l[t] = i + 1, l[i]
            temp[i] , temp[l[t] - 1] = i, t
            count += 1
    return count
                
                
# ans = swp_min_2([4,3,1,2])
ans = swp_min_2([2,3,4,1,5])
print(ans)
# swp_min_2([7,1,3,2,4,5,6])



