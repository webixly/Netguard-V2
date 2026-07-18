import socket

def scan_target_ports(target_host: str, ports_to_scan: list[int] = None) -> list[dict]:
    """
    Scans specific ports on a target host to identify open services.
    
    Args:
        target_host (str): IP address or domain to scan.
        ports_to_scan (list): List of port numbers to check.
        
    Returns:
        list: A list of dictionaries containing open ports and their banners.
    """
    if ports_to_scan is None:
        
        ports_to_scan = [21, 22, 80, 443, 8080]
        
    discovered_ports = []
    
   
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        return discovered_ports

    for port in ports_to_scan:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            port_data = {
                "port": port,
                "service": socket.getservbyport(port) if port in [21, 22, 80, 443] else "Unknown",
                "banner": "No banner grabbed"
            }
            
            
            try:
                s.send(b"Hello\r\n")
                banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                if banner:
                    port_data["banner"] = banner
            except Exception:
                pass
                
            discovered_ports.append(port_data)
            
        s.close()
        
    return discovered_ports