import sys 
sys.stdin = open("crosswood.in")
sys.stdout = open("crosswood.out","w")
input = sys.stdin.readline

def count_crossings():
  n = int(input().strip())
  cow_positions = [-1] * 11 
  ans = 0 
  for _ in range(n):
    A,B = map(int, input().split())
    if cow_positions[A] != -1 and cow_positions[A] != B  : ans += 1 
    cow_positions[A] = B 


  return ans

print(count_crossings())