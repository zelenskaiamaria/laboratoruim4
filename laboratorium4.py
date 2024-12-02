
import math

# 1
# r = int(input('radius: '))
# def funck():
#     if r>0:
#         print(f's ={r*r*3.14}')
#     else:
#         print('Nie isnieje')
# funck()

# 2
# a = int(input('Podaj a: '))
# b = int(input('Podaj b: '))
# h = int(input('Podaj h: '))
# def fun():
#     if (a>0 and b>0 and h>0):
#         print(f's = {((a+b)*h)/2}')
#     else:
#         print('Nie isnieje')
# fun()

# 3
# liczba = int(input('podaj liczbę: '))
# def fun():
#     if liczba>0:
#         print('liczba jest dodatnia')
#     else:
#         print('liczba jest ujemna')
# fun()

# 4
# def wskażnik_BMI(waga = float(input("Podaj swoją wagę w kg")), wzrost = float(input("Podaj swój wzrost w metrach"))):
#     BMI = waga / wzrost**2
#     if BMI < 18.5:
#         return BMI, "niedowaga"
#     elif 18.5 < BMI < 24.9:
#         return BMI, "pożądana masa ciała"
#     elif 25 < BMI < 29.9:
#         return BMI, "nadwaga"
#     elif 30 < BMI < 34.9:
#         return BMI, "otyłość I stopnia"
#     elif 35 < BMI < 39.9:
#         return BMI, "otyłość II stopnia"
#     elif BMI > 40:
#         return BMI, "otyłość III stopnia"
#
# print(wskażnik_BMI())

# 5
# list = [3,6,7,5,9]
# def fun():

#     suma = sum(list)
#     leng = len(list)
#     print(f"{suma/leng}")
# fun()


# 9
# n=int(input('podaj liczbę: '))
# def fib(n):
#     if n ==1 or n == 2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(n))



#7

# def oblicz_pole_trojkąta(a , b ,c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return "Boki muszą być dodatnimi."
#     if a + b <= c or b + c <= a or a + c <= b:
#         return "Podane boki nie mogą tworzyć trojkąta."
#
#     s = (a + b + c) / 2
#
#     pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
#
#     return "Wynisi:", pole
#
# try:
#     a = float(input("Podaj długość boku a "))
#     b = float(input("Podaj długość boku b "))
#     c = float(input("Podaj długość boku c "))
#
#     pole = oblicz_pole_trojkąta(a, b, c)
#
#     print(f"Pole trojkąta wynosi {pole}")
# except ValueError:
#     print("Wprowadzona wartość nie jest poprawna")


# 8
# def potega(a = float(input("Podaj podstawę (a): ")), n = int(input("Podaj wykładnik (n): "))):
#     # Warunek bazowy
#     if n == 0:
#         return 1  # Każda liczba do potęgi zerowej to 1
#     elif n < 0:
#         return 1 / potega(a, -n)  # Obsługa ujemnych potęg
#     else:
#         return a * potega(a, n - 1)  # Rekurencja: a^n = a * a^(n-1)
#
# print(potega())

# 10
# def odwracaj_string(s):
#
#     return s[::-1]
#
# odwrócony_string = odwracaj_string("hello")
# print(odwrócony_string)

#13
# def nwd(a, b):
#
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# a = 56
# b = 98
# print(f"NWD({a}, {b}) = {nwd(a, b)}")

#14
# def czy_palindrom(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]
#
# slowo = input("Slowo: ")
# if czy_palindrom(slowo):
#     print(f"{slowo} jest palindromem.")
# else:
#     print(f"{slowo} nie jest palindromem.")


