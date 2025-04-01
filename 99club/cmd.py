# 문자열
# n = int(input())
# pattern = ""
# array = []

# # Loop to get the input
# for i in range(n) :
#     array.append(str(input()))

# # array에서 공통적인 부분 추출해서 result에 저장
# for i in range(len(array)):
#     for j in range(len(array[i])) :
#         # 첫번째 문자열부터 체크해서 공통이 있으면 

n = int(input())

first = list(str(input()))
len_first = len(first)
result = first[:]
for _ in range(n-1) :
    o = str(input())
    for j in range(len_first) :
        if first[j] != o[j] :
            result[j] = "?"
            continue
        

print(''.join(result))
# 전체 입력받은 문자에서 첫번째 문자를 체크
# 전체 문자의 자리수의 문자를 체크해서 값이 같으면 해당 문자를, 다르면 ?을 입력한다. 문자열에는 "."도 포함될수있다.

# for i in range(len(array[0])) :
#     for j in range(1, len(array)) :
#         if array[0][j] != array[i][j] : 
#             result[j] += array[i][j]
#         else : 
#             result[j] += "?"
#             break
# print(result)

