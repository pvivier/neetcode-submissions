class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = list(zip(position, speed)) 
        paired.sort()            

        a_sorted, b_reordered = zip(*paired)

        position_s = list(a_sorted)
        speed_s = list(b_reordered)








        n = len(position_s)
        fleets = n
        time_to_targets = defaultdict(int)

        for i, p in enumerate(position_s[::-1]):
            print(target, p, speed_s[n-i-1])
            alone_time_to_t = (target - p) / speed_s[n-i-1]
            print('alone time : ' + str(alone_time_to_t))
            if alone_time_to_t <= time_to_targets[n-i-1+1]:
                fleets -=1
            time_to_targets[n-i-1] = max(alone_time_to_t, time_to_targets[n-i-1+1])
        return fleets


