class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm={}
        for num in nums:
            if num in hm:
                return True
            else:
                hm[num]='*'
        return False
        