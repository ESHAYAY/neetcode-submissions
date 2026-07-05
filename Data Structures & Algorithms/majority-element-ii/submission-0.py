class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = dict()
        for i in nums:
            if i not in dic:
                dic[i] = nums.count(i)
        lst = []
        n = len(nums)//3
        for key, value in dic.items():
            if value>n:
                lst.append(key)
        return lst