#--Class

#1
class NetworkDevice:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
#3
    def display_config(self):
        print(f"Hostname: {self.hostname}, IP address: {self.ip_address}")

#2

# print(f"Device: {router.hostname}, IP: {router.ip_address}")

# #3
# router.display_config()

#4
class Router(NetworkDevice):
    def __init__(self, hostname, ip_address, routing_protocol):
        super(). __init__(hostname, ip_address)
        self.routing_protocol = routing_protocol
#5
    def display_config(self):
        super().display_config()
        print(f"Routing protocol: {self.routing_protocol}")

router = NetworkDevice ("Router1", "192.168.1.1")
router.display_config()

# router = Router("Router1", "192.168.1.1", "OSPF")
# print(f"Routing Protocol: {router.routing_protocol}")


