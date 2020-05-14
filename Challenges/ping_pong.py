"""
Ping Pong!
A game of table tennis almost always sounds like Ping! followed by Pong! 
Therefore, you know that Player 2 has won if you hear Pong! 
as the last sound (since Player 1 didn't return the ball back).

Given an array of Ping!, create a function that inserts Pong! 
in between each element. Also:

If win equals true, end the list with Pong!.
If win equals false, end with Ping! instead.

Examples
ping_pong(["Ping!"], true) 
➞ ["Ping!", "Pong!"]

ping_pong(["Ping!", "Ping!"], false) 
➞ ["Ping!", "Pong!", "Ping!"]

ping_pong(["Ping!", "Ping!", "Ping!"], true) 
➞ ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"]

Notes
You will always return the ball (i.e. the Pongs are yours).
Player 1 serves the ball and makes Ping!.
Return an array of strings.
"""

def ping_pong(arr, win):
    words = []
    for _ in range(len(arr)):
        words.append("Ping!")
        words.append("Pong!")
    if not win:
        words.pop()
        return words
    return words






print(ping_pong(["Ping!"], True))
print(ping_pong(["Ping!", "Ping!"], False))
print(ping_pong(["Ping!", "Ping!", "Ping!"], True))