

def isValid(s):
    
    stack =[]
    openingBracks = ["{","[","("]
    closingBracks = ["}","]",")"]
    for item in s:
        if item in openingBracks:
            stack.append(item)
        else:
            if len(stack) == 0:
                # this happens when there is a closing bracket but no opening bracket before
                return False
            idx = closingBracks.index(item)
            if stack[-1] != openingBracks[idx]:
                return False
            else:
                # opening brack found for this closing bracket
                # so pop the opening one and move forward
                stack.pop()
    # below can happen when there are only opening brackets
    # in the input
    return len(stack) == 0
        
    

            




print(isValid("["))
