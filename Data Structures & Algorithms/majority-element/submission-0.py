class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = int(nums.count(i))
        m = max(dic, key=dic.get)
        return m
            