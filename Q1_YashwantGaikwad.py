from collections import Counter
string = "BOOKKEEPER"

oup = Counter(string)

for k in oup.keys():
    if(oup[k] == 2):
        string = string.replace(k, "Z")
    if(oup[k] > 2):
        string = string.replace(k, "X")
print(string)