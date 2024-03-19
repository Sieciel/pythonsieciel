#--- Mutability and references

#1
# my_string = "hello, Python!"
# try:
#     my_string[7] = 'W'
# except TypeError as e:
#     print(e)

#2
# my_list = [1,2,3,4]
# my_list[2] = 30
# print(my_list)

#3
# original_list = [1,2,3]
# # new_list = original_list
# # new_list[1] = 200
# # print(original_list)

# #4
# independent_copy = original_list[:]
# independent_copy[1] = 20
# print(original_list)
# print(independent_copy)

#5
# a = 10
# b = a
# b = 5
# print(a)
# print(b)

#6
lst1 = [1,2,3]
lst2 = lst1
lst2.append(4)
print(lst1)
print(lst2)
