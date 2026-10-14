class Solution:
    def climbStairs(self, n: int) -> int:
        k=1
        end1 = 1
        end2 = 0
        while k<n:
            k+=1
            temp = end2
            end2 = end1
            end1 = (end1 + temp)
            
            print(k, end1, end2)
        return end1+end2