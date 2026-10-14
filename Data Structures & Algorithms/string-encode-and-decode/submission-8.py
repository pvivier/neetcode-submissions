class Solution:
    p = 11
    q = 13
    n = 143
    l = 120
    e = 73 #public
    d = 97 #private

    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    def char_to_num(self, c):
        return self.alphabet.index(c) if c in self.alphabet else None
    def num_to_char(self, n):
        try:
            return self.alphabet[n]
        except:
            return None
        

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return 'a'
        n = 143
        e = 73
        lis = []
        for s in strs:
            numberword = []
            for letter in s:
                m = self.char_to_num(letter)
                if m is None:
                    numberword.append(letter)
                    continue
                c = (m**e)%n
                numberword.append(str(c))
            wordstring='b'.join(numberword)
            lis.append(wordstring)
            print(lis)
        return 'c'.join(lis)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        if s == "a":
            return []
        n = 143
        d = 97 #private
        lis = s.split('c')
        final = []
        for numberword in lis:
            numberword = numberword.split('b')
            word = []
            for c in numberword:
                try:
                    m = (int(c)**d)%n
                    letter = self.num_to_char(m)
                except:
                    letter = c
                word.append(letter)
            word = ''.join(word)
            final.append(word)
        return final


        

        





