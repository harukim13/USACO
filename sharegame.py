#https://usaco.org/index.php?page=viewproblem2&cpid=891

import sys

sys.stdin = open("shell.in")
sys.stdout = open("shell.out",'w')

swap = int(input())
cases = [0,0,0]
shell_order = [0,1,2]
for i in range(swap):
  swap1, swap2, guesses = map(int, input().split())
  swap1 -= 1
  swap2 -= 1
  guesses -= 1

  shell_order[swap1], shell_order[swap2] =shell_order[swap2], shell_order[swap1]
  cases[shell_order[guesses]] += 1

print(max(cases))