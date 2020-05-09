"""
/*
Clear the Fog
Create a function which returns the word in the string, 
but with all the fog letters removed. 
However, if the string is clear from fog, return "It's a clear day!".

Examples
clearFog("sky") ➞ "It's a clear day!"

clearFog("fogfogfffoooofftreesggfoogfog") ➞ "trees"

clearFog("fogFogFogffffooobirdsandthebeesGGGfogFog") ➞ "birdsandthebees"
Notes
There won't be any fog inside of any of the actual words 
(won't include the letters f, o or g).
Hidden words are always in lowercase.
*/
"""


import re

def clear_fog(string):
    good_string = re.search("[fog]", string)
    s = "".join(re.findall("[^fog]", string))
    return s if good_string is not None else "It's a clear day!"



# ans = clear_fog("fogfogfffoooofftreesggfoogfog")
ans = clear_fog("a")
print(ans)
