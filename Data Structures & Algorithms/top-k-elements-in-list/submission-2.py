class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] +=1
        largest_values = heapq.nlargest(k, dic.values())
        lis = []
        for i,v in dic.items():
            if v in largest_values:
                lis.append(i)
        return lis

