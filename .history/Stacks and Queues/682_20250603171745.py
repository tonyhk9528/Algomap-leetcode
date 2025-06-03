class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        stack = []
        answer = 0

        for op in operations:
            if op.isnumeric():
                stack.append(int(op))
            elif op.startswith("-"):
                stack.append(int(op))
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
                
        return sum(stack)