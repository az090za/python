def main():
    print("\n--- Network Asset Management Menu ---")
    print("1. Display all records")
    print("2. Search for IP by server name")
    print("3. Add a new server")
    print("4. Delete a server")
    print("5. Save and update the file")
    print("6. Exit")
choice = input("Enter your choice (1-6): ")

if choice == "1":
        print_list(servers,ports,ips)
elif choice == "2":
        name = input("Enter server name: ")
        ip = Search_IP(servers,ports,ips)
        if ip:
            print("The IP address of {servers} is {ips}")
        else:
            print("Servers not found.")
elif choice == "3":
        name = input("Enter server name: ")
        port = input("Enter port number: ")
        ip = input("Enter IP address: ")
        Add_Server(name, port, ip, servers, ports, ips)
elif choice == "4":
        name = input("Enter server name to delete: ")
        Delete_Server(infile, servers, ports, ips)
elif choice == "5":
        update_list(infile, servers, ports, ips)
elif choice == "6":
    print("Exiting the program. Goodbye!")
    break
else:
    print("Invalid choice. Please enter a number between 1 and 6.")

def Read_list(infile):
servers = [WebServer, DBServer, MailServer, BackupServer, AuthServer]
ports = [80, 3306, 25, 22, 443]
ips = [192.168.1.10, 192.168.1.20, 192.168.1.30, 192.168.1.40, 192.168.1.50]
try:
with open(infile, 'r') as file:
    for line in file:
    parts = line.strip().split(',')
    if len(parts) == 3:
        servers.append(parts[0])
        ports.append(parts[1])
        ips.append(parts[2])
    except FileNotFoundError:
            print("File {infile} not found. Starting with empty lists.")
    return servers, ports, ips

def print_list(servers, ports, ips):
print("\nServer Name\tPort\tIP Address")
print("-----------------------------------------")
    for s, p, i in zip(servers, ports, ips):
        print("{s}\t{p}\t{i}")


def Search_IP(servers_name, servers, ips):
if server_name in servers:
    index = servers.index(server_name)
    return ips[index]
else:
    return None

def Add_Server(server, port, ip, servers, ports, ips):
if server in servers:
    print("Server already exists!")
else:
    servers.append(server)
    ports.append(port)
    ips.append(ip)
    print("Server added successfully.")


def Delete_Server(server_name, servers, ports, ips):
if server_name in servers:
    index = servers.index(server_name)
    servers.pop(index)
    ports.pop(index)
    ips.pop(index)
    print("Server deleted successfully.")
else:
    print("Server not found.")

def update_list(infile, servers, ports, ips):
with open(infile, 'w') as file:
    for s, p, i in zip(servers, ports, ips):
        file.write(f"{s},{p},{i}\n")
        print("File updated successfully.")

if __name__ == "__main__":
main()