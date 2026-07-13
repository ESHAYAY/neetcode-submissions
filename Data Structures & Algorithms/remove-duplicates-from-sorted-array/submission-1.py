class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = list(set(nums))
        nums[:len(new)] = sorted(new)
        return len(new)