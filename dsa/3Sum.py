def threeSum(nums):
    # print(nums)
    output = []
    outPutIndexHash = {}
    sortedNums =sorted(nums)
    visitedNums = []

    for index,num in enumerate(sortedNums):
        # print("__",num)
        if num not in visitedNums:
            visitedNums.append(num)
            target = 0 - num
            sortedRemainingElements = sortedNums[:index]+sortedNums[index+1:]
            # print("sortedRemainingElements",sortedRemainingElements)

            l = 0
            r = len(sortedRemainingElements) -1
            
            while l<r:
                left = sortedRemainingElements[l]
                right = sortedRemainingElements[r]
                if left + right> target:
                    r = r-1
                elif left + right < target:
                    l = l+1
                else:
                    # print("found")
                    result = sorted([num,left,right])
                    hash = "".join(str(result))
                    if outPutIndexHash.get(hash)is None:
                        output.append(result)
                        # outPutIndexHash["".join(str(sorted(result)))] = 1
                        outPutIndexHash[hash] =True
                        

                    l = l+1 
                    r = r-1
    # print("output",output)
    # print("outPutIndexHash",outPutIndexHash)
    return output

            
               





# print(threeSum([-1,0,1,2,-1,-4]))
#  [[-1,-1,2],[-1,0,1]]
# print(threeSum([0,0,0]))

print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
# nums = input("Enter the nums: ")
# print(threeSum([-1,0,1]))
# [[-1,0,1]]
# print(threeSum(nums))


