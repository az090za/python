def menu():
    print("1) Print student list ")
    print("2) Calculate the class average ")
    print("3) Add Student ")
    print("4) Update the file ")
    print("0) Exit ")
    opt=int(input("Enter Option "))
    return opt
def read_file(name,grade):
    infile=open("grades2.txt","r")
    for line in infile:
        n=line.split(",")[0]
        g=int(line.split(",")[1])
        name.append(n)
        grade.append(g)
    infile.close()
def print_list (name,grade):
    print("Name		Grade")
    print("----		-----")
    for i in range(len(name)):
        print(name[i], "\t\t",grade[i])
    print()
def avg(grade):
    sum=0
    for i in grade:
        sum+=i
    return sum/len(grade)
def add_stu(name,grade):
    n=input("Enter Student Name: ")
    g=input("Enter Grade: ")
    name.append(n)
    grade.append(g)
    print("Student ",n, " has been added")
    print()
def write_file(name,grade):
    outfile=open("grades2.txt","w")
    for i in range(len(name)):
        print(name[i],",",grade[i],file=outfile)
    outfile.close()
    print("File has been updated")
    print()
#----------------------------------
name=[]
grade=[]
read_file(name,grade)
#print(name)
#print(grade)

opt=menu()
while opt!=0:
    if opt==1:
        print_list(name,grade)
        #print("opt1")
    elif opt==2:
        print("Class is",avg(grade))
        #print("opt2")
    elif opt==3:
        add_stu(name,grade)
        #print("opt3")
    elif opt==4:
        write_file(name,grade)
        #print("opt4")
    else:
        print("Wrong Option")
    opt=menu()
    