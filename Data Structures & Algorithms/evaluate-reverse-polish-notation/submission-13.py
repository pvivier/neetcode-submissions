class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for i in tokens:
            if i not in  ("+","-","*","/"):
                stack.append(i)
                continue
            b = stack.pop()
            a = stack.pop()
            if i == '/':
                c = int(int(a)/int(b))
            else:
                c = eval(str(a) + i + str(b))
            stack.append(c)
        return stack[0]