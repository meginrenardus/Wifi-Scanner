#! /usr/bin/python3.7

import socket, struct
import nmap

def get_default_gateway():
    """Read the default gateway directly from /proc."""
    with open("/proc/net/route") as file:
        for line in file:
            fields = line.strip().split()
            if fields[1] != '00000000':
                # If not default route, skip it
                continue
            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

def portscanner():
	# initialiseer de port scanner
	nmScan = nmap.PortScanner()

	print("Scan gestart...")

	# scan localhost verkregen van get_default_gateway method voor specifieke ports
	nmScan.scan(get_default_gateway(),'53,23')#'20,21,23,69,80,109,110,445,666,1701,3389,5800,5900,5985')

	# Loop om al de gevonden resultaten over de poorten op te slaan en te printen
	# Loop door alle opgegeven hosts en sla op in "host". In dit geval is het er 1 van de functie get_default_gateway
	for host in nmScan.all_hosts():
		#Loop door de gebruikte protocollen (UDP,TCP)
		for proto in nmScan[host].all_protocols():
			#De gescande poorten worden opgeslagen in een dict 
			lport = nmScan[host][proto].keys()
			#loop door de lport dict om alle resultaten te printen
			for port in lport:
				print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
			return True if nmScan[host][proto][53]['state'] == 'open' else False
def main():
	
	portscan = portscanner()

if __name__ == '__main__':
	main()
