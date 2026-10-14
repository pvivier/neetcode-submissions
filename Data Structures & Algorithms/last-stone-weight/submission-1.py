class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        import heapq
        heapq.heapify(stones)
        print(stones)
        while len(stones)>1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            print(a)
            print(b)
            if a == b:
                continue
            if b < a:
                a = a - b
                heapq.heappush(stones, -a)
        if len(stones) == 0:
            return 0
        else:
            return -heapq.heappop(stones)
        