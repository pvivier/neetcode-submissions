class Solution:
    def isValid(self, s: str) -> bool:
        
        dic = {'a':'a','(':')','[':']','{':'}'}
        from collections import deque
        d = deque()
        last = 'a'
        for i in s:
            if i == '(':
                d.append(i)
                last = i
            elif i == '{':
                d.append(i)
                last = i
            elif i == '[':
                d.append(i)
                last = i
            else:
                if dic[last] == i:
                    d.pop()
                    last = 'a'
                    if d:
                        last = d[-1]
                else:
                    return False
        return not d
