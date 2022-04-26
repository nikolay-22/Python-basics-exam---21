import math
import sys
number_of_airlines = int(input())
average_per_previous_airline = -sys.maxsize

for i in range(1, number_of_airlines + 1):
    airline_name = input()
    total_per_this_airline = 0
    average_for_the_airline = 0
    flights_per_airline = 0
    while True:
        command = input()
        if command != "Finish":
            flights_per_airline += 1
            passengers_in_the_flight = int(command)
            total_per_this_airline += passengers_in_the_flight
            average_for_the_airline = total_per_this_airline / flights_per_airline
        else:
            print(f"{airline_name}: {math.floor(average_for_the_airline)} passengers.")
            if average_for_the_airline >= average_per_previous_airline:
                average_per_previous_airline = average_for_the_airline
                biggest_airline = airline_name
                biggest_airline_average = average_for_the_airline
            break

print(f"{biggest_airline} has most passengers per flight: {math.floor(biggest_airline_average)}")