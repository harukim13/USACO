cowphabet = input()
letter = input()

number_times = 1

for i in range(len(letter) - 1):
  if cowphabet.index(letter[i + 1]) <= cowphabet.index(letter[i]):
    number_times += 1

print(number_times)