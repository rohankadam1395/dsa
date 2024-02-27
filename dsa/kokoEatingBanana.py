import math
def minEatingSpeed(piles, h):
    # print(piles,h)
    l = 1
    high = max(piles)
    answer = l

    while l<=high:
        print(l,high)
        mid = l + math.floor((high-l)/2)
        print("mid",mid)
        hoursForMidSpeed = getHoursNeededForConsumption(mid,piles)
        if hoursForMidSpeed == h:
            print("found it ")
            answer = mid
            high = mid - 1

        elif hoursForMidSpeed > h:
            print("increase speed")
            # increase  the spee
            l = mid + 1
        else:
            print("decrease speed")
            # decrease speed
            high = mid - 1
    return l
    
        



def getHoursNeededForConsumption(speed,piles):
    total = 0
    for num in piles:
        total = total + math.ceil(num/speed)
    print("total",total)
    return total



# print(minEatingSpeed([3,6,7,11],8))

print(minEatingSpeed([30,11,23,4,20],6))
# print(minEatingSpeed([312884470],312884469))
# print(minEatingSpeed([1,1,1,999999999] ,10))

  

