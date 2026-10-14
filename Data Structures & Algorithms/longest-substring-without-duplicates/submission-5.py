class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        dic = {}
        length = 0
        max_length = 0
        window = deque()
        for l in string:
            if l in dic:
                w = window.copy()
                for i in w:
                    if window[0] == l:
                        window.popleft()
                        window.append(l)
                        break
                    window.popleft()
                    del dic[i]
                    length -=1
            else:
                window.append(l)
                dic[l] = 0
                length +=1
            max_length = max(length, max_length)
        return max_length