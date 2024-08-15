#https://usaco.org/index.php?page=viewproblem2&cpid=712
import sys

def usaco(f_name): 
    sys.stdin = open(f_name + ".in")
    sys.stdout = open(f_name+".out", "w")

usaco("circlecross")
input = sys.stdin.readline

crossings = input().strip()

start = [-1 for _ in range(26)]
end = [-1 for _ in range(26)]

for v, c in enumerate(crossings):
    c_id = ord(c) - ord("A")
    if start[c_id] == -1:
        start[c_id] = v
    else:
        end[c_id] = v

crossing_pairs = 0
for i in range(26):
    for j in range(26):
        crossing_pairs += start[i] < start[j] and start[j] < end[i] and end[i] < end[j]

print(crossing_pairs, file=sys.stdout)




# AA BB 
# BB AA 
# A BB A 
# B AA B 

# A B A B 
# B A B A 

