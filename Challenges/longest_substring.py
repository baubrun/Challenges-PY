"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not  a substring
"""

def length_of_longest_substring(s):
    i = 0
    j = 0
    longest = 0
    n = len(s)
    unique = set()
    while (j < n):
        if s[j] in unique:
            unique.remove(s[i])
            i += 1
        else:
            unique.add(s[j])
            longest = max(len(unique), longest)
            j += 1
    return longest


print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))
