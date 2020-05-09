"""
Given an array of integers, return indices of the two 
numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

storing complement in dict 
so when subtracting current number is the idx of its complement in
dict ....

"""


def two_sum(nums, target):
    d = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in d.keys():
            return d[complement], i
        else:
            d[nums[i]] = i

ans = two_sum([7, 11, 15, 2], 9)
print(ans)
