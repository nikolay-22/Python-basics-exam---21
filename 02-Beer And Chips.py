import math
name = input()
budget = float(input())
beers = int(input())
chips = int(input())

beer_single_price = 1.20
beers_price = beers * beer_single_price
chips_single_price = beers_price * 0.45
chips_price = math.ceil(chips * chips_single_price)
total_sum = beers_price + chips_price
money_left = budget - total_sum

if money_left >= 0:
    print(f"{name} bought a snack and has {money_left:.2f} leva left.")
else:
    print(f"{name} needs {abs(money_left):.2f} more leva!")
