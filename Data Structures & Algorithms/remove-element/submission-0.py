class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        lst = []
        for i in range(0, len(nums)):
            if nums[i]!=val:
                lst.append(nums[i])
                k+=1
        nums[:k] = lst
        return k