def dailyTemperatures(temperatures):

    stack =[]
    n  =len(temperatures)
    for i in range(n):
        while len(stack)>0 and stack[-1].get("value") < temperatures[i] :
            d = stack.pop()
            # print(":::",d)
            temperatures[d.get("idx")] = i - d.get("idx")

        stack.append({'idx':i,'value':temperatures[i]})
    while len(stack) > 0 :
        d = stack.pop()
        temperatures[d.get("idx")] = 0
    # print(stack)
    # print(temperatures)
    return temperatures

  
                

   


print(dailyTemperatures([73,74,75,71,69,72,76,73]))

# [1,1,4,2,1,1,0,0]