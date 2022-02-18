from collections import deque

def solve(n,k):
    lst = deque(range(1, n+1))
    for i in range(0, k):
        eka = lst.popleft()
        toka = lst.popleft()
        lst.append(toka)
        lst.append(eka)
        #away = (lst.pop(1), lst.pop(0))
        #lst.extend(away)

    return lst[0]

if __name__ == "__main__":
    print(solve(4,3)) # 4
    print(solve(12,5)) # 11
    print(solve(99,555)) # 11
    print(solve(12345,54321)) # 9875