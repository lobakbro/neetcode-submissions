class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for n in nums:
            if seen.get(n, False):
                return True
            else: 
                seen[n]= 1
        return False
        