class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums is None or len(nums) < 4:
            return []
        nums.sort()
        res = set()
        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        lst = []
        for i in res:
            lst.append(list(i))

        return lst
