class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        set_ = set()
        length = 0
        max_length = 0
        window = deque()
        for i,l in enumerate(string):
            while l in set_:
                leftmost = string[window[0]]
                set_.remove(leftmost)
                window.popleft()
                length -=1
            if l not in set_:
                set_.add(l)
                window.append(i)
                length +=1
            max_length = max(length, max_length)
        return max_length
                    



            