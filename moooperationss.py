import sys 
input = sys.stdin.readline

def cnt_moo(str):
  n = len(str)
  if n<3: return -1
  if 'MOO' in str: return n-3
  if ('MOM'in str) or ('OOO' in str) : return n-3+1
  if 'OOM' in str: return n-3+2
  return -1

N = int(input())

for i in range(N):
  s = input().strip() 
  cnt = cnt_moo(s)
  print(cnt)