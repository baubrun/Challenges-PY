"""
/*
Removing Enemies
Remove enemies from the list of people, even if the 
enemy shows up twice.

Examples
print(remove_enemies(["Fred"], []) ➞ ["Fred"])

print(remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], 
["Emmy"]) )
➞ ["Adam", "Tanya"]

print(remove_enemies(["John", "Emily", "Steve", "Sam"], 
["Sam", "John"]) )
➞ ["Emily", "Steve"]
Notes
All names to be removed will be in the enemies list; 
simply return the list, 
no fancy strings.
*/

"""


def remove_enemies(names, enemies):
    if enemies == []:
        return names
    names.sort()
    enemies.sort()
    l1 = set(names)
    l2 = set(enemies)
    l3 = l1 | l2
    unique = []
    for i in sorted(l3):
        if i in l1:
            if i in l2:
                continue
            else:
                unique.append(i)
    return unique

print(remove_enemies(["Fred"], []))
print(remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], ["Emmy"]))
print(remove_enemies(["John", "Emily", "Steve", "Sam"], ["Sam", "John"]))
