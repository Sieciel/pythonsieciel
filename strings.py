#----Stings

#1
# single_quoted_string = 'hello, Python!'
# double_quoted_string = "hello, Python!"
# print(single_quoted_string)
# print(double_quoted_string)

#2
# greeting = "Hello"
# target = "World"
# message = greeting + ", " + target + "!"
# print(message)

# #3
# name = "Python"
# version = 3.8
# message = f"Welcome to {name} version {version}!"
# print(message)

# #4
# # a = 5
# # b = 10
# # result_message = f"The sum of {a} and {b} is {a+b}."
# # print(result_message)

# #5
# length = len(message)
# print(length)

#6
cidr_notation = "172.168.1.1/24"
ip_address = cidr_notation.split('/')[0]
print(ip_address)

#7
first_octet = ip_address[:ip_address.index('.')]
print(first_octet)
second_octet_start = ip_address.index('.') + 1
second_octet_end = ip_address.index('.', second_octet_start)
second_octet = ip_address[second_octet_start:second_octet_end]
print(second_octet)

#8
subnet_mask = cidr_notation.split('/')[1]
print(subnet_mask)