def encode(strs):
    # write your code here
    encoded_str =[]
    for str in strs:
        encoded_str.append(str+":;")
    return "".join(encoded_str)

        


def decode(str):
    # write your code here
    print(str)
    decoded_str =[]
    word = ""

    for s in range(len(str)):
        print(s)
        if str[s] == ":" and str[s+1] == ";":
            print("hey",word)
            decoded_str.append(word)
            word = ""
        elif str[s-1] != ":" and str[s] != ";":
            word = word + str[s]

    print(decoded_str)


input = encode(["hello", "world", "leetcode::", "example"])
output = decode(input)

print(output)