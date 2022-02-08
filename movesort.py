def check(t):
    n = int(len(t)/2)
    sortedt = sorted(t)

    for i in range(n, 0, -1):
        if t == sortedt:
            return t
        else:
            startlist = t[:i]
            endlist = t[-i:]
            
            if i != n:
                betweenlist = t[i:-i] 
            else:
                betweenlist = []
            
            t = endlist + betweenlist + startlist 

        
    
    return t

if __name__ == "__main__":
    print(check([3,1,4,2])) # True
    print(check([3,1,2,4])) # False
    print(check([1,2])) # True
    print(check([4,5,6,1,2,3])) # True
    print(check([5, 8, 13, 1, 3, 6, 11, 4, 9, 12, 14, 2, 7, 10])) # False