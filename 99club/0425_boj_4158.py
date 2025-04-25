import sys

# N : 상근이가 가지고있는 CD의 수 , M : 선영이가 가지고 있는 CD 의 수
while True:
    N, M = map(int, sys.stdin.readline().strip().split())
    if N == 0 and M == 0:
        break

    nlist = []  # 상근이가 가진 cd번호 오름차순
    mlist = []  # 선영이가 가진 cd번호 오름차순
    for _ in range(N):
        nlist.append(int(sys.stdin.readline()))

    for _ in range(M):
        mlist.append(int(sys.stdin.readline()))

    # print(nlist)
    # print(mlist)
    # sys.stdin.readline()

    count = 0
    if N < M:
        for n in nlist:
            if n in mlist:
                count += 1
    else:
        for m in mlist:
            if m in nlist:
                count += 1

	print(count)
    ## 선형 탐색은 시간이 오래 걸림
