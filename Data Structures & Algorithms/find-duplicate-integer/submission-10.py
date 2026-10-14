class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #find a number not in its slot
        for i,n in enumerate(nums):
            nums[i] = n-1
        print(nums)
        for i in range(len(nums)):
            if nums[i] == i:
                print(i)
                continue
            else:
                j = i
                print(j)
                while nums[j] != j:
                    first_number = nums[j]
                    print(first_number)
                    second_number = nums[nums[j]]
                    print(second_number)

                    nums[nums[j]] = first_number
                    nums[j] = second_number
                    
                    if first_number == second_number:
                        return first_number+1






            


        


        

