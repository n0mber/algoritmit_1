def count(s):
    charqueue = 0
    lst = []
    for index in range (0, len(s)):
        if index < len(s)-1:
            if s[index] == s[index+1]:
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