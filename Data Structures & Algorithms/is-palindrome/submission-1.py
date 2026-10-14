class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis = [c.lower() for c in s if c.isalnum()]
        if not lis:
            return True
        s = 0
        e = 1
        l = len(lis) -1
        while lis[s] == lis[-e]:
            print(lis[s], lis[-e])
            if s == l:
                return True
            s += 1
            e += 1
            
        return False
        

        