def twoSum(numbers, target):
    # print(numbers,target)

    l=0
    r=len(numbers) -1

    while l<r:
        # print(l,r)
        sum = numbers[l] + numbers[r]

        if sum == target:
            return [l+1,r+1]
        elif sum >target:
            r = r-1
        else:
            l=l+1


print(twoSum([-1,0],-1))