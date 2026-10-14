class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxim = 0
        for start in s:
            if start-1 in s:
                continue
            i = 0
            while True:
                if start+i in s:
                    i+=1
                else:
                    break

            if i > maxim:
                maxim = i
        return maxim
        