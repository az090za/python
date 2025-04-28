def count_zero(L):
    c=0
    for i in L:
        if i ==0:
            #print(0)
            i+=1
    print("There are ",c, "Zeros")

def Add_list(L1,L2):
    for i in range(len(L1)):
        print(L1[i]+L2[i], end=" ")
    print()
    
def sum2(n1,n2):
    c=n1+n2
    return c

def sum3(n1,n2):
    c=n1+n2
    return n1,n2,c
#--------------------------------
mylist1=[0,1,2,0,3,0,8,0]
mylist2=[0,1,2,0,3,0,8,0]
#count_zero(mylist1)
#Add_list(mylist1,mylist2)
c=sum2(3,4)
print(c)

print(sum2(3,4))

n1,n2,c =sum3(3,4)
print(n1,n2,c)