def count(t,k):
    windowlist = []
    
    if len(t) == k:
        windowlist.append(t)
    else:
        for i in range(0, len(t)):
            if i == 0:
                sublist = t[:k]
                if len(sublist) == k:
                    windowlist.append(sublist)
            else:
                sublist = t[i:k+i]
                if len(sublist) == k:
                    windowlist.append(sublist)
    print(windowlist)
    difnumlist = []
    countlist = []
    for i in range(0, len(windowlist)):
        difnumlist.clear()
        for j in range(0, k):
            output = windowlist[i][j]
            if output not in difnumlist:
                difnumlist.append(windowlist[i][j])
                
        countlist.append(len(difnumlist))

    return countlist

if __name__ == "__main__":
    print(count([1,1,2,2],2)) # [1,2,1]
    print(count([1,1,1,1],4)) # [1]
    print(count([1,2,3,2,2,2],3)) # [3,2,2,1]
    print(count([3, 3, 2, 3, 3, 3, 1, 2, 2, 3],6))
    print(count([2, 3, 1, 3, 2],1))