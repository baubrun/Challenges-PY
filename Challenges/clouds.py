"""
Emma is playing a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.

She must avoid the thunderheads.

Determine the minimum number of jumps it will
take Emma to jump from her starting position to the last cloud.
It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if
they are safe or 1 if they must be avoided.

For example c = [0,1,0,0,0,1,0],  indexed from 0...6.
The number on each cloud is its index in the list so she must avoid
the clouds at indexes 1 and 5.

She could follow the following two paths: 0-2-4-6 or 2-3-4-6 .
The first path takes 3 jumps while the second takes 4.

***
    She can jump on any cloud having a number
    that is >= current cloud + 1 or 2.
***

"""
s = [0, 1, 0, 0, 0, 1, 0]


# start with edge cases the 2 ifs



def clouds(c):
    jumps = 0
    pos = 0
    n = len(c)
    end = n - 1
    while pos <= n:
        if pos == end:
            return jumps
        if pos == end - 1:
            jumps += 1
            return jumps
        else:
            if c[pos + 2] == 0:
                jumps += 1
                pos += 2
            else:
                jumps += 1
                pos += 1
ans = clouds(s)
print("Num jumps:", ans)

