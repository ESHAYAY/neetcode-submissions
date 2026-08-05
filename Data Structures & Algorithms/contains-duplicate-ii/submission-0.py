from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)
        for i in range(0, len(nums)):
            if nums.count(nums[i])>=2:
                dic[nums[i]].append(i)
        for value in dic.values():
            for i in range(0, len(value)-1):
                if value[i+1] - value[i] <= k:
                    return True
        return False
        
            