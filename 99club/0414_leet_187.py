class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
    	# seen : 한번이상 나온 10글자 문자열 저장 set	
        seen = set()
        # repeated : 두번이상 등장한 문자열 저장 set
        repeated = set()
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)
        return list(repeated)