# 2283. Check if Number Has Equal Digit Count and Digit Value
# Input: num = "1210"
# Output: true
# Explanation:
# num[0] = '1'. The digit 0 occurs once in num.
# num[1] = '2'. The digit 1 occurs twice in num.
# num[2] = '1'. The digit 2 occurs once in num.
# num[3] = '0'. The digit 3 occurs zero times in num.
# The condition holds true for every index in "1210", so return true.

class Solution:
    def digitCount(self, num: str) -> bool:
        for idx, value in enumerate(num):
#           idx 인덱스와 값을 비교해서 인덱스와 동일한 숫자가 몇개나 있는지 체크 한다.
# 			여기에서 값을 바로 return 해주는 것이 속도 향상에 도움이 된다.
            if (int(value) != num.count(str(idx))) :
                return False
        return True