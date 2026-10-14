class Solution:
    def isValid(self, s: str) -> bool:
        
        dic = {'a':'a','(':')','[':']','{':'}'}
        from collections import deque
        d = deque()
        last = 'a'
        for i in s:
            if i == '(':
                d.append(i)
            elif i == '{':
                d.append(i)
            elif i == '[':
                d.append(i)
            else:
                if not d:
                    return False
                if dic[d[-1]] == i:
                    d.pop()
                else:
                    return False
        return not d
