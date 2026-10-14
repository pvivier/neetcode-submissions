class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1


        counts = [[] for i in range(len(nums)+1)]
        for i,v in dic.items():
            counts[-v].append(i)
        
        final = []
        for i in counts:
            final.extend(i)
            if len(final) == k:
                return final


        # dic = defaultdict(int)
        # for i in nums:
        #     dic[i] +=1
        # largest_values = set(heapq.nlargest(k, dic.values()))
        # lis = []
        # for i,v in dic.items():
        #     if v in largest_values:
        #         lis.append(i)
        # return lis

