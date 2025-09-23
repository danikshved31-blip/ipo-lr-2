import math
print("Введите чему равен объем шара = ")
V = float(input())
print(f"объем = {V} ед.³ ")
r = ((3 * pow( V, 1/3 )) / (4 * math.pi ))
print(f"радиус шара равен = {r} ед." )