class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                left += 1
                right = mid
            elif nums[right] < nums[mid]:
                left = mid +1
            else:
                return nums[left]
        mid = (left + right) // 2
        return nums[mid]



