# # 계산할 수식은 정수 하나와 0개 이상의 느낌표. 정수는 0또는 1이며, 
# # 느낌표는 정수의 앞이나 뒤에 올수있음.
# # !n = n, n! = n팩. 
# # !0 = 1, 0! = 1
# # !1 = 0, 1! = 1
# # 
# # !!n!! = !(!(n!)!).
# # 수식계산하기
# # 수식의 개수 T, 수식이 한줄에 하나씩. 하나의 수식은 a개의 느낌표, 정수 n, b개의 느낌표가 공백없이 합쳐진 형태.

# t = int(input())

# for i in range(t) :
#     # 수식 입력받기 
#     list = input()
#     # 수식의 길이
#     # print(len(list))
#     a= 0
#     b = 0
#     n = -1
#     result = -1

#     for li in list :
#         if n == -1 and li == '!' :
#             a += 1
#         elif li == '0' or li == '1' :
#             n = int(li)
#         elif n != -1 and li == '!' :
#             b += 1
#     # print('a:', a ,'n:', n, 'b:', b)

# # !n = n, n! = n팩. 
# # !0 = 1, 0! = 1
# # !1 = 0, 1! = 1

#     # n = 1일때, 1!!...! => 1 , b는 몇개든  상관없음 1이 나옴.
#     # n = 1일때, !1 => 0!!1 => 1 !!!1 => 0
#     # n = 1일때, 앞에 !가 1개면 0 두개면 1, 짝수개면 1, 홀수개면 0임. 
#     # n = 0일때, 0!!...! => 1 , b는 몇개든  상관없음 1이 나옴.
#     if b > 0 :
#         result = 1

#     if result < 0 and n == 1 :
#         if a % 2 == 0 :
#             result = 1
#         else :
#             result = 0

#     elif result < 0 and n == 0 :
#         if a % 2 == 0 :
#             result = 0
#         else :
#             result = 1      
#     # n = 0일때, 0!!,, => 0! -> 1, 0!! ->1 0!!! ->1
#     # n = 0일때, !0 =>1 , !!0=>0
   
#     print(result)
    

t = int(input())

for i in range(t) :
    # 수식 입력받기 
    list = input()
    # 수식의 길이
    a= 0
    b = 0
    n = -1
    result = -1

    for li in list :
        if n == -1 and li == '!' :
            a += 1
        elif li == '0' or li == '1' :
            n = int(li)
        elif n != -1 and li == '!' :
            b += 1
            
    if b > 0 :
        result = 1

    if result < 0 and n == 1 :
        if a % 2 == 0 :
            result = 1
        else :
            result = 0

    elif result < 0 and n == 0 :
        if a % 2 == 0 :
            result = 0
        else :
            result = 1      
   
    print(result)
    