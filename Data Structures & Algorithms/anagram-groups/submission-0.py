class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        def convert_string_to_frozenset(s):
            ddic = defaultdict(int)
            for l in s:
                ddic[l]+=1
            fset = frozenset(ddic.items())
            return fset

        dics = defaultdict(list)
        for i, s in enumerate(strs):
            fset = convert_string_to_frozenset(s)
            dics[fset].append(s)
        return list(dics.values())







