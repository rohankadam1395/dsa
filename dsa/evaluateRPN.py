def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        # float(y) is to be done in python2.x
        operators ={"+": lambda x,y : x + y,
                    "-": lambda x,y : x - y,
                    "*": lambda x,y : x * y,
                    "/": lambda x,y : int(x / y)}
        keysOps = operators.keys()

        # use of if else to check operator and the peroforming calculation directly 
        # instead of using operators dict is faster

        for token in tokens:
            print(token)
            if token in keysOps:
                # print("found operator",token)
                print(stack[-2],token,stack[-1])
                result = operators[token](stack[-2],stack[-1])
                # print("result",result)
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                print("operand",token)
                stack.append(int(token))
        return stack[0]




print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
))
        