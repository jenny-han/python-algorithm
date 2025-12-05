# 첫 시도
# 시간초과 실패 591B
# m, n = map(int, input().split())
# for num in range(m, n+1):
#     if num <= 1 :
#         continue
#     is_prime = True
#     if num <= 2:
#         print(num)
#         continue
#     for i in range(2, num-1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

# 재시도 314B 통과는 되었지만 여전히 느린 느낌 32412KB	5860ms
# m, n = map(int, input().split())
# for num in range(m,n+1):
#     if num <= 1 :
#         continue
#     is_prime = True
#     if num <= 2:
#         print(num)
#         continue
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

# 3번째 시도 에라토스테네스의 체 40084kb	280ms
import sys
m, n = map(int, sys.stdin.readline().split())

limit = n
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, limit+1, i):
            is_prime[j] = False

for number in range(m, n+1):
    if is_prime[number]:
        print(number)