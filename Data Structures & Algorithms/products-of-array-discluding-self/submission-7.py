class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import numpy as np
        lispre = [1]
        for i in range(1,len(nums)):
            lispre.append(lispre[-1] * nums[i-1])

        lissuf = [1]
        for i in range(len(nums)-1, 0, -1):
            lissuf.append(lissuf[-1] * nums[i])
        lissuf = lissuf[::-1]
        
        print(nums)
        print(lispre)
        print(lissuf)
        c = [x * y for x, y in zip(lispre, lissuf)]
        return c

        
        # [prod(temp) where temp = nums.copy() for i in range(len(nums))]

        # from math import prod
        # lis = []
        # for i in range(len(nums)):
        #     temp = nums.copy()
        #     temp[i] = 1
        #     lis.append(prod(temp)) 
        # return lis

        # matrix = [nums.copy() for _ in range(len(nums))]
        # n = len(matrix)
        # for i in range(n):
        #     matrix[i][i] = 1
        # from math import prod
        # products = [prod(row) for row in matrix]
        # return products

        # a = Counter(nums)
        # print(a[0])
        # if a[0] > 1:  
        #     return [0 for i in range(len(nums))]  
        # total = 1
        # for n in nums:
        #     if n!= 0:
        #         total *= n
        # if a[0] == 1:
        #     lis = []
        #     for i in nums:
        #         if i == 0:
        #             lis.append(total)
        #         else:
        #             lis.append(0)
        #     return lis
        # lis = []
        # for i in nums:
        #     lis.append(int(total/i))
        # return lis