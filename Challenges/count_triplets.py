"""
You are given an array and you need to find number of tripets of indices (i,j,k) such that the
elements at those indices are in geometric progression for a given common ratio r and i < j < k.

For example, arr = [1,4,16,64]. If r=4 ,
we have [1,4,16] and [4,16,64] at indices (0,1,2) and (1,2,3) .

Function Description

Complete the countTriplets function in the editor below. It should return
the number of triplets forming a geometric progression for a given  as an integer.

countTriplets has the following parameter(s):

arr: an array of integers
r: an integer, the common ratio

Input Format

The first line contains two space-separated integers n and r,
the size of arr and the common ratio.
The next line contains n space-seperated integers arr[i].

Constraints

1 <= n <= 10^5
1 <= r <= 10^9
1 <= arr[i] <= 10^9

Output Format

Return the count of triplets that form a geometric progression.

Sample Input 0

4 2
1 2 2 4
Sample Output 0

2

Explanation
There are  triplets in satisfying our criteria,
whose indices are (0,1,3)  and (0,2,3)
-----------------
Sample Input 1

6 3
1 3 9 9 27 81
Sample Output 1

6

Explanation 1

The triplets satisfying are index (0,1,2) , (0,1,3) ,
(1,2,4) , (1,3,4) , (2,4,5)  and (3,4,5).
------------------
Sample Input 2

5 5
1 5 5 25 125
Sample Output 2

4


Explanation 2

The triplets satisfying are index (0,1,3), (0,2,3) , (1,3,4) , (2,3,4) .

"""

from collections import Counter


def count_triplets(arr, r):
    count = 0
    possibilites = {}
    combos = {}

    for num in arr:
        next_num = num * r

        if num in combos:
            count += combos[num]
            
        if next_num in combos:
            combos[next_num] = combos[next_num]
        else:
            combos[next_num] = 0

        if num in possibilites:
            combos[next_num]  += possibilites[num]

        if next_num in possibilites:
            possibilites[next_num] += 1
        else:
            possibilites[next_num] = 1
    return count



print(count_triplets([int(i) for i in "1 2 2 4".split()], 2))
print(count_triplets([int(i) for i in "1 3 9 9 27 81".split()], 3))
print(count_triplets([int(i) for i in "1 5 5 25 125".split()], 5))

