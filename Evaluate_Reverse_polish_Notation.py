class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        op = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for i in tokens:
            if i in op:
                b = stack.pop()
                a = stack.pop()
                stack.append(op[i](a, b))
            else:
                stack.append(int(i))

        return stack.pop()  


solution = Solution()
result = solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(result)  