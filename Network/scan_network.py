import nmap

nm = nmap.PortScanner()

myhost = '192.168.0.1'
nm.scan(myhost, '22-443')

print(nm.command_line())
print(nm.scaninfo())
print(nm.all_hosts())
print(nm[myhost].hostname())
print(nm[myhost].state())
print(nm[myhost].all_protocols())
print(nm[myhost]['tcp'].keys())
print(nm[myhost].has_tcp(22))
print(nm[myhost].has_tcp(23))
print(nm[myhost]['tcp'][22])
print(nm[myhost].tcp(22))
print(nm[myhost]['tcp'][22]['state'])



#python-nmap library
