


"""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0


We define an hourglass in  to be a subset of values with indices falling 
in this pattern in 's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. 
Calculate the hourglass sum for every hourglass in arr, 
then print the maximum hourglass sum.



"""

"""print 2D array"""
# a = [[1, 2, 3], [4, 5, 6]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=" ")
#     print()


"""add elem of 2D array"""
# s = 0
# a = [[1, 2, 3], [4, 5, 6]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         s += a[i][j]
#     print()


"""create array size of row * col """
# row = 3
# col = 4
# a = [0] * row
# for i in range(row):
#     a[i] = [0] * col
# print(a)
"""lc version"""
# a = [[0] * col for i in range(row)]
# print(a)

""" diagonal"""
# row = 3
# col = 3

# a = [0] * row
# for i in range(row):
#     a[i] = [0] * col # create all 0
# print(a)

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][i] = 1 # diagonal
# print(a)


# ########################
#     arr = []

#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))

s = """1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
""".replace("\n", "")
sj = [int(i) for i in s.split(" ")]
arr = []
# slice at intervals
for n in range(0, len(sj), 6):
    arr.append(sj[n: n + 6])
# # print(a)



def hourglassSum(arr):
    hourglass_max = float("-inf")
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            current_glass = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + \
                        arr[i + 1][j + 1] + \
                        arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2] 
            hourglass_max = max(hourglass_max, current_glass)
    return hourglass_max

print(arr)

