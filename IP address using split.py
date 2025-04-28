ip=input("Enter the IP address: ")

first_octet=int(ip.split(".")[0])
if first_octet >=1 and first_octet <=250:

    if 1 <= first_octet <=127:
        print("Class A")
    elif 128 <= first_octet <=191:
        print("Class B")
    elif 192 <= first_octet <=223:
        print("Class C")
    elif 224 <= first_octet <=239:
        print("Class D")
    elif 240 <= first_octet <=250:
        print("Class E")
else:
    print("Wrong IP")