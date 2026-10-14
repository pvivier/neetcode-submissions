class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = cost[::-1]
        dic = defaultdict(lambda: float('inf'))
        dic[0] = 0
        index = 1
        dic[index] = steps[0]
        print(steps)
        while index < len(cost):
            index +=1
            print(index)
            dic[index] = steps[index-1] + min(dic[index-1], dic[index-2])
            print(dic)
            
        return min(dic[len(cost)], dic[len(cost)-1])