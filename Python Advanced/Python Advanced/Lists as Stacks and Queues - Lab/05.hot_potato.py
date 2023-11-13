from collections import deque

kids_names = deque(input().split())
rotation_num = int(input())

while len(kids_names) > 1:
    kids_names.rotate(-rotation_num - 1)
    removed_kid = kids_names.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {kids_names.popleft()}")