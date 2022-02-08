def count(s):
    charqueue = 0
    onecharqueue = 0
    lst = []
    for index in range (0, len(s)-1):
        for i in range (index+1, len(s)):
            if s[index] == s[i]:
                onecharqueue += 1
                continue
            else:
                charqueue += 1
                break
        for j in range (index, onecharqueue):
            if index < len(s)-onecharqueue:
                if s[index] == s[index+j]:
                    charqueue += 1
            if index < len(s)-2:
                if s[index] == s[index+1] == s[index+2]:
                    charqueue += 1
            currentChar = s[index]
        if currentChar not in lst:  
            lst.append(currentChar)
            for char in s:
                if char == currentChar:
                    charqueue += 1
      
    return charqueue



if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5