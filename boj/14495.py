# 피보나치 수열  fn = f(n-1) + f(n-3), f(1) = f(2) = f(3) = 1
# 자연수 n을 입력받아 n 번째 수열 구하기 ! 
 
# import sys
# n = int(sys.stdin.readline())


#  #f(n)을 구하기 위해 이전 값들을 저장할 리스트 생성
# flist = [0] * (n + 1)

# # 초기값 설정
# flist[1] = flist[2] = flist[3] = 1

# # 점화식에 따라 f(n) 계산
# for i in range(4, n + 1):
#     flist[i] = flist[i - 1] + flist[i - 3]

# # 결과 출력
# print(flist[n])

# 런타임에러 발생

# 재시도
import sys
n = int(sys.stdin.readline())

# f(n)을 구하기 위해 이전 값들을 저장할 리스트 생성
flist = [0] * (max(4, n + 1))

flist[1] = flist[2] = flist[3] = 1

for i in range(4, n + 1):
    flist[i] = flist[i - 1] + flist[i - 3]

print(flist[n])