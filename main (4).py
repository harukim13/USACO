"""
Problem
Given two integers n and m, count the number of pairs of integers (a,b) such that 0 < a < b < n and (a2+b2+m)/(ab) is an integer.

Input
The input consists of T test cases. The number of test cases (T) is given in the first line of the input file. Each test case consists of a single line: each line contains the integers n and m. n is greater than 0 and does not exceed 100.

Output
For each test case, print the number of pairs (a,b) satisfying the given property, one per line.



Example Input 1
3
10 1
20 3
30 4

Example Output 1 
2
4
5
"""









'''
Problem
C major scale consists of 8 tones: c d e f g a b C. For this task we number the notes using numbers 1 through 8. The scale can be played ascending, from 1 to 8, descending, from 8 to 1, or mixed. Write a program that, given the sequence of notes, determines wether the scale was played ascending, descending or mixed.

Input
First and only line of input will contain 8 integers, from 1 to 8 inclusive. Each integer will appear exactley once in the input.

Output
In the first and only line of input print "descending" if the scale was played descending, "ascending" if the scale was played ascending and "mixed" if the scale was played mixed.

Example Input 1
1 2 3 4 5 6 7 8

Example Output 1  
ascending

Example Input 2
8 7 6 5 4 3 2 1

Example Output 2
descending

Example Input 3
8 1 7 2 6 3 5 4

Example Output 3
mixed


def check_scale(notes):
  if notes == list(range (1, 9)): 
    return "ascending"

  if notes == list(range(8,0,-1)):
    return "descending"

  if sorted(notes) == list(range(1,9)):
    return "mixed"

notes = [int(x) for x in input().split()]
print(check_scale(notes))


##https://usaco.org/index.php?page=viewproblem2&cpid=1083 

'''

cowphabet = input()
letter = input()

number_times = 1

for i in range(len(letter) - 1):
  if cowphabet.index(letter[i + 1]) <= cowphabet.index(letter[i]):
    number_times += 1

print(number_times)