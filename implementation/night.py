# 나이트의 현재 위치를 입력한다
nightloc = input()

# 8*8 판에서 나이트의 위치에서 이동할수 있는 경우의 수를 찾아야한다.
# 현재위치를 세팅 col = a~h
# ord 로 문자형의 유니코드를 알아낸다
col = int(ord(nightloc[0])) - int((ord('a'))) + 1
row = int(nightloc[1])


# 나이트의 가능 이동방향 8가지 케이스 
steps = [(-2,1),(-2,-1),(2,1),(2,-1),(1,-2),(1,2),(-1,2),(-1,-2)]

# 현재 위치에서 이동가능한 경우의 수는?
result = 0

for step in steps :
    x = col + step[0]
    y = row + step[1]
    
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if x >= 1 and y >= 1 and x <= 8 and y <= 8 :
        result += 1
        
print(result)


