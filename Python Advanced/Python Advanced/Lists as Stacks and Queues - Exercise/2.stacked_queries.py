from collections import deque

number_of_lines = int(input())
my_stack = deque()

for _ in range(number_of_lines):
    command_line = input().split()
    command = int(command_line[0])

    if command == 1:
        number = int(command_line[1])
        my_stack.append(number)
    elif command == 2:
        if my_stack:
            my_stack.pop()
    elif command == 3:
        if my_stack:
            print(max(my_stack))
    elif command == 4:
        if my_stack:
            print(min(my_stack))

my_stack.reverse()
print(*my_stack, sep=", ")
