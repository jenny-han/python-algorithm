# 계단 오르기 n에 도달하기 위한 단계가 필요함.
# 1을 오르거나 2를 오를 수있음. 정상까지 올라갈 수 있는 방법은 몇가지인가?

n = int(input())
# 1이나 2를 사용해서 goal을 만들기
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 :
            return n

        # dynamic programming 을 활용하여 풀기?
        stack = [1,2]

        for i in range(3,n+1) :
            current = stack[-1] + stack[-2]
            stack.append(current)

 
        return stack[-1]
