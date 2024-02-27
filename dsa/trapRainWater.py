def trap(height):
    print(height)

    l = 0
    r = len(height)-1

    nextGreatElements =getNextGreatElement(height.copy())
    print(nextGreatElements)

    while l<r:
        print("l",l,"r",r)


        leftNextElementIndex = nextGreatElements[l]["index"]
        leftNextElementValue = nextGreatElements[l]["value"]

        if leftNextElementValue != -1:
            minimumOfTwoBars = min(height[l],leftNextElementValue)
            width =leftNextElementIndex -l -1
            areaBetweenTwoBars =  minimumOfTwoBars *  width
            print(minimumOfTwoBars,width,"areaBetweenTwoBars",areaBetweenTwoBars)
            inBetweenElementsLeft = height[l+1:leftNextElementIndex]
            print("inBetweenElementsLeft",inBetweenElementsLeft)

            effectiveAreaLeft = 0
            for heightItem in inBetweenElementsLeft:
                 effectiveAreaLeft = effectiveAreaLeft + heightItem *1
            effectiveAreaLeft = areaBetweenTwoBars - effectiveAreaLeft
            print("effectiveAreaLeft",effectiveAreaLeft)
            l = leftNextElementIndex - 1


             
        rightNextElementIndex = nextGreatElements[r]["index"]
        rightNextElementValue = nextGreatElements[r]["value"]

        if rightNextElementValue != -1:          
            minimumOfTwoBarsRight = min(height[r],rightNextElementValue)
            widthRight =rightNextElementIndex - r
            areaBetweenTwoBarsRight =  minimumOfTwoBarsRight *  widthRight
            print(minimumOfTwoBarsRight,widthRight,"areaBetweenTwoBarsRight",areaBetweenTwoBarsRight)
            inBetweenElementsRight = height[r+1:rightNextElementIndex]
            print("inBetweenElementsRight",inBetweenElementsRight)
            

        l=l+1
        r=r-1

def getNextGreatElement(elements):
        stack = []
        for index,element in enumerate(elements):
             while len(stack)>0 and stack[-1]["value"] <= element:
                  d = stack.pop()
                  elements[d["index"]] = {"value":element,"index":index}
             stack.append({"value":element,"index":index})
        # print(elements)
        # print(stack)

        while len(stack)>0:
             d =stack.pop()
             elements[d["index"]] = {"value":-1,"index":d["index"]}

        # print(elements)
        return elements

getNextGreatElement([8,7,6,9,10,11,2])




print(trap([0,1,0,2,1,0,1,3,0,1,2,1]))
# print(getNextGreatElement([8,7,6,9,10,11,2]))