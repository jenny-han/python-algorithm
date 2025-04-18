# 특정 과목의 합을 통해 서류 전형의 합격 여부를 결정함. 어떤 과목이 서류 평가되는지는 모름. 
# 과목수와 공개된 과목들이 주어질때, 얻을 수있는 최소와 최대 점수 구하기.
# 과목 중복없음, 모두 수강과목에 포함되어있음.
# 
import sys;

# 수강한 과목수 n, 요구하는 과목수 m, 공개한 과목수 k 
n, m, k = map(int, sys.stdin.readline().split())

#  수강한 과목이름 s , 정수 점수 p / n줄
dict = {}

for _ in range(n) :
    line = sys.stdin.readline().rstrip().split()
    # 과목을 key로 점수 값을 저장
    dict[line[0]] = int(line[1])

sum = 0
# 공개한 과목이름 t / k줄
for i in range(k) :
    t = sys.stdin.readline().rstrip()
    sum += dict[t]
    # 이미 공개한 과목은 딕셔너리에서 삭제
    dict.pop(t)

# m개를 충족해야 함. m-k개의 점수를 더 합해야 함. 
min, max = sum, sum
score = sorted(dict.values())
for i in range(m - k) :
    min += score[i]
    max += score[-(i + 1)]

print(min, max)
