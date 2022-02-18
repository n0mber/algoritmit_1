def count(s):
    
    while s.find("()") != -1:
        
        i = s.index('()')
        s = s[0: i :] + s[i+2 : :]

    return len(s)
    
if __name__ == "__main__":
    print(count("(()())")) # 0
    print(count(")))))")) # 5
    print(count("((())(")) # 2
    print(count("(()()())()()")) # 0
    print(count("))))))((((((")) # 12