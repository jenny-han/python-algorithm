n,m = map(int, input().split())

result = 0
for i in range(n) : 
    data = list(map(int,input().split()))
    # min 함수 활용
    min_value = min(data)
    result = max(result,min_value)

# 2중 반복문 구조를 이용하는 답안. 
    min_value =10001 #숫자 범위보다 큰 수
    for a in data : 
        min_value = min(min(min_value,a))
    result = max(result, min_value)

print(result)
