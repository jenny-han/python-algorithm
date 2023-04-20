n, m, k = map(int, input().split())
nlist = list(map(int, input().split()))
sum = 0

nlist.sort()
first = nlist[-1]
second = nlist[-2]

mul = m // (k+1) 

sum += ((first * k) + second) * mul
sum += first * (m-((k+1)*mul))

# 책
# count = int(m/ (k+1)) * k
# count += m % (k+1)

# sum += count * first
# sum += (m-count) * second

print(sum)