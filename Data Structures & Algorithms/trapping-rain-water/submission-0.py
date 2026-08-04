class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(1, len(height)-1):
            left = max(height[:i])
            right = max(height[i+1:])
            h = max(0, min(left, right) - height[i])
            res += h
        return res
        
                    