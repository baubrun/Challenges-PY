"""
The Fizz Buzz test is a poplular interview question used to 
'help filter out the 99.5% of programming job candidates who can't seem to program their way out of a wet paper bag.'

Write a program that returns a list of all the numbers from 1 
to an interger argument. But for multiples of three use “Fizz” 
instead of the number and for the multiples of five use “Buzz”. 
For numbers which are multiples of both three and five use “FizzBuzz”
Example
fizzBuzz(10) ➞ [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']

fizzBuzz(15) ➞ [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
"""

def fizz_buzz(maximum):
    l = []
    for i in range(1, maximum + 1):
        w = ""
        if i % 3 == 0 :
            w += "Fizz"
        if i % 5 == 0:
            w += "Buzz"
        l.append(i) if not w else l.append(w)
    return l
            
print(fizz_buzz(15))