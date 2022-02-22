class Mode:
    def add(self, x):
        modedict = {}
        modedict[len(modedict)] = x
        countList = []
        i = 0
        while i < len(modedict):
            countList.append(m.count(m[i]))
            i += 1
        d1 = dict(zip(m, modelist))
        print(d1)

        for (k, v) in d1.items():
            if v == max(modelist):
                return v 

if __name__ == "__main__":
    m = Mode()
    print(m.add(1)) # 1
    print(m.add(2)) # 1
    print(m.add(2)) # 2
    print(m.add(1)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 3