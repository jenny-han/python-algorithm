# 학생이름이 공백으로 구분된 문자열 A.
# 각 학생이 좋아하는 학생의 이름 리스트가 공백으로 구분된 문자열 주어짐
# 각 학생이 좋아하는 학생 1명이상. 내가 나를 좋아하는 경우는 없음
# 나를 좋아하는 학생이 많을 수록 내 인기도가 높음.
# 인기도가 같은 경우 이름기준으로 오름차순으로 출력

import sys
from collections import defaultdict

n = sys.stdin.readline().strip()
A = sys.stdin.readline().strip().split()
result = defaultdict(int)

for a in A:
    line = sys.stdin.readline().strip().split()
    for l in line:
        result[l] += 1
    if a not in result.keys() :
        result[a] = 0
        
# print(result)
# VALUES 오름차순 정렬, KEY 내림차순 정렬
d = sorted(result.items(), key= lambda x:x[0])
# print(d)
sorted_d = sorted(d, key=lambda x: x[1], reverse=True)
# for r in sorted(result)
# print(k,v in sorted_d)
for v in sorted_d:
    print(v[0], v[1])
#==========================================
### 두번째 코드
# import sys
# from collections import defaultdict

# n = sys.stdin.readline().strip()
# A = sys.stdin.readline().strip().split()

# # 정수형으로 초기화되는 딕셔너리 객체를 생성한다. 
# result = {name : 0 for name in A}

# # N을 사용해도되지만, A를 사용하여 순서대로 꺼내도록 하였다
# for _ in range(int(n)):
# 	# 한 줄씩 읽어 학생 이름 리스트로 분리한다
#     line = sys.stdin.readline().strip().split()
    
#     # 한 명씩 꺼내며 인기도를 더해준다
#     for l in line:
#         result[l] += 1

# sorted_d = sorted(result.items(), key=lambda x: (-x[1], x[0]))

# # 값을 출력한다.
# for v in sorted_d:
#     print(v[0], v[1])

#===================================
### 가장 짧고 성능이 좋았던 코드 !!
# 기본 딕셔너리, 리스트
# n = input()
# students = input().split()
# popularity = {name: 0 for name in students}

# for name in students:
#     likes = input().split()
#     for target in likes:
#         popularity[target] += 1

# for name, score in sorted(popularity.items(), key=lambda x: (-x[1], x[0])):
#     print(name, score)
