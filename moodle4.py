import time

def counttime(n):
    lst = []
    alku = time.time()
    for i in range(1, n+1):
        lst.append(i)
    loppu = time.time()
    print("aikaa lisäykseen kului", loppu-alku, "s")

    uusalku = time.time()
    for i in range(0, len(lst)):
        lst.pop(0)
    uusloppu = time.time()
    print("aikaa poistoon kului", uusloppu-uusalku, "s")

counttime(10**5)
