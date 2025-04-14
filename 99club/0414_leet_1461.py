def hasAllCodes(s, k):
	# 포함되어있는 바이너리 코드 집합 생성
    seen = set()
    # 문자열의 길이 만큼 확인 
    # (k길이만큼 확인할 거기때문에 배열을 넘어가지 않도록 for문 조건 구성함)
    for i in range(len(s) - k + 1):
    	# s문자열의 i부터 k길이만큼의 값을 set에 넣음
        seen.add(s[i:i+k])
        # 중복없이 저장된 조합이 2 ** k (조합가능 한 개수)와 같은지 확인
    return len(seen) == 2 ** k