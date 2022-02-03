a_string = "abcdabcdabcd"
sameTrue = 1
sameFalse = 1
for n in range(1, len(a_string)):
    split_strings = [a_string[index : index + n] for index in range(0, len(a_string), n)]
    print(split_strings)

    for i in range(1, len(split_strings)):
        if len(split_strings[i]) == len(split_strings[i-1]):
            if split_strings[i] == split_strings[i-1]:
                sameTrue += 1
            else:
                sameTrue = 1
                sameFalse += 1
        else:
            sameTrue = 1
            sameFalse += 1
            
    
    if sameTrue == len(split_strings):
        print(True)
        print(sameTrue)


