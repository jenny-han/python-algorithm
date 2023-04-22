# n : 세로 , m : 가로
n, m = map(int,input().split())

# 방금 입력받은 위치를 저장하기 위해 맵을 생성해서 모두 0으로 초기화한다.
mapbox = [[0] * m for _ in range(n)]

# (a,b) : 현 위치, d : 방향 (0:북, 1:동, 2:남, 3:서)
x, y, d = map(int, input().split())

# 시작 위치 (현위치) 방문 기록 세팅
mapbox[x][y] = 1

# 육지 인지 바다인지 입력 받는다 (육지 :0, 바다:1)
array = []
for i in range(n):
    # list 를 받아서 array 에 그대로 넣음
    array.append(list(map(int,input().split())))

# 북,동,남,서 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽방향으로 회전하도록 하는 함수
def turn_left() :
    global d
    d -= 1 # 반대방향으로 방향 설정.
    if d == -1 :
        d = 3 # -1 이 되면 3으로 다시 세팅

#시뮬레이션 시작
count = 1
turn_time = 0
while True : 
    #왼쪽으로 회전
    turn_left()
    
    # 이동될 좌표 방향 세팅
    nx = x + dx[d]
    ny = y + dy[d]
    
    #안 가본곳 이고 바다가 아니면, 이동
    if mapbox[nx][ny] == 0 and array[nx][ny] == 0:
        # 방문 마킹
        mapbox[nx][ny] = 1
        
        #현 위치 변경
        x = nx
        y = ny
        
        # 이동한 횟수 +1
        count += 1
        # 이동했으니까 방향 돈 횟수 초기화
        turn_time = 0
        continue
    # 회전한 이후에 가보지 않은 칸이없거나 바다인경우.
    else : 
        #회전하기
        turn_time += 1
    
    #네방향이모두 막혀있을경우, 방향은 유지.
    if turn_time == 4 :
        nx = x - dx[d]
        ny = y - dy[d]
        
        # 뒤로 갈 수 있다면, 육지라면.. 이동하기
        if array[nx][ny] == 0 :
            x = nx
            y = ny
            
        # 뒤가 바다로 막혀있는경우
        else :
            break 
        turn_time = 0

# 정답 출력
print(count)
    