class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        left = 0
        right = -1
        counter_dic = Counter(s1)
        print(counter_dic)
        extra_stuff = 0
        dic = defaultdict(int)
        while right != len(s1)-1:
            right += 1
            dic[s2[right]] += 1
            if dic[s2[right]] > counter_dic[s2[right]]:
                extra_stuff +=1
        if extra_stuff == 0:
            return True
        print(dic)
        print(right)
        print(extra_stuff)
        while right != len(s2)-1:
            if dic[s2[left]] > counter_dic[s2[left]]:
                extra_stuff -=1
            dic[s2[left]] -= 1
            left +=1

            right += 1
            dic[s2[right]] += 1
            if dic[s2[right]] > counter_dic[s2[right]]:
                extra_stuff += 1
            if extra_stuff == 0:
                return True
            print(extra_stuff)
            print(dic)
        return False

