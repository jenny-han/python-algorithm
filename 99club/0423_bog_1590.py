import sys

N, T = map(int, sys.stdin.readline().split())
wait_times =[]

for n in range(N):
    s,i,c = map(int, sys.stdin.readline().split())
    last = s + i * (c-1)

    if last < T : 
       continue

     
    for j in range(s, last+1, i):
        if j >= T :
            wait_times.append(j-T)
            break

if wait_times:
    print(min(wait_times))
else:
    print(-1)        