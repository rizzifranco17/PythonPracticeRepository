import socket

def port_scanner (target_ip, start_port,end_port):
    print (f"Scanning ports {start_port}-{end_port} on {target_ip}...")
    for port in range (start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target_ip,port))
            if result == 0:
                print (f"Port {port}is open.")
            else: 
                print (f"Port {port}is closed.")

target_ip = input("Enter the target IP: ")
port_scanner(target_ip,1,100)


