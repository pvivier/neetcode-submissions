class TimeMap:

    def __init__(self):
        self.dic = defaultdict(lambda: [[], []])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key][0].append(value)
        self.dic[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        lis = self.dic[key][1]
        if len(lis) == 0:
            return ""
        target = timestamp
        left = 0
        right = len(lis) - 1

        while left < right:
            mid = (left+right)//2 +1
            if lis[mid] <= target:
                left = mid
            elif lis[mid] > target:
                right = mid -1
        if lis[right] <= target:
            return self.dic[key][0][right]
        return ""


