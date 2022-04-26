food_qty_kg = int(input())
food_qty_g = food_qty_kg * 1000
enough_food = True

while True:
    command = input()
    if command == "Adopted":
        break
    else:
        food_eaten = int(command)
        food_qty_g -= food_eaten
    if food_qty_g >= 0:
        continue
    else:
        enough_food = False
        #break

if enough_food:
    print(f"Food is enough! Leftovers: {food_qty_g} grams.")
else:
    print(f"Food is not enough. You need {abs(food_qty_g)} grams more.")


