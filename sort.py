def soi(x):
    s=0
    while(x>0):
        s+=x%10
        x//=10
    return s

def alpha(x):
    s=""
    ok=["zero ","one ","two ","three ","four ","five ","six ","seven ","eight ","nine "]
    cc=0
    while(x>0):
        s=ok[x%10]+s
        #print(x%10)
        x//=10
        cc+=1
    #print(cc)
    return s

    ##"eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen",#"twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"

def keyfn(x):
    return soi(x)

def keyfn2(x):
    return str(x)


a = list(map(int, input().rstrip().split()))
a = sorted(a,key=keyfn)
#print(a)
#print(alpha(a[1]))

fin=[]
i=0
while( i<len(a) ):
    tmp=[a[i]]
    while(i<len(a)-1 and soi(a[i])==soi(a[i+1])):
        tmp.append(a[i+1])
        i+=1
    #print(tmp)
    tmp=sorted(tmp,key=keyfn2)
    for x in tmp:
        fin.append(x)
    i+=1
    #print(tmp)
print(fin)
