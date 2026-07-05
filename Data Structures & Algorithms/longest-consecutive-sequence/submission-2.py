class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        c = 0
        m = 0
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                c+=1
            else:
                c = 0   
            m = max(m, c)
        if m!=0 or nums:
            return m+1
        return m