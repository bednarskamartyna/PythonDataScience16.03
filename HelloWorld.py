print("Hello world")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

jan = ("Jan", "Kowalski", 33)
janina = ("Janina", "Nowak", (21,12,1978), 'K')

imie = jan[0]
nazwisko = jan[1]
wiek = jan[2]

imie, nazwisko, wiek = jan

lista = [1,2,3,4,-5,6,-10]

print(lista)

print(type(lista))

liczby = [0.1, 0.2, 0.3, 4.5, -7.3, 6.87, 10]
print(type(liczby))


imiona = ['Ala', 'Zygmunt', "Alojzy", "Bogusława"]

print(imiona)

lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
print(lista[1:6])

print(lista[2:6:2])

print(lista[:4])

print(lista[::-1])

print(lista[:])

lista = [2,3,5,7,9]
print(lista)

lista[2:4] = ["pies", "a", "2"]
print(lista)


lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
lista.append("zebra")
print(lista)

lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
lista.insert(2, "zebra") #dorzucenie zebry na pozycji drugiej, nie zamieniamy istniejącego elementu
print(lista)

tel = dict([('Jan', 4139277), ('Kazimierz', 4126327)])
print(tel)

zbior = {"ala", "kot", 1, 2.89}
print(zbior)

#operacje na zbiorach
#sprawdzenie czy element naleźy do zbioru
#dodawanie, odejmowanie, część wspólna i rozłączna