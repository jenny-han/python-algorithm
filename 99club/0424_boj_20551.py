# 배열 A 의 원수의 개수 N 과 질문의 개수 M
# N줄에 걸쳐 정수 A..가 주어짐
# A의 원소들이 오름차순으로 정렬된 배열 B
# M줄에 걸쳐 정수 D가 주어짐

# M개의 질문에 대해 주어진 D가 B에서 처음으로 등장한 위치 출력. 없는 경우에는 -1을 출력

import sys

N, M = map(int, sys.stdin.readline().split())
A = []

for i in range(N):
    A.append(int(sys.stdin.readline().rstrip()))
B = sorted(A)

for i in range(M):
    D = int(sys.stdin.readline().rstrip())
    left, right = 0, N - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if B[mid] == D:
            ans = mid
            right = mid - 1
        elif B[mid] < D:
            left = mid + 1
        else:
            right = mid - 1
    print(ans)
# 이진 탐색을 통해 O(logN)으로 찾을 수 있음