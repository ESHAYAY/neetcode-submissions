class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3 or nums is None:
            return []
        nums.sort()
        res = set()
        for i in range(0, len(nums)-2):
            left = i+1
            right = len(nums)-1
            while(left < right):
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        lst = []
        for i in res:
            lst.append(list(i))
        return lst
