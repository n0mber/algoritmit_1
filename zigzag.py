def create(n):
    j = 0
    listNumber = []

    for i in range(1, n+1):
        if i%2 == 0:
            listNumber.insert(j, i)
            j += 1
        else:
            listNumber.insert(0, i)
            j += 1
    return listNumber

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2,4]