class TimeMap:

    def __init__(self):
        self.dic = defaultdict(lambda: [[], []])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key][0].append(value)
        self.dic[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        lis_of_timestamps = self.dic[key][1]
        print(lis_of_timestamps)


        left, right = 0, len(lis_of_timestamps)-1
        valid_mid = None
        while left <= right:
            mid = (left + right) // 2
            if lis_of_timestamps[mid] == timestamp:
                return self.dic[key][0][mid]
            elif lis_of_timestamps[mid] < timestamp:
                print('in ' + str(timestamp) + " " + str(mid))
                left = mid+1
                valid_mid = mid
            else:
                right = mid-1
        if valid_mid is not None:
            return self.dic[key][0][valid_mid]
        else:
            return ""


