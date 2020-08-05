from collections import Counter

def gameOfThrones(s):
    s = Counter(s)
    total = 0
    for k, v in s.items():
        total += v % 2
    
    if total > 1 :
        return "NO"
    return "YES"


