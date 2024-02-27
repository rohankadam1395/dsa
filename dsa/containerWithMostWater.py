def maxArea(height):
    # print(height)
    l = 0
    r = len(height) -1

    maxArea = None


    while l<r:
        # print(height[l],height[r])

        width = r-l
        minHeight = min(height[l],height[r])
        # print("w: ",width,"h: ",minHeight)
        area = minHeight * width
        # print("area: ",area)
        if maxArea is None:
            maxArea = area
        elif area > maxArea:
            maxArea = area

        if height[l] > height[r]:
            r = r-1
            continue
        else:
            l = l+1
            continue
    # print("maxArea",maxArea)
    return maxArea
        


print(maxArea([1,8,6,2,5,4,8,3,7]))
