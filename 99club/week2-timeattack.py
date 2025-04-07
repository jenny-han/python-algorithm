# 재현이가 잘못된 수를 부를 때마다 0을 외쳐서 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
# 첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)\
# 이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.


import sys
K = int(input())

line = []
results = []
for _ in range(K):
    line.append(sys.stdin.readline().rstrip('\n'))

# print(line)

for i in line:
    if i == '0' :
        if(len(results) > 0) :
            results.pop()
    else :
        results.append(int(i))

print(sum(results))

