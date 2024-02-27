def generateParenthesis(n):

    base = ["(",")"]
    initial = base*n
    allCombos =[]

    # for i in range(0,len(initial)):
        
    #     item =[initial[i]]
    #     for j in range(0,len(initial)):
    #         if i !=j:
    #             item.append(initial[j])
    #     if isValidCombo(item):
    #         allCombos.append(item)
    #     print("".join(item))
    # print("//")
    # for i in reversed(range(0,len(initial))):
    #     if not (i==len(initial)-1 or i==0):
    #         item =[initial[i]]
    #         for j in reversed(range(0,len(initial))):
    #             if i !=j:
    #                 item.append(initial[j])
    #         if isValidCombo(item):
    #             allCombos.append(item)
    #         print("".join(item))
    # return allCombos


    # for p in permutations(initial):
    #     print("::::::",p)
    #     # if isValidCombo(p):
    #     #     print("p",p)
    #     #     allCombos.append("".join(p))
    #     allCombos.append("".join(p))
    print("final ",permutations(initial,0,0))
    return  allCombos


    

def permutations(initial,opening,closing):

    if len(initial) == 0:
        return [[],opening,closing]
     
    if len(initial) == 1:
        if initial[0] == ")":
             closing =closing + 1
             
            #  print("its a closing, check if there is a respective opening before",opening,closing)
        else:
             opening = opening + 1
            #  print("its an opening",opening,closing)
         
        return [[initial],opening,closing]


    allCombos = []

    for idx in range(len(initial)):
        # print("idx",idx)
        initialItem = initial[idx]
        remainingItems = initial[:idx]+initial[idx+1:]
        permtn , open , close= permutations(remainingItems,opening,closing)
        for p in permtn:
            print("o,c",open,close)
            print([initialItem],p)
            allCombos.append([initialItem]+p)
       
    # print("::::", allCombos)
    print("-----------")

    return [allCombos,opening,closing]
 



def isValidCombo(items):
    # print("isValidCombo",items)
    stack = []
    for item in items:
        if item == "(":
            stack.append(item)
        else:
            if len(stack) == 0:
                # print("not valid")
                return False
            stack.pop()
    # print("stack",stack)
    return len(stack) == 0


    


            



    # print("allCombos",allCombos)
    

print(generateParenthesis(2))

# 1,2,3

# 1,2,3
# 2,1,3 
# 3,1,2
# 3,2,1
# 2,3,1
# 1,3,2


