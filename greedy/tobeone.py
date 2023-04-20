n, k = map(int,input().split())
result = 0

# #N이 K보다 크면 계속 진행
# while n >= k :
#     while n % k != 0 :
#         n -= 1
#         result += 1
#     n //= k
#     result += 1

# # 마지막으로 남은 수에 대해서 1씩 빼기
# while n > 1 :
#     n -= 1
#     result +=1


while(True) :
    # N이 K의 배수가 될 때까지 1을 뺀다.
    target = (n//k) * k 
    result += (n-target)
    n=target

    # N이 K보다 작을 때 (더이상 나눌 수 없을 때 반복문 탈출)
    if n<k :
        break
    result += 1
    n //= k

# 마지막으로 남은 수에 대해 1씩 빼기.
result += (n-1)
print(result)