class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)

        lower = 1
        upper = m

        while lower < upper:
            mid = (lower + upper) //2
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            if time > h:
                lower = mid +1
            elif time <= h:
                upper = mid
            print(mid, time)
        mid = lower
        return mid
            




