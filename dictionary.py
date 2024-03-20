#---Dictionary (slownik to struktura klucz - wartosc (key-value pair); nie ma dwoch kluczy o tej samej nazwie)
#slowniki tworzymy za pomoca miekkiej klamry -> {}

#1
device = {
   "hostname" : "router1" ,
   "ip" : "192.168.1.1" ,
   "model" : "Cisco 2901" ,
   "interfaces" : ["GigabitEthernet0" , "gigabitEthernet1"]
}
print(device)

#2
ip_address = device["ip"]
print(f"Device IP address: {ip_address}")

#3
device["location"] = 'Data Center A'
print(device)

#4
device["ip"] = "192.168.2.1"
print(device)

#5
del device["model"]
location = device.pop("location")
print(location)
print(device)

# #6
# for key in device.keys():
#     print(key)

# #7
# for value in device.values():
#     print(value)

#8
for key,value in device.items():
    print(f"{key}: {value}")

#9
    routing_table = {
        "10.0.0.0/24" : "192.168.1.1",
        "172.16.0.0/16" : "192.168.2.1"
    }
    for network, next_hop in routing_table.items():
        print(f"Destination: {network}, Next Hopw: {next_hop}")
