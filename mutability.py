#--- Mutability and references

#1 (stringa moemy literowac ale nie mozemy podmieniac elementow)
# my_string = "hello, Python!"
# try:
#     my_string[7] = 'W'
# except TypeError as e:
#     print(e)

#2 (w liscie mozna podmieniac elementy odwolujac sie do jej indeksu)
# my_list = [1,2,3,4]
# my_list[2] = 30
# print(my_list)

#3 (nowa zmienna tworzy wskaznik do obiektu anie tworzy nowy obiekt)
# original_list = [1,2,3]
# new_list = original_list
# new_list[1] = 200
# print(original_list)

#4 (tutaj wymuszamy stworznie nowego obiektu a nie tak jak wyzej  mamy tutaj dwie rozne listy)
# independent_copy = original_list[:]
# independent_copy[1] = 20
# print(original_list)
# print(independent_copy)

#5 (int jest immutable dlatego dla a zostaje wartosc poczatkowa)
# a = 10
# b = a
# b = 5
# print(a)
# print(b)

#6 (lista jest mutowalna wiec zmienia sie zawartosc listy)
# lst1 = [1,2,3]
# lst2 = lst1
# lst2.append(4)
# print(lst1)
# print(lst2)
