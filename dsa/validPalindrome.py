def isPalindrome(s):
    alphaNum = "".join(filter(str.isalnum,s)).lower()
    reversedString = "".join(reversed(alphaNum))
    # print(alphaNum)
    # print(reversedString)
    return alphaNum == reversedString

isPalindrome("A man, a plan, a canal: Panama")