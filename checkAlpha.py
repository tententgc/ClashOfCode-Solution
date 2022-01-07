a=input()
q=[]
for i in a:
    if i.isalpha():
        q.append(("-","_")[i.islower()]) 
    else:
        q.append ("*")
print("".join(q)) 
    
    