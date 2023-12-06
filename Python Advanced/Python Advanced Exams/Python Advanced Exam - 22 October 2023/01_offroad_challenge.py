from collections import deque

initial_fue = deque((int(x) for x in input().split()))
consumption = deque((int(x) for x in input().split()))
fuel_needed = input().split()



print(initial_fue)
print(consumption)
print(fuel_needed)