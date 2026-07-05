class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs:
            s = tuple(sorted(i))
            if s not in dic:
                dic[s] = []
            dic[s].append(i)

        lst = []
        for key, value in dic.items():
            lst.append(value)
        return lst 