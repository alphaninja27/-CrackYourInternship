class Solution:
    def calculate(self, s: str) -> int:
        num, sig, stk = 0, "+", []
        for i in s + "+":
            if i.isdigit():
                num = num * 10 + int(i)
            elif i in "+-*/":
                if sig == "+":
                    stk.append(num)
                if sig == "-":
                    stk.append(-num)
                if sig == "*":
                    stk.append(stk.pop()*num)
                if sig == "/":
                    stk.append(math.trunc(stk.pop() / num))
                sig = i
                num = 0
        return sum(stk)
                
