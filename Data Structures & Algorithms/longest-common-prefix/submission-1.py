class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        i = 0
        while(i <= len(s)):
            for j in strs:
                if not j.startswith(s[:i]):
                    return s[:i-1]
            i += 1
        return s