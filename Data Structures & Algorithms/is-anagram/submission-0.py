class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        lst = list(s)
        lst1 = list(t)
        lst.sort()
        lst1.sort()
        if lst == lst1:
            return True
        return False