#I - Lists comprehensions

#1
numbers = [1,2,3,4,5]
squares = [n**3 for n in numbers]
print(squares)

#2
evens = [n for n in numbers if n %2 == 0]
print(evens)

#3
ip_list = ["192.168.1.1" , "10.0.0.256" , "172.16.0.1" , "256.0.0.1"]
# valid_ips = [ip for ip in ip_list if 0<=int(ip.split('.')[0])<=255] #sprawdza tylko pierwszy oktet
valid_ips = [ip for ip in ip_list if all (0 <=int(octet) <= 255 for octet in ip.split("."))]  #sprawdza wszystkie 4 oktety w adresie IP
print(valid_ips)

#4
interfaces = [f"GigabitEthernet0/{i} "for i in range(0,5)]
print(interfaces)

#5
subnets = [["192.168.1.1", "192.168.1.2"], ["10.0.0.1", "10.0.0.2"]]
all_ips = [ip for subnet in subnets for ip in subnet]
print(all_ips)