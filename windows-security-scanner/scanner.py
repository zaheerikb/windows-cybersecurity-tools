# windows-security-scanner.py
import os
import platform
import socket
import subprocess
from datetime import datetime

def get_system_info():
    """Gather basic Windows system information"""
    print("🖥️  Windows Security Scanner")
    print("=" * 50)
    
    system_info = {
        "System": platform.system(),
        "Version": platform.version(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Scan Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return system_info

def check_windows_defender():
    """Check if Windows Defender is running"""
    try:
        result = subprocess.run(
            ['powershell', 'Get-MpComputerStatus'],
            capture_output=True, text=True
        )
        return "Running" if "RealTimeProtectionEnabled" in result.stdout else "Not Running"
    except:
        return "Unknown"

def scan_open_ports():
    """Scan common ports on localhost"""
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3389]
    open_ports = []
    
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            open_ports.append(port)
        sock.close()
        
    return open_ports

def main():
    print("⚠️  WARNING: For educational use only on systems you own! ⚠️\n")
    
    # System Information
    info = get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")
    
    # Windows Defender Status
    defender_status = check_windows_defender()
    print(f"Windows Defender Status: {defender_status}")
    
    # Open Ports Scan
    print("\n🔍 Scanning common ports on localhost...")
    open_ports = scan_open_ports()
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No common ports open on localhost")
    
    print(f"\n✅ Scan completed at {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()