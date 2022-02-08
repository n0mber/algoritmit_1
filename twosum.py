def find(t,x):
    t.sort()
    reversedt = t.sort(reverse=True)
    lukupari = 0
    length = len(t)-1
    for i in range(1, len(t)): 
        length = int(length-1)  
        if t[i] + t[0] <= x:
            lukupari += 1
        if t[length] + t[i] <= x and length > i and length != len(t)-1:
            lukupari += 1
        if t[i] + t[len(t)-1] <= x and i != len(t)-1:
            lukupari += 1
    return lukupari
        


if __name__ == "__main__":
    print(find([1,2,3],4)) # 2
    print(find([5,2,4,7],10)) # 4
    print(find([1,1,1,1],2)) # 6
    print(find([1,1,1,1],1)) # 0
    print(find([8,8,1,2,5,1,9,3],9)) # 14