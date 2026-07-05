class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mx, mn = max(nums), min(min(nums), 1)
        lst = list(range(mn, mx+1))
        nums.sort()
        for i in lst:
            if i not in nums and i>0:
                return i
        
        return max(mx+1, 1)