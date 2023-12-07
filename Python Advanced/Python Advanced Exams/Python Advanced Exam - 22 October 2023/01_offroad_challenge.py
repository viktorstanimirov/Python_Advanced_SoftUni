from collections import deque

initial_fuel = deque((int(x) for x in input().split()))
consumption_index = deque((int(x) for x in input().split()))
fuel_needed = list((int(x) for x in input().split()))

reached_points = 0
result = []
is_finished = False
while initial_fuel:

    fuel = initial_fuel.pop()
    consumption = consumption_index.popleft()
    fuel_left = fuel - consumption
    altitude = fuel_needed[reached_points]

    if fuel_left >= altitude:
        reached_points += 1
        result.append(f'Altitude {reached_points}')
        print(f"John has reached: Altitude {reached_points}")
    elif fuel_left < altitude or fuel_left == 0 and initial_fuel != 0:

        if reached_points == 0:
            print("John failed to reach the top.")
            print("John didn't reach any altitude.")

        reached_points += 1
        print(f"John did not reach: Altitude {reached_points}")
        print(f"John failed to reach the top.")

        break

    if reached_points == len(fuel_needed):
        is_finished = True
        print("John has reached all the altitudes and managed to reach the top!")
        break

if not is_finished:
    print(f"Reached altitudes: {', '.join(result)}")
