ip=input("Enter IP ") #192.168.1.1
is_private=ip.startswith("192") or ip.startswith("10")

print(is_private)