class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        output = []
        for i in range(len(nums)-2):
            target = -nums[i]
            start = 1
            end = 1
            while i+start != len(nums)-end:
                if nums[i+start] + nums[-end] == target:
                    output.append((nums[i], nums[i+start], nums[-end]))
                    start+=1
                elif nums[i+start] + nums[-end] < target:
                    start += 1
                else:
                    end += 1
        return list(set(output))