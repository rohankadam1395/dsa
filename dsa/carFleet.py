def carFleet(target, position, speed):
    # print(target, position, speed)
    cars = []
    for i in  range(len(position)):
        cars.append({"position":position[i],"speed":speed[i], "time": (target - position[i])/float(speed[i])})
    cars.sort(key=lambda x :x["position"])
    stack = []
    fleets = {}
    print("cars",cars)
    for index,car in enumerate(cars):
        while len(stack) > 0 and stack[-1]["time"] >     abs(car["time"] - stack[-1]["time"]): 
            print("diff",stack[-1]["time"],abs(car["time"] - stack[-1]["time"]))
            d = stack.pop()
            fleets[car["position"]] = 1
            # print("popped",d,index)
        # print("-------")
        stack.append(car)
    # while len(stack) > 0:
    #     d = stack.pop()
    #     fleets[d["position"]] = 1
    # print("stack",stack)
    # print("fleets",fleets)
    fleetNum = len(fleets)
    if len(stack) > 0:
        fleetNum =fleetNum + 1
    return fleetNum




    
        





# print(carFleet(10,[6,8],[3,2]))
# # 2
# print(carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
# # 3
# print(carFleet(10,[3],[3]))
# # 1
print(carFleet(100,[0,2,4],[4,2,1]))
# 1
print(carFleet(10,[0,4,2],[2,1,3]))
# 1


# 10,8,5,3 
# 0,3