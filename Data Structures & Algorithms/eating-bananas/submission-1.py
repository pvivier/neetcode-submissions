class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_ = max(piles)
        while left <= right:
            mid = (left + right) // 2
            print('mid = ' + str(mid))
            total_hours = 0
            for i in piles:
                total_hours += math.ceil(i/mid)
            if total_hours <= h:
                min_ = mid
                #this means that we managed to eat
                #all the bananas while eating at rate k
                #so we now have to try to eat at a slower rate
                #so we have decrease k
                #to decrease k, we should move the right to mid
                right = mid - 1
            else:
                left = mid + 1
        return min_




