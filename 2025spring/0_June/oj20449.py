x=input()
ans=[]
now=0
for i in range(len(x)):
    now*=2
    now+=int(x[i])
    if now%5==0:ans.append('1')
    else:ans.append('0')
print(''.join(ans))