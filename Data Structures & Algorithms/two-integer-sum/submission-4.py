class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        answer=[]
        for i in range(len(nums)):
            ans.append(target-nums[i])
        print(ans)
        for j in range(len(nums)):
            ans1=ans.copy()
            ans1.pop(j)
            if nums[j] in ans1:
               answer.append(j)
        return answer

