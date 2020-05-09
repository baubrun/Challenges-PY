"""
You are given an unordered array consisting of consecutive integers  
[1, 2, 3, ..., n] without any duplicates. 
You are allowed to swap any two elements. 
You need to find the minimum number of swaps required 
to sort the array in ascending order.

"""
# # bubble sort
# a = [4,1,3,2]
# count = 0
# # starting from the back prevents indexError
# # while checking las elem
# for i in range(len(a) - 1, 0, -1):
#     for val in range(i):
#         if a[val] > a[val + 1]:
#             temp = a[val]
#             a[val] = a[val + 1]
#             a[val + 1] = temp
#             count += 1
#             print(a)
# print("count:", count)



"""
b/c idx is immutable 0,1,2,3,4 this will set your sorting comparisons

 a = [1,4,3,2]
 swap = 0
 for idx, val in enumerate(a):
     if idx != val - 1:
         swap += 1
         print("to swap:", val)

"""

"""

compare idx with val
if idx != val:
    treat val as idx to find next val

    if we come back to visited val:
        then there is a cycle
        get len of cycle
        num of swaps is len - 1
        do this for all cycles and sum them

"""
# def min_swap(a):
#     count_swap = 0
#     is_checked = [False] * len(a)
#     d = {val: idx for idx, val in enumerate(a)}
#     print("d:", d)


#     for k, v in sorted(d.items(), key=lambda x: x[0]):
#         if is_checked[k] or k == v:
#             continue

#         cycle_count = 0
#         v = k

#         while not is_checked[v]:
#             is_checked[v] = True
#             v = d[v]
#             cycle_count += 1

#         count_swap += cycle_count - 1
#     print("count_swap:", count_swap)

# a = [0,2,3,4,1,6,5]

# min_swap(a)

""" geeksforgeeks  enumerate(): (idx, val)"""
a = [4, 3, 2, 1]
n = len(a)
# Create two arrays and use
# as pairs where first array
# is element and second array
# is position of first element

# [(0, 0), (1, 2), (2, 3), (3, 4), (4, 1), (5, 6), (6, 5)]
arrpos = [*enumerate(a)]    # n = 7-1 = 6 ; create list with: [(idx, val)]
# print(arrpos)

# # [(0, 0), (4, 1), (1, 2), (2, 3), (3, 4), (6, 5), (5, 6)]
# # sort the array so that idx = position of next number
# #  0 is at pos 0, 4 is at pos 1 ...
# sort by val: [(val, idx)] to find pos of array
arrpos.sort(key=lambda x: x[1])
# print(arrpos)

# # keep track of visited elements
visited = {k: False for k in range(n)}
# print(visited)

ans = 0
for i in range(n):
    # # if swapped or in correct position
    if visited[i] or arrpos[i][0] == i:
        continue

    # find number of nodes
    # in this cycle and
    # add it to ans
    cycle_size = 0
    j = i

    # mark idx as visited
    while not visited[j]:
        visited[j] = True

        # move to next node, use that node to check dict
        j = arrpos[j][0]
        cycle_size += 1

    # update answer by adding
    # current cycle
    if cycle_size > 0:
        ans = + cycle_size - 1

print(ans)
