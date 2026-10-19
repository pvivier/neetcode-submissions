class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if left == right:
                return -1
            if nums[left] < nums[mid]: #this means the break is on the right
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid] < nums[right]: #this means the break is on the left
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                left +=1
        return -1
        