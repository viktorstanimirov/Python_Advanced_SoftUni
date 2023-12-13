from collections import deque

worms = deque((int(x) for x in input().split()))
holes = deque((int(x) for x in input().split()))

matches = 0
all_holes = len(holes)

while worms and holes:

    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1

    else:
        curr_worm = worm - 3

        if curr_worm <= 0:
            continue
        else:
            worms.append(curr_worm)


if matches:
    print(f"Matches: {matches}")

else:
    print("There are no matches.")

if not worms and matches == all_holes:
    print("Every worm found a suitable hole!")

elif not worms and matches != all_holes:
    print("Worms left: none")

else:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if holes:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")
else:
    print("Holes left: none")




