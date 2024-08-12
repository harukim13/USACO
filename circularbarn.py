import sys
sys.stdin = open("cbarn.in")
sys.stdout = open("cbarn.out","w")

def solve():
  room_num = int(sys.stdin.readline().strip())
  rooms = [int(sys.stdin.readline().strip()) for _ in range(room_num)]
  total_cows = sum(rooms)
  min_dist = float("INF")

  for unlock in range(room_num):
    dist = 0
    cows_left = total_cows
    for r in range(room_num):
      cows_left -= rooms[ (unlock + r) % room_num ] 
      dist += cows_left
    min_dist = min(min_dist, dist)

  print(min_dist, file = sys.stdout)

solve() 
