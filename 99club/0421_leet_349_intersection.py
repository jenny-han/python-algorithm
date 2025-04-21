# 제출한 코드
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result =set()
        if len(nums1) >= len(nums2) :
            for n in nums2 :
                if n in nums1 :
                    result.add(n)
        else :
            for n in nums1 :
                if n in nums2 :
                    result.add(n)
        return list(result)

# intersection을 통해 비교하는 방법이 있었음..https://www.w3schools.com/python/ref_set_intersection.asp
    class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=list(set(nums1).intersection(set(nums2)))
        return n