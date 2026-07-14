class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lst = []
        for i in range(0, len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    lst.append(i+1)
                    lst.append(j+1)
        return lst