from collections import deque

petrol_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

petrol_data_copy = petrol_data.copy()

truck_fuel = 0
index = 0


while petrol_data_copy:
    tank_refuel, next_pump_distance = petrol_data_copy.popleft()
    truck_fuel += tank_refuel

    if truck_fuel >= next_pump_distance:
        truck_fuel -= next_pump_distance
    else:
        petrol_data.rotate(-1)
        truck_fuel = 0
        index += 1
        petrol_data_copy = petrol_data.copy()

print(index)
