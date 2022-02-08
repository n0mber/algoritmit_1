def find(t):
    lst = []
    t.sort()
    for i in range(0, len(t)):
        if t[i] in lst:
            lst.remove(t[i])  
        else:
            lst.append(t[i])  
    return lst[0]

if __name__ == "__main__":
    print(find([2,2,4,3,4])) # 3
    print(find([1,2,3,4,1,2,3])) # 4
    print(find([1])) # 1
    print(find([1,4,2,3,2,3,4])) # 1
    print(find([4,1,3,2,3,2,1])) # 4
    print(find([4,1,3,2,2,1])) # 3, 4