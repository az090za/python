infile=open("grades2.txt","r")
sum=0
stu=0
for line in infile:
    #print(line)
    g=int(line.split(",")[1])
    sum=sum+g
    stu=stu+1
if stu>0:
    avg=sum/stu
    print(avg)
else:
    print("No data in the file")

infile.close()