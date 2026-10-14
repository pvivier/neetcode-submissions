class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        from sortedcontainers import SortedList
        self.sl = SortedList(nums)

        self.k = k

        

    def add(self, val: int) -> int:
        self.sl.add(val)
        return self.sl[-self.k]
