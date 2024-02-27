# Since I feel like many solutions didn't explain clearly why it was called "sliding window"
#  (or I was too dumb to understand),
#  here's my attempt to explain in simplest of terms:

# First, if you start from the beginning (first character of string),
#  intuitively you know that we want to keep looking down the string until there are k characters that are
# different from the most popular. This is "expanding the window until it's not a valid window anymore". 
# This means moving the right pointer to the right, one by one,
# until (length of the substring) - (the "count of most popular character") = k. 
# We monitor the condition by keeping track of the most popular character with maxCount. 
# Simply, when we see a character, we increment its count, and check if it's greater than maxCount.
# If it is, we update maxCount.

# At this point, we have a window from start to end, and it has maxCount + k characters in it.
#  We know we can't keep expanding the window (since there are already k characters different from our most popular one).
# So what do we do? We just slide the entire window down. Why? Because the window represents our best answer so far, 
# and anything less than this window we don't care about (remember, we're trying to find the largest window in this string). 
# So it doesn't make sense to shrink the window. While we slide the window, we do 2 things: 1) we see a new character at end,
# and add that to the count array. 2) We also decrement the count of the character at start, which is now out of the window.

# At this point, we only need to know whether the total count of the new character at end (which represents the accurate count 
# of this character within the window) is greater than our maxCount, which represents the most popular character count for 
# the current window size that we have seen. If any new character's count exceeds the maxCount, that means: we have found
# a character in the current window that is even more popular for this given window size. Which means, we should now expand
#    the window until we have k "weirdos" again! We do this be extending out end by 1, and now we have a bigger window and
# a new maxCount. Any new character we see will have to beat this maxCount for us to expand the window again. Every step,
#    you move the end pointer down the string. If you can expand the window, then you move the end and nothing else.
# If you can't expand the window without violating the rule, then you slide the window by also moving the start forward.

# Don't forget, the "size of the window" is basically the value that we are trying to find the biggest value for. As
# you slide the window down, you're basically saying something like: "I have a window of length 4, where 2 of the 
# characters were the same (the maxCount characters). Can I find any other window with the same length, but more characters 
# that are the same? If so, then I can expand my window and I've found a larger window. Save this window length as my current
# best answer. Now repeat until I get to the end. Then return the largest window I saw in this string."

def characterReplacement(s, k):

    if len(s) ==1:
        return 1
    
    windowStart = 0
    frequecyChar = {}
    lengthOfMostPopularChar = 0
    maxWindowLength = 0

    for windowEnd in range(0,len(s)):
        lastChar = s[windowEnd]
        frequecyChar[lastChar] = frequecyChar.get(lastChar,0) + 1
        if frequecyChar[lastChar]  > lengthOfMostPopularChar:
            lengthOfMostPopularChar = frequecyChar[lastChar]        

        windowLength = windowEnd - windowStart
 
        if windowLength - lengthOfMostPopularChar ==k :
            # here checking popularChar is wrong  just check if lastChar is mpre than the most popukar
            if frequecyChar[lastChar] <= lengthOfMostPopularChar:
                # windowEnd = windowEnd + 1          
                frequecyChar[s[windowStart]] = frequecyChar[s[windowStart]] - 1
                windowStart = windowStart + 1

            else:
                # print("hey its a new chracter whos more popular")
                windowLength = windowLength + 1
        else:
            windowLength = windowLength + 1

        
        if windowLength > maxWindowLength:
             maxWindowLength = windowLength

    return maxWindowLength












print(characterReplacement("ABCAA",2))

# A A B A B B A
# 0 1 2 3 4 5 6
