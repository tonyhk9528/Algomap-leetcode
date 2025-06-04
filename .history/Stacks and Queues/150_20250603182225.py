class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        answer = 0

        if len(tokens) == 1:
            return int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i].isnumeric() or (tokens[i][0] == '-' and tokens[i][1:].isnumeric()):
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if tokens[i] == '+':
                    answer = num1 + num2
                elif tokens[i] == '-':
                    answer = num1 - num2
                elif tokens[i] == '*':
                    answer = num1 * num2
                elif tokens[i] == '/':
                    answer = int(float(num1) / num2)
                
                stack.append(answer)
        
        return answer
