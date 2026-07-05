import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            res.append(int(math.prod(nums[:i]) * math.prod(nums[i+1:])))
        return res