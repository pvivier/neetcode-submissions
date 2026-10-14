class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        print(a[0])
        if a[0] > 1:  
            return [0 for i in range(len(nums))]  
        total = 1
        for n in nums:
            if n!= 0:
                total *= n
        if a[0] == 1:
            lis = []
            for i in nums:
                if i == 0:
                    lis.append(total)
                else:
                    lis.append(0)
            return lis
        lis = []
        for i in nums:
            lis.append(int(total/i))
        return lis