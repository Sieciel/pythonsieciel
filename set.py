#---Set (jest nieuporządkowany i zawiera nieduplikowane elementy; mozemy dodawac i odejmowac elementy )

#1
vlans = {10,20,30,40,50}
protocols = set(['OSPF', 'BGP', 'EIGRP'])
print(vlans)
print(protocols)

#2
vlans.add(60)
print(vlans)

# #3
# vlans.remove(10)
# print(vlans)

#4
vlans.remove(10)
protocols.discard('EIGRP')
print(vlans)
print(protocols)

#5
a = {1,2,3}
b = {3,4,5}
union_set = a.union(b)
print(union_set)

#6
intersection_set = a.intersection(b)
print(intersection_set)

#7
difference_set = a.difference(b)
print(difference_set)

