'''
Problem
Implement a stack that stores integers, then write a program to process the commands given as input. There are a total of five commands:

1. `1 X`: Push the integer X onto the stack. (1 ≤ X ≤ 100,000)
2. `2`: If there is an integer in the stack, pop and output the top integer. If the stack is empty, output -1 instead.
3. `3`: Output the number of integers currently in the stack.
4. `4`: Output 1 if the stack is empty, otherwise output 0.
5. `5`: If there is an integer in the stack, output the top integer. If the stack is empty, output -1 instead.

Input
The first line contains the number of commands N. (1 ≤ N ≤ 1,000,000)

From the second line onward, each of the N lines contains one command.

At least one command that requires output will be given.

Output
For each command that requires output, print the result on a new line.


Example Input 1
9
4
1 3
1 5
3
2
5
2
2
5


Example Output 1
1
2
5
3
3
-1
-1

# 11 : 22 
n = int(input())
stack = []

for _ in range(n):
  command = input().split()
  if command[0] == "1":
    stack.append(int(command[1]))
  elif command[0] == "2":
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif command[0] == "3":
    print(len(stack))
  elif command[0] == "4":
    print(1 if not stack else 0)
  elif command[0] == "5":
    print(stack[-1] if stack else -1)
'''





'''
Problem
Your boss has asked you to add up a sequence of positive numbers to determine how much money your company made last year.

Unfortunately, your boss reads out numbers incorrectly from time to time.

Fortunately, your boss realizes when an incorrect number is read and says “zero”, meaning “ignore the current last number.”

Unfortunately, your boss can make repeated mistakes, and says “zero” for each mistake.

For example, your boss may say “One, three, five, four, zero, zero, seven, zero, zero, six”, which means the total is 7 as explained in the following chart:

Boss statement(s)	Current numbers	Explanation
“One, three, five, four”	1, 3, 5, 4	Record the first four numbers.
“zero, zero“	1, 3	Ignore the last two numbers.
“seven”	1, 3, 7	Record the number 7 at the end of our list.
“zero, zero”	1	Ignore the last two numbers.
“six”	1, 6	We have read all numbers, and the total is 7.
At any point, your boss will have said at least as many positive numbers as “zero” statements. If all positive numbers have been ignored, the sum is zero.

Write a program that reads the sequence of boss statements and computes the correct sum.

Input
The first line of input contains the integer K (1 ≤ K ≤ 100 000) which is the number of integers (including “zero”) your boss will say. On each of the next K lines, there will either be one integer between 1 and 100 (inclusive), or the integer 0.

Output
The output is one line, containing the integer which is the correct sum of the integers read, taking the “zero” statements into consideration. You can assume that the output will be an integer in the range 0 and 1 000 000 (inclusive).

Example Input 1
4
3
0
4
0

Example Output 1
0

Example Input 2
10
1
3
5
4
0
0
7
0
0
6

Example Output 2
7



def calculate_total(inputs):
  stack = []
  total = 0
  
  for input_val in inputs:
    if input_val == 0:
      if stack:
        stack.pop()
        
    else:
      stack.append(input_val)
  
  while stack:
    total+=stack.pop()

  return total

k = int(input())

inputs = []
for _ in range(k):
  inp = int(input())
  inputs.append(inp)

total = calculate_total(inputs)
print(total)
'''

"""

Problem

Parenthesis String (PS) consists of two parenthesis symbols ‘(’ and ‘)’ only. In parenthesis strings, some strings are called a valid PS (shortly, VPS). Let us give the formal definition of VPS. A single “( )” is a member of VPS, called the base VPS. Let x and y be a member of VPS. Then “(x)”, a VPS which encloses a VPS x with a single pair of parenthesis, is also a member of VPS. And xy, the concatenation of two VPS x and y, is a member of VPS. For example, “(())()” and ((()))” are all VPS, but “(()(”, “(())()))” and “(()” are not VPS. You are given a set of PS. You should decide if the input string is VPS or not. 

Input
Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Then PS’s are given in the following T lines one by one. The length of each PS is between 2 and 50, inclusively.

Output
Your program is to write to standard output. Print the result in each line. If the input string is a VPS, then print “YES”. Otherwise print “NO”. 

Example Input 1
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

Example Output 1
NO
NO
YES
NO
YES
NO

Example Input 2
3
((
))
())(()

Example Output 2
NO
NO
NO

"""

def is_valid_parenthesis_string(s):
  stack = []
  for c in s : 
    if c == '(':
      stack.append(c)
    elif c == ')':
      if not stack:
        return False
      stack.pop()
  return len(stack) == 0

def solve_problem(input_data):
  for s in input_data:
    print("YES" if is_valid_parenthesis_string(s) else "NO")

N = int(input())
input_data = []
for i in range(N) : 
  S = input()
  input_data.append(S)

solve_problem(input_data)
