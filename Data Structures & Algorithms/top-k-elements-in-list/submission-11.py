class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=dict()
        for i in nums:
            dic[i]=dic.get(i,0)+1
        lis=[]
        for i in range(len(nums)):
            lis.append([])
        for i in dic:
            lis[dic.get(i)-1].append(i)
        print(lis)
        new_lst = [item for sublist in lis for item in sublist]
        new_lst.reverse()
        answer=[]
        for i in range(k):
            answer.append(new_lst[i])
        return answer