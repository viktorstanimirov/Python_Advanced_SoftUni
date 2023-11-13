from collections import deque

clothes_quantity = deque((int(x)for x in input().split()))
rack_capacity = int(input())


current_capacity = rack_capacity
number_of_racks = 1


while clothes_quantity:
    clothes = clothes_quantity.pop()

    if current_capacity >= clothes:
        current_capacity -= clothes
    else:
        current_capacity = rack_capacity - clothes
        number_of_racks += 1


print(number_of_racks)