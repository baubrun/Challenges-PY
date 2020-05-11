"""
Don't Roll Doubles!
John is playing a dice game. The rules are as follows.

Roll two dice.
Add the numbers on the dice together.
Add the total to your overall score.
Repeat this for three rounds.
But if you roll DOUBLES, your score is instantly wiped to 0 and your game 
ends immediately!

Create a function which takes in a matrix as input, 
and return John's score after his game has ended.

Examples
diceGame([[1, 2], [3, 4], [5, 6]]) ➞ 21

diceGame([[1, 1], [5, 6], [6, 4]]) ➞ 0

diceGame([[4, 5], [4, 5], [4, 5]]) ➞ 27
"""


def diceGame(arr):
    s = 0
    l = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            l.append(arr[i][j])
            s += arr[i][j]
    for num in range(len(l) - 1):
        if l[num] == l[num + 1]:
            return 0
    return s


print(diceGame([
    [1, 2],
    [3, 4],
    [5, 6]
]))
print(diceGame([
    [1, 1],
    [5, 6],
    [6, 4]
]))
print(diceGame([
    [4, 5],
    [4, 5],
    [4, 5]
]))

