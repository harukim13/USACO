'''import sys

def usaco(f_name): 
    sys.stdin = open(f_name + ".in")
    sys.stdout = open(f_name+".out", "w")

#usaco("circlecross")
input = sys.stdin.readline

#https://usaco.org/index.php?page=viewproblem2&cpid=639

N = 4 

for i in range(N):
  for j in range(i+1, N):
      print(f"{i, j}")


'''


import sys

def usaco(f_name): 
    sys.stdin = open(f_name + ".in")
    sys.stdout = open(f_name+".out", "w")

usaco("diamond")

input = sys.stdin.readline
data = input().split()
n = int(data[0])
k = int(data[1])
diamond = [ int(input()) for _ in range(n)] 



most = 0

for x in diamond:
  fittable_ones = 0

  for y in diamond:
    if x <= y <= k + x:
      fittable_ones += 1

  most = max(most, fittable_ones)

print(most, file=sys.stdout)
