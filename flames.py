import time;

boy = "ram"        #change the boy name inside quotes
girl = "seeta"     #change the girl name inside quotes

boy = list(boy);
girl = list(girl);
c = len(boy) + len(girl)

for n in range(len(boy)):
    for m in range(len(girl)):
        if boy[n] == girl[m]:
            c-=2
            break

f = "flames"
f = list(f)

# print(f)

keywords={
    "f":"friend",
    "l":"love",
    "a":"affection",
    "m":"marriage",
    "e":"enemy",
    "s":"siblings"
}

for i in range(5):
    time.sleep(2)
    
    m = (c % len(f)) -1
    print("not ",keywords[f[m]])
    
    if m>-1:
        f = f[m+1:] + f[:m]
        # print(f)
    else:
        f = f[:m]
        # print(f)
        
    
print("Relationship is :",keywords[f[0]])
    
