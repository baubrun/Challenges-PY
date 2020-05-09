"""
Harold is a kidnapper who wrote a ransom note,
but now he is worried it will be traced back to him through
his handwriting.

He found a magazine and wants to know
if he can cut out whole words from it and use them to
create an untraceable replica of his ransom note.

The words in his note are case-sensitive and he must
use only whole words available in the magazine.
He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note,
print Yes if he can replicate his ransom note exactly
using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn".
The magazine contains only "attack at dawn".
The magazine has all the right words, but there's a case mismatch.
The answer is NO.



checkMagazine has the following parameters:
magazine: an array of strings, each a word in the magazine
note: an array of strings, each a word in the ransom note

The first line contains two space-separated integers, m  and n,
the numbers of words in the magazine  and the note..

The second line contains m space-separated strings, each magazine[i] .
The third line contains n space-separated strings, each note[i].


use operations between dict Counter subtract
"""

magazine = "give me one grand today night"
# magazine = "two times three is not four"
# magazine = "ive got a lovely bunch of coconuts"
# magazine = "A bBb"

note = "give one grand today"
# note = "two times two is four"
# note = "ive got some coconuts"
# note = "A bBb ccc a"


from collections import Counter

def a(mag, note):
    right_words = Counter(note) - Counter(magazine) == {}
    if right_words:
        return print("Yes")
    print("No")



a(magazine, note)
