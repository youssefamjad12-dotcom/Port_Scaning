import ipaddress
from Scaning import TCP_Scan, UDP_Scan

# hy
print("""
Choose Service:
[1] TCP
[2] UDP
""")

service = input("Enter [1] or [2]: ")

start_ip = input("Enter Start IP: ")
end_ip = input("Enter End IP: ")

ports = input("Enter ports (ex: 80,53,443): ")

ports = [int(port.strip()) for port in ports.split(",")]


start = int(ipaddress.ip_address(start_ip))
end = int(ipaddress.ip_address(end_ip))

for ip_int in range(start, end + 1):

    ip = str(ipaddress.ip_address(ip_int))

    for port in ports:

        if service == "1":
            print(f"{ip}")
            TCP_Scan(ip, port)

        elif service == "2":
            print(f"{ip}")
            UDP_Scan(ip, port)

        else:
            print("Invalid choice.")
            break