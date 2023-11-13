from collections import deque

wather_quantity = int(input())
people_names = input()

people_for_wather = deque()


while people_names != "Start":
    people_for_wather.append(people_names)
    people_names = input()

while True:
    command_line = input().split()
    command = command_line[0]
    if command == "End":
        break

    if len(command_line) == 1:
        needed_wather = int(command_line[0])
        if wather_quantity >= needed_wather:
            wather_quantity -= needed_wather
            print(f"{people_for_wather.popleft()} got water")
        else:
            print(f"{people_for_wather.popleft()} must wait")

    else:
        wather_refill = int(command_line[1])
        wather_quantity += wather_refill

print(f"{wather_quantity} liters left")
