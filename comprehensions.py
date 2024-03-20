#I - Lists comprehensions

#1
numbers = [1,2,3,4,5]
squares = [n**3 for n in numbers]
print(squares)

#2
evens = [n for n in numbers if n %2 == 0]
print(evens)

