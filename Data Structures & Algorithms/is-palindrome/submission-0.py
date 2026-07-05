class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (s.replace(" ", "")).lower()
        new = ""
        for i in s:
            if i.isalnum():
                new = new + i
        if new == new[::-1]:
            return True
        return False