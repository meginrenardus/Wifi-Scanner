#! /usr/bin/python3.7

import nmap

def portscanner():
	# initialize the port scanner
	nmScan = nmap.PortScanner()

	print("Scan gestart...")

	# scan localhost for ports in range 21-443
	#nmScan.scan('192.168.1.1', '21-443')
	nmScan.scan('192.168.1.1', '53-55')

	# run a loop to print all the found result about the ports
	for host in nmScan.all_hosts():
		print('Host : %s (%s)' % (host, nmScan[host].hostname()))
		print('State : %s' % nmScan[host].state())
		for proto in nmScan[host].all_protocols():
			print('----------')
			print('Protocol : %s' % proto)

			lport = nmScan[host][proto].keys()
			for port in lport:
				print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
				return True if nmScan[host][proto][53]['state'] == 'open' else False
def main():
	portscan = portscanner()

if __name__ == '__main__':
	main()
		
