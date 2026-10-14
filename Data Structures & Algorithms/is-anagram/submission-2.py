class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        dds = defaultdict(int)
        ddt = defaultdict(int)
        for i in s:
            dds[i] += 1
        for j in t:
            ddt[j] += 1
        if dds == ddt:
            return True
        else:
            return False




        