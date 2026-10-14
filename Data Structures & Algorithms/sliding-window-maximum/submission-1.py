class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dec_lis = deque()
        list_of_max = []
        counter = 0
        for i, n in enumerate(nums):
            while len(dec_lis) >= 1 and n > nums[dec_lis[-1]]:
                dec_lis.pop()
            dec_lis.append(i)
            print(dec_lis)
            counter +=1
            print(counter)
            if counter >= k:
                list_of_max.append(nums[dec_lis[0]])
                if dec_lis[0] == counter-k:
                    dec_lis.popleft()
        return list_of_max

                





