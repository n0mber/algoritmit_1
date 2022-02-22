def count(s):
    hakemisto = {}
    hakemisto[0] = 0
    hakemisto2 = []
    for i in range(0, len(s)):
        if s[i] == "L":
            hakemisto[i+1] = hakemisto[i]-1
        elif s[i] == "R":
            hakemisto[i+1] = hakemisto[i]+1
        elif s[i] == "U":
            hakemisto[i+1] = hakemisto[i]-10
        elif s[i] == "D":
            hakemisto[i+1] = hakemisto[i]+10
    
    for key in hakemisto:
        if hakemisto[key] not in hakemisto2:
            hakemisto2.append(hakemisto[key])
    
    return len(hakemisto2)



print(count("LL")) # 3
print(count("UUDLRR")) # 5
print(count("UDUDUDU")) # 2