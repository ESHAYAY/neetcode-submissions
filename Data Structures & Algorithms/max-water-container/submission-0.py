class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = float('-inf')
        for i in range(0, len(heights)-1):
            c = 1
            left = i+1
            while(left < len(heights)):
                h = max(h, c * min(heights[i], heights[left]))
                left += 1
                c += 1
        return h