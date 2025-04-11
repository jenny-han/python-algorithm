#
import sys
from collections import defaultdict

n = int(sys.stdin.readline())
x_counter = defaultdict(int)
y_counter = defaultdict(int)

for _ in range(n):
    x, y = map(int, input().split())
    x_counter[x] += 1
    y_counter[y] += 1

x_lines = sum(1 for count in x_counter.values() if count >= 2)
y_lines = sum(1 for count in y_counter.values() if count >= 2)
print(x_lines + y_lines)



##==== counter 활용
# from collections import Counter
# import sys
# n = int(sys.stdin.readline)
# x_counter = Counter()
# y_counter = Counter()
# # x=0이거나 , Y=0인 좌표들을 이으면, X좌표,Y좌표와 평행한 값들을 구할 수 있다.
# for _ in range(n):
#     x, y = map(int, input().split())
#     x_counter[x] += 1
#     y_counter[y] += 1


# # x 또는 y좌표가 같은 게 2개 이상일 때, 하나의 선을 세울 수 있음
# x_lines = sum(1 for count in x_counter.values() if count >= 2)
# y_lines = sum(1 for count in y_counter.values() if count >= 2)
# print(x_lines + y_lines)

# for i in range(len(data)):
#     list1 = data[i].split(" ")
#     # print(list)
#     for k in range(len(data)):
#         if k != i:
#             list2 = data[k].split(" ")
#             if int(list1[0]) - int(list2[0]) == 0 or int(list1[1]) - int(list2[1]) == 0:
#                 if (",").join(list1) in array:
#                     array[(",").join(list1)].add((",").join(list2))
#                 elif (",").join(list2) in array:
#                     array[(",").join(list2)].add((",").join(list1))
#                 else:
#                     array[(",").join(list1)] = set()
#                     array[(",").join(list1)].add((",").join(list2))

# for l in list(array.keys()):
#     counter += len(array[l])

# print(counter)

# import sys

# n = int(sys.stdin.readline())
# data = []
# array = {}
# counter = 0
# # x=0이거나 , Y=0인 좌표들을 이으면, X좌표,Y좌표와 평행한 값들을 구할 수 있다.
# for _ in range(n):
#     data = sys.stdin.readline().rstrip('\n')
#     # print(data)
#     # if data in array.keys:
#     #     array[data] = set()
    
    
#     for k in range(len(data)):
#         # print("k", k)
#         list2 = data[k].split(" ")
#         if k != i:
#             if int(list[0]) - int(list2[0]) == 0 or int(list[1]) - int(list2[1]) == 0:
#                 if (",").join(list) in array:
#                     if list2 not in array[(",").join(list)]:
#                         array[(",").join(list)].append(list2)
#                         counter += 1
#                 elif (",").join(list2) in array:
#                     if list not in array[(",").join(list2)]:
#                         array[(",").join(list2)].append(list)
#                         counter += 1
#                 else:
#                     array[(",").join(list)] = []
#                     array[(",").join(list)].append(list2)
#                     counter += 1


# print(array)




####==== try 1 ? 
# import sys

# n = int(sys.stdin.readline())
# array = []
# # x=0이거나 , Y=0인 좌표들을 이으면, X좌표,Y좌표와 평행한 값들을 구할 수 있다.
# for _ in range(n):
#     data = sys.stdin.readline().rstrip('\n')
#     for d in data.split(" "):
#         if int(d) == 0:
#             array.append(data)
# print(len(array))

# ##==== 시간초과
# import sys

# n = int(sys.stdin.readline())
# data = []
# array = {}
# counter = 0
# # x=0이거나 , Y=0인 좌표들을 이으면, X좌표,Y좌표와 평행한 값들을 구할 수 있다.
# for _ in range(n):
#     data.append(sys.stdin.readline().rstrip('\n'))

# for i, v in enumerate(data):
#     list = v.split(" ")
#     # print(list)
#     for k in range(len(data)):
#         # print("k", k)
#         list2 = data[k].split(" ")
#         if k == i:
#             continue
#         else:
#             if int(list[0]) - int(list2[0]) == 0 or int(list[1]) - int(list2[1]) == 0:
#                 if (",").join(list) in array:
#                     if list2 not in array[(",").join(list)]:
#                         array[(",").join(list)].append(list2)
#                         counter += 1
#                 elif (",").join(list2) in array:
#                     if list not in array[(",").join(list2)]:
#                         array[(",").join(list2)].append(list)
#                         counter += 1
#                 else:
#                     array[(",").join(list)] = []
#                     array[(",").join(list)].append(list2)
#                     counter += 1


# print(counter)


