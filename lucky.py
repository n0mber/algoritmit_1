def check(n):
    
    numList = [int(digit) for digit in str(n)]
    result = 0
    for i in numList:
        result += i
    if result % 7 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(check(14)) # False
    print(check(16)) # True
    print(check(123)) # False
    print(check(777)) # True
    print(check(9999999)) # True