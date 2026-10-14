class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        r = 0
        stack = []
        for i in tokens:
            print(i)
            if i not in  ("+","-","*","/"):
                stack.append(i)
                continue
            
            a = str(stack[-2])
            b = str(stack[-1])
            stack.pop()
            stack.pop()
            if i == '/':
                c = int(int(a)/int(b))
            else:
                c = eval(a + i + b)
            stack.append(c) 
            print(c)
        return stack[0]