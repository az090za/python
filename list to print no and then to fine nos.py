L=[-1,5,8,-1,-2,4,0,5]
print(L)

for i in range(0,len(L)):
    if L[i] < 0:
        L[i]=0
print(L)
