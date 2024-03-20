#--Functions  (definiujemy za pomoca slowa def; Najczesciej funkcje umieszcza sie na poczatku kodu a nizej odwolujemy sie do nich)

#1
def greet():
    print("Hello, Network Engineer!")

greet()

#2
def configure_interface(interface_name, ip_address):
    print(f"Configuring {interface_name} with IP {ip_address}")
configure_interface("GigabitEthernet0/1" , "192.168.1.1")

#3
configure_interface(ip_address= "192.168.1.1", interface_name= "GigabitEthernet0/1")

#4
def calculate_metrics(bytes_transmitted, bytes_received):
    tx_rate = bytes_transmitted / 60
    rx_rate = bytes_received / 60
    return tx_rate, rx_rate
tx, rx = calculate_metrics(3000, 5000)
print(f"Transmit Rate: {tx} Bps, Receive Rate: {rx} Bps")
