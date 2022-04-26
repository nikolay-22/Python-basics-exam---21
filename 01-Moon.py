import math
speed = float(input())
consumption_100 = float(input())

#time = distance / speed + 3
distance = 384400 * 2
time = distance / speed + 3

consumption_1 = consumption_100 / 100
total_consumption = distance * consumption_1

print(math.ceil(time))
print(int(total_consumption))

