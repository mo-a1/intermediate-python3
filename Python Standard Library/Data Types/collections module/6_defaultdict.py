from collections import defaultdict

a = [("a", 1), ("b", 2), ("a",5), ("c",4)]
dDic = defaultdict(list)
for i, j in a:
    dDic[i].append(j)

print(dDic)
