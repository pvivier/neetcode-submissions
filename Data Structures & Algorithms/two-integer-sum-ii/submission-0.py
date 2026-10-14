class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        start = 0
        end = 0

        for i in range(n):
            if numbers[start] + numbers[n-end-1] == target:
                return [start+1, n-end]
            elif numbers[start] + numbers[n-end-1] < target:
                start +=1
            else:
                end +=1
