import socket, struct

def get_default_gateway():
    """Read the default gateway directly from /proc."""
    with open("/proc/net/route") as file:
        for line in file:
            fields = line.strip().split()
            if fields[1] != '00000000':
                # If not default route, skip it
                continue
            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

def main():
	getgateway = get_default_gateway()
	print(get_default_gateway()) 

if __name__ == '__main__':
	main()