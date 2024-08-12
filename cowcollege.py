def solve_tuition():
  n = int(input())
  tuition = list(map(int, input().split()))

  tuition.sort()

  max_money = 0
  max_tuition = 0
  for i in range(n):
    curr_tuition = tuition[i] * (n - i)
    if curr_tuition > max_money:
      max_tuition = tuition[i]
      max_money = curr_tuition

  print(max_tuition, max_money)


solve_tuition()
