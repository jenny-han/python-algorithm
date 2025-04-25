import sys
# N : 상근이가 가지고있는 CD의 수 , M : 선영이가 가지고 있는 CD 의 수
while True:
    N, M = map(int, sys.stdin.readline().strip().split())
    if N ==0 and M==0: 
        break
        
    nset = set()
    for _ in range(N):
        nset.add(int(sys.stdin.readline()))
        
    count = 0
    for _ in range(M):
        if int(sys.stdin.readline()) in nset:
            count += 1


    print(count)
