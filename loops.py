#---Petle - loopy

# #1
# port_status = "up"
# if port_status == "up":
#     print("The port is operational")

# #2
# if port_status == "up":
#     print("The port is operational")
# else:
#     print("The port is down")

# #3
# port_speed = 1000
# if port_speed == 100:
#     print ("FastEthernet port.")
# elif port_speed == 1000:
#     print("GigabitEthernet port.")
# else:
#     print("Speed unrecognized")

# #4
# interface_configs ={
#     "GigEth0/1": {"status": "up", "vlan": "10"},
#     "GigEth0/2": {"status": "down", "vlan": "20"},
#     "GigEth0/3": {"status": "up", "vlan": "10"},
#     }

# #5 while loop
# counter = 0
# while counter <5:
#     print(f"Counter is {counter}")
#     counter +=1

#6
counter = 0
while True:
    if counter == 5:
        break
    print(f"Counter is {counter}")
    counter +=1