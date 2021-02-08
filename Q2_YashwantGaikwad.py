string = "EduCatiON"
lower = 0
upper = 0


for i in range(0, len(string)):   
    # for j in range(i+1, len(string)):  
    #     if(string[i] == string[j] and string[i] != ' '):  
    #         count = count + 1;    
    if(string[i].islower()):
        string= string[0:i] + string[i].upper() + string[i+1: ]
        lower = lower + 1
    else:
        string= string[0:i] + string[i].lower() + string[i+1: ]
        upper = upper + 1

print ("lower characters = ", lower)
print ("upper characters = ", upper)
print ("formatted string = ", string)
