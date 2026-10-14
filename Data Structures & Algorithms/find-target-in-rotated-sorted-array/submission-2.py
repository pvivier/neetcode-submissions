class Solution:
    def search(self, nums, target) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] > nums[mid]: #break is on left, right is clean, check if on right
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            elif nums[right] < nums[mid]: #break is on right, left is clean, check if on left
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else: #if list is sorted
                if target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
        return -1


