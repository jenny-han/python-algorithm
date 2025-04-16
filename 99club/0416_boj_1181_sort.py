import sys

N = int(sys.stdin.readline().strip())

result = {}

for _ in range(N):
    word = sys.stdin.readline().strip()
    # 길이가 짧은 것 부터 넣기
    # 길이가 같으면 사전순으로 넣기
    if len(word) not in result.keys():
        result[len(word)] = set()
    result[len(word)].add(word)

for i in sorted(result.keys()):
    wordlist = sorted(list(result[i]))
    for v in wordlist:
        print(v)

# 
# for v in sorted(result.items()):
#     print(v[1])

# 1차 시도.. 뒤집고 뒤집기.. 틀렸습니다!
# import sys

# N = int(sys.stdin.readline().strip())

# test = []
# for _ in range(N):
#     word = sys.stdin.readline().strip()
#     if word not in test:
#         test.append(word)
# test.sort(key=len, reverse=True)

# for li in list(reversed(test)):
#     print(li)