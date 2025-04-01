
# 첫번째 시도. def를 만들어서, 프린트하는 방법 먼저 구상
def check(str) :
    small = 0
    capital =0
    number = 0
    space = 0
    for i in str :
        if i >='a' and i <='z' :
            small += 1
        elif i >='A' and i <='Z' :
            capital += 1
        elif i >='0' and i <='9' :
            number += 1
        elif i == ' ' :
            space += 1
    return print(small, capital, number, space)

# if __name__ == '__main__':
#     str = input() 
# 문자열은 어떻게 받아야할까..?

#     check(str)


# 두번째 시도. import sys 를 활용해서 데이터를 읽어옴 => 32412kb	36ms
# import sys
# while True : 
    # sys 를 활용하면 데이터를 읽어올 수 있음
    # line = sys.stdin.readline().rstrip('\n') 

    # line = sys.stdin.readline().rstrip('\n')의 의미
    # sys.stdin.readline()은 표준 입력으로부터 한 줄을 읽어옵니다. 이 함수는 줄 끝에 개행 문자 \n을 포함합니다. 
    # 따라서 rstrip을 이용하여 개행 문자 \n을 제거합니다.
    # 표준 입력으로부터 한 줄을 개행 문자 없이 읽어오게 됩니다.
    
    # if not line : 
    #     break

#     check(line)

# 세번째 시도 : input을 이용하는 방법 => 32412kb	40ms => 4ms 차이
while True : 
    try:
        line = input("")
    except EOFError :
        break

    small, capital, number, space = 0,0,0,0

    for i in line :
        if i.islower() : 
            small += 1
        elif i.isupper() :
            capital += 1
        elif i.isdigit() :
            number += 1
        elif i == ' ' :
            space += 1
    print(small, capital, number, space)

# 네번째 시도. 문자열 구분 어떤게 더 빠를까? => 32412kb	36ms 동일함.! 하지만 코드 길이가 길어지므로 위의 방법이 더 나은듯!
# while True : 
#     line = sys.stdin.readline().rstrip('\n')
    
#     if not line : 
#         break

    # small = 0
    # capital = 0
    # number = 0 
    # space = 0
    # for i in line :
    #     if i >='a' and i <='z' :
    #         small += 1
    #     elif i >='A' and i <='Z' :
    #         capital += 1
    #     elif i >='0' and i <='9' :
    #         number += 1
    #     elif i == ' ' :
    #         space += 1
    # print(small, capital, number, space)