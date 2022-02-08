def find(a,b):
    a.sort()
    b.sort()
    lenght = len(a)
    summa = 0
    
    for i in range(0, lenght):
        if a[i] > b[i]:
            summa += (a[i] - b[i])
        elif a[i] < b[i]:
            summa += (b[i] - a[i])
        else:
            summa += 0
    return summa



if __name__ == "__main__":
    print(find([1,2,3],[2,5,2])) # 3
    print(find([2],[7])) # 5
    print(find([1,1,1,1],[3,4,3,4])) # 10
    print(find([5,2,9,1,2,4],[8,8,2,3,9,4])) # 11