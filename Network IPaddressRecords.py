def menu():
    
    print("\n--- Network Asset Management Menu ---")
    print("1. Display all records")
    print("2. Search for IP by server name")
    print("3. Add a new server")
    print("4. Delete a server")
    print("5. Save and update the file")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    return choice

def Read_list(infile):
    servers = []
    ports = []
    ips = []
    try:
        with open(infile, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    servers.append(parts[0])
                    ports.append(parts[1])
                    ips.append(parts[2])
    except FileNotFoundError:
            print(f"File {infile} not found. Starting with empty lists.")
    return servers, ports, ips

def print_list(servers, ports, ips):
    print("\nServer Name\tPort\tIP Address")
    print("-----------------------------------------")
    for s, p, i in zip(servers, ports, ips):
        print(f"{s}\t{p}\t{i}")

def Search_IP(servers_name, servers, ips):
    if servers_name in servers:
        index = servers.index(servers_name)
        return ips[index]
    else:
        return None

def Add_Server(filename, server, port, ip, servers, ports, ips):
    if server in servers:
        print("Server already exists!")
    else:
        servers.append(server)
        ports.append(port)
        ips.append(ip)
    print("Server added successfully.")

def Delete_Server(filename, server_name, servers, ports, ips):
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

# assets file name
file_name = 'assets.txt'

# assign required values to variables
servers, ports, ips = Read_list(file_name)

# get user entered value
choice = menu()

while choice != 0:
    if choice == "1":
        print_list(servers,ports,ips)
    elif choice == "2":
        name = input("Enter server name: ")
        ip = Search_IP(name, servers, ips)
        if ip:
            print(f"The IP address of {name} is {ip}")
        else:
            print("Servers not found.")
    elif choice == "3":
        server_name = input("Enter server name: ")
        port = input("Enter port number: ")
        ip = input("Enter IP address: ")
        Add_Server(file_name, server_name, port, ip, servers, ports, ips)
    elif choice == "4":
            server_name = input("Enter server name to delete: ")
            Delete_Server(file_name, server_name, servers, ports, ips)
    elif choice == "5":
            update_list(file_name, servers, ports, ips)
    elif choice == "6":
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
    choice = menu()