def makeDict(a, b):
    tmp = {}
    for key, value in zip(a, b):
        tmp[key] = value
    
    return tmp

K = ('A','B','C')
V = (1, 2, 3)

#check unique
if(len(K) != len(set(K))):
    print("Key is not unique")
    quit()

#make dictionary
custom_dict = makeDict(K, V)

#check
same = 1
for dic, tup in zip(tuple(custom_dict.values()), V):
    if(dic != tup):
        same=0
        break
if (same):
    print(custom_dict)
else:
    print("error")
    quit()
