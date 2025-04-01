word = str(input())
# 단어의 길이는 1~100자 
# 알파벳 소문자로만 구성되어 있음

# 시도 1. 그냥 단순 접근 
if(len(word) >= 1 and len(word) <= 100) :

    for i in range(len(word)):
        if word[i] != word[len(word) - 1 - i] :
            print(0)
            n = 0
            break
        else :
            if(i == len(word) - 1 -i) :
                print(1)
                break
     
# 시도 2 파이썬을 다 까먹었다..
word2 = list(str(input()))
if word2 == word2[::-1] :
    print(1)
else :
    print(0)


# 방법 3. 배열로 받아서 바꾸고 비교하기
word = list(input())
wordRv = list(reversed(word))

if word == wordRv:
    print("1")
else:
    print("0")