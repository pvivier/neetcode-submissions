class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        mid = l//2
        i = 1
        step = 0
        while nums[mid] != target and step !=1:
            print('mid ' + str(mid))
            print('step ' + str(step))
            i+=1
            step = l //(2**i) +1
            if nums[mid] < target:
                mid = mid + step
            else:
                mid = mid - step
            if mid <0:
                mid = 0
            if mid > len(nums)-1:
                mid = len(nums)-1
        if nums[mid] == target:
            return mid
        else:
            return -1
