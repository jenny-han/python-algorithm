# 드디어 컴파일 성공코드. 도움을 받았음.. 
# import sys
# input = sys.stdin.read
# data = input().split()

# N = int(data[0])
# index = 1

# results = []
# for _ in range(N):
#     s = data[index]
#     index += 1
#     idx = 0
#     for i, char in enumerate(s):
#         if char != '!':
#             idx = i
#             break
#     results.append(int(not ((idx % 2 == 0) == (s[-1] == '0'))))

# for result in results:
#     print(result)


## 코파일럿 추천 코드
# t = int(input())
# for _ in range(t):
#     s = input()
#     idx = 0
#     for i, char in enumerate(s):
#         if char != '!':
#             idx = i
#             break
#     print(int(not ((idx % 2 == 0) == (s[-1] == '0'))))

# 세번째. 틀렸대. 아마도 입력값이 한번에 들어가서 그런가봐. 
# t = int(input())

# for _ in range(t):
#     s = input().strip()
#     a = s.count('!')
#     n = int(s.replace('!', ''))
    
#     if n == 0:
#         result = 1 if a % 2 != 0 else 0
#     else:
#         result = 0 if a % 2 != 0 else 1
    
#     print(result)

# 마지막 코드. 성공함. 
import sys
input = sys.stdin.read
# 줄별로 읽어오기
data = input().splitlines()

# 첫 줄의 입력값을 정수로 변환하여 테스트 케이스의 수를 저장
t = int(data[0])

results = []
for i in range(1, t + 1):
    s = data[i]
    idx = 0 # 숫자가 입력되어있는 인덱스 저장하기 위한 변수
    # enumerate 를 사용하면 index와 value를 동시에 가져올 수 있음.
    # 문자열을 순회하면서 첫 번째 '!'가 아닌 문자의 인덱스를 찾음
    for j, char in enumerate(s):
        if char != '!':
            idx = j
            break
    # 조건에 따라 결과를 계산하여 리스트에 저장
    # idx가 짝수이고 문자열의 마지막 문자가 '0'인 경우 또는
    # idx가 홀수이고 문자열의 마지막 문자가 '1'인 경우 결과는 0, 그렇지 않으면 1
    results.append(int(not ((idx % 2 == 0) == (s[-1] == '0'))))
    

for result in results:
    print(result)