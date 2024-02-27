def checkInclusion(s1, s2):
    # print(s1,s2)
    orginalFrquencyChar = {}
    for s in s1:
        orginalFrquencyChar[s] = orginalFrquencyChar.get(s,0) + 1

    windowStart = 0
    frequencyChar = {}
    for windowEnd in range(len(s2)):
        # print(s2[windowEnd])
        frequencyChar[s2[windowEnd]] = frequencyChar.get(s2[windowEnd],0) + 1
        windowLength = windowEnd -windowStart +1
        if windowLength == len(s1):
            # print("check now")
            check = True
            for i in range(windowStart,windowEnd+1):
                # print("__",s2[i])
                if orginalFrquencyChar.get(s2[i]):
                    if frequencyChar[s2[i]] != orginalFrquencyChar[s2[i]]:
                        # print("break this loop")
                        check = False
                        break
                else:
                    check = False
                    break
            if check:
                return True

            frequencyChar[s2[windowStart]] = frequencyChar[s2[windowStart]] - 1
            # move the start by one now
            windowStart = windowStart + 1
    return False
        






    


print(checkInclusion("ab","eidboaoo"))