sum1=0
for i in range(1,6):
    grade=int(input("Enter grade:" + str(i) + "\t"))
    #sum1 += grade
    sum1=sum1+grade
avg=sum1 / 5
print("Avg", int(avg))