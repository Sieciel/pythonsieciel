# #I - Lists comprehensions

# #1 najprostsza forma komprehencji
# numbers = [1,2,3,4,5]
# squares = [n**3 for n in numbers]
# print(squares)

# #2 to samo co wyzej plus warunek (petla)
# evens = [n for n in numbers if n %2 == 0]
# print(evens)

# #3
# ip_list = ["192.168.1.1" , "10.0.0.256" , "172.16.0.1" , "256.0.0.1"]
# # valid_ips = [ip for ip in ip_list if 0<=int(ip.split('.')[0])<=255] #sprawdza tylko pierwszy oktet
# valid_ips = [ip for ip in ip_list if all (0 <=int(octet) <= 255 for octet in ip.split("."))]  #sprawdza wszystkie 4 oktety w adresie IP
# print(valid_ips)

# #4
# interfaces = [f"GigabitEthernet0/{i} "for i in range(0,5)]
# print(interfaces)

# #5
# subnets = [["192.168.1.1", "192.168.1.2"], ["10.0.0.1", "10.0.0.2"]]
# all_ips = [ip for subnet in subnets for ip in subnet]
# print(all_ips)

# II - Dictionary comprehension

#1
numbers = [1,2,3,4,5]
squares = {n:n**2 for n in numbers}
print(squares)

#2
even_squares = {n:n**2 for n in numbers if n %2 == 0}
print(even_squares)

#3
devices = ["router1", "Switch1", "Router2"]
ips = ["192.68.1.1", "192.168.1.2", "192.168.1.3"]
ip_device_map = {ips[i]:devices[i] for i in range(len(devices))}
print(ip_device_map)

#4
interfaces = ["Gi0/0", "Gi0/1", "Fa0/0"]
speeds = ["1Gbps", "1Gbps", "100Mbps"]
interface_speed =  {interfaces[i]: speeds[i] for i in range(len(interfaces))}
print(interface_speed)
