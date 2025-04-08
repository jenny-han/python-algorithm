# 모든 글자의 'A'와 'B' 로 모든 글자가 변경되어있음.
# 보고서에서 좋은 단어를 세보기로 함 (??)

# 좋은 단어란?
# 단어 위로 아치형 곡선을 그어 같은 글자끼리(A는 A끼리, B는 B끼리) 쌍을 짓기로 하였다. 
# 만약 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면, 그 단어는 '좋은 단어'이다.
# 예를 들어, 아래와 같은 단어는 좋은 단어이다.
# 문제가 이해가 안되는데?

# -- 어떻게 스택으로 구현할수있을까 고민하다가 고민만 늘어난 상황 ㅋ
# import sys
# num = int(input())
# count = 0

# for n in range(num) :
#     data = sys.stdin.readline().rstrip('\n')
#     stack = list(data)
#     is_good = False

#     # print(stack, len(stack))
#     # 길이가 홀수인 경우는 무조건 좋지 않음.
#     if len(stack)%2 == 1 :
#         is_good = False
#     # 길이가 짝수인 경우는 좋은 단어인지 확인함.
#     else : 
#         # 현재 단어랑 뒤의 단어 같은 지 확인 다르면 , 다음단어 확인
#         # for _ in 
#         #     if stack[i] == stack[i+1]  :
#         #         is_good = True
#         #         stack.pop(i)
#         #         # print(stack)
#         #     elif stack[i] == stack[i-1] :
#         #         is_good = True
#         #         stack.pop(i)
#         #     #     stack.pop(i+1) 
#         i = 0
#         while i < len(stack)-1 :
#             # print(stack)
#             if stack[i] == stack[i+1] :
#                 is_good = True
#                 stack.pop(i)
#                 stack.pop(i)
#                 i = 0
#             else :
#                 i += 1
            
            
#     if is_good : count += 1
# print(count)


# -- 시간 초과	
# import sys
# num = int(input())
# count = 0

# for n in range(num) :
#     data = sys.stdin.readline().rstrip('\n')
#     stack = list(data)
#     is_good = False
#     if len(stack)%2 == 1 :
#         is_good = False
#     else : 
#         i = 0
#         while i < len(stack)-1 :
#             # print(stack)
#             if stack[i] == stack[i+1] :
#                 is_good = True
#                 stack.pop(i)
#                 stack.pop(i)
#                 i = 0
#             else :
#                 i += 1
            
            
#     if is_good : count += 1
# print(count)

#-- 정석 코드
import sys

n = int(sys.stdin.readline()) # 테스트 케이스의 수 (한줄 읽기)
count = 0

for _ in range(n):
    word = sys.stdin.readline().strip() # 단어를 한줄씩 읽는다
    stack = [] # 스택 array 생성
    for ch in word:
        # 스택이 비어있지 않고, 스택의 마지막 문자(peek)와 현재 문자가 같으면 pop
        # stack 이 비어있으면 stack[-1] 에러가 나기 때문에 조건문을 추가함
        if stack and stack[-1] == ch: 
            stack.pop()
        # 스택이 비어있거나, 스택의 마지막 문자와 현재 문자가 다르면 push
        else:
            stack.append(ch)
    # 스택이 비어있으면 좋은 단어
    if not stack:
        count += 1
# 요약: "스택에 쌓인 마지막 글자와 현재 글자가 같으면 pop" 하는 방식
print(count)
