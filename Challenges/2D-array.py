


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

s = """1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
""".replace("\n", "")



# create 2d array
sj = [int(i) for i in s.split(" ")]
arr = []
for n in range(0, len(sj), 6):
    arr.append(sj[n: n + 6])




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

