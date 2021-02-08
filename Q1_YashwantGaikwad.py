string = "BOOKKEEPER"
two = []
three = []
new = ""

  
for i in range(0, len(string)):  
    count = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;    

    if(count > 1 and string[i] != '0'):  
        if(count == 2):
            two.append(string[i])
        elif (count > 2):
            three.append(string[i])

for x in two:
    new = string.replace(x, "Z")

for y in three:
    new = new.replace(y,"X")

print(new)