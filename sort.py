def sum_of_integers(x):
    s=0
    while(x>0):
        s+=x%10
        x//=10
    return s

def sortkey_sum_of_integers(x):
    return soi(x)

def sortkey_string(x):
    return str(x)


a = list(map(int, input().rstrip().split()))
a = sorted(a,key=sortkey_sum_of_integers)

fin=[]
i=0
while( i<len(a) ):
    tmp=[a[i]]
    while(i<len(a)-1 and sum_of_integers(a[i])==sum_of_integers(a[i+1])):
        tmp.append(a[i+1])
        i+=1
    tmp=sorted(tmp,key=sortkey_string)
    for x in tmp:
        fin.append(x)
    i+=1
print(fin)
