def find(s):
    a_string = s
    sameTrue = 1
    for n in range(1, len(a_string)+1):
        split_strings = [a_string[index : index + n] for index in range(0, len(a_string), n)]

        for i in range(1, len(split_strings)):
            if len(split_strings[i]) == len(split_strings[i-1]):
                if split_strings[i] == split_strings[i-1]:
                    sameTrue += 1
                else:
                    sameTrue = 1         
            else:
                sameTrue = 1           
        
        if sameTrue == len(split_strings):
            return len(split_strings[0])



if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7