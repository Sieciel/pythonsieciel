#---Tuple (lista ktorej elementow nie mozemy zmienic - immutable. Uzywamy w niej normalne nawiasy zaiast kwadratowych)

#1
device = ('Router' , '192.168.1.1' , "Cisco")
print(device)

#2
interface = "GigabitEthernet0", "up" , 1000
print(interface)

#3
try:
    device[1]="192.168.2.1"
except TypeError as e:
    print(e)

#4
name, ip, brand = device
print(f"Name: {name}, IP: {ip}, Brand: {brand}")

#5
device_info = ("Router1", "172.16.0.1" , "Juniper" , 22)
endpoint = ("10.10.10.1" , 443)

#6
