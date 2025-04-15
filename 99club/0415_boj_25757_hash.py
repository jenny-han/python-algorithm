import sys

# 첫째 줄에는 플레아하기를 신청한 횟수와 플레이 할 게임의 종류
# 두번째 줄에는 같이 플레이 하고자 하는 사람들의 이름(아이디)
# 게임은 윷놀이 Y(2), 같은그림찾기 F(3) , 원카드 O(4) 인원이 부족하면 게임을 시작할 수없다.
# 한번 같이 플레이한 사람과는 다시 같이 플레이 하지 않는다.

N, game = sys.stdin.readline().strip().split(' ')

minigame = {'Y': 1, 'F': 2, 'O': 3}
meet = set()

for n in range(int(N)):
    player = sys.stdin.readline().rstrip('\n')
    meet.add(player)

print(len(meet)//minigame[game])

