import socket  # Import socket module for network communication
import termcolor  # Import termcolor module for colored terminal output

def scan(target, ports):
    """ Function to scan ports on a target IP address."""
    print('\n' + ' Starting Scan For ' + str(target))  
    for port in range(1, ports + 1):  # Loop through the specified range of ports
        scan_port(target, port)  # Call scan_port function for each port

def scan_port(ipaddress, port):
    """Function to scan a single port on a given IP address."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # use Ipv4, and Create a TCP socket 
        sock.settimeout(0.5)  # timeout for the connection attempt
        sock.connect((ipaddress, port))  # Try to connect to the target IP and port
        print(termcolor.colored("[+] Port Opened " + str(port), 'green'))  
        sock.close()  # Close the socket
    except:
        print(termcolor.colored("[-] Port Closed " + str(port), 'red'))
        # pass  # If connection fails, do nothing (port is considered closed)

try:
    targets = input("[*] Enter Targets To Scan (split them by ,): ")
    ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

    if ',' in targets:  # Check if multiple targets are provided
        print(termcolor.colored("[*] Scanning Multiple Targets", 'green')) 
        for ip_addr in targets.split(','):  # Split the targets by comma and scan each one
            scan(ip_addr.strip(), ports)  # Strip whitespace from each IP address and scan it
    else:
        scan(targets.strip(), ports)  # If only one target, strip whitespace and scan it
except KeyboardInterrupt:
    print(termcolor.colored("\n[*] Exiting Program", 'red'))  
except Exception as e:
    print(termcolor.colored(f"An error occurred: {e}", 'red'))  # Print any other exceptions that occur





# import socket
# import termcolor

# def scan(target, ports):
#     print('\n' + ' Starting Scan For ' + str(target))
#     for port in range(1, ports):
#         scan_port(target, ports)

# def scan_port(ipaddress, port):
#     try:
#         sock = socket.socket()
#         sock.connect((ipaddress, port))
#         print("[+] Port Opened " + str(port))
#         sock.close()
#     except:
#         pass
    
# targets = input("[*] Enter Targets To Scan(split them by ,): ")
# ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
# if ',' in targets:
#     print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
#     for ip_addr in targets.split(','):
#         scan(ip_addr(' '), ports)
# else:
#     scan(targets, ports)