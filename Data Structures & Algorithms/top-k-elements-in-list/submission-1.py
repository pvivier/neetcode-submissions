class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] +=1
        counts = set(sorted(dic.values())[-k:])
        lis = []
        for i,v in dic.items():
            if v in counts:
                lis.append(i)
        return lis

