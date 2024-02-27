def dailyTemperatures(temperatures):

    stack = []

    for index,item in enumerate(temperatures):
        while len(stack)>0 and stack[-1]["value"] < item:
            smallerElement = stack.pop()
            temperatures[smallerElement["index"]] = index - smallerElement["index"]

        stack.append({"value":item,"index":index})
    # print(stack)
    # print(temperatures)

    while len(stack) > 0:
        element = stack.pop()
        temperatures[element["index"]] = 0


    return temperatures


  
                

   


print(dailyTemperatures([73,74,75,71,69,72,76,73]))

# [1,1,4,2,1,1,0,0]