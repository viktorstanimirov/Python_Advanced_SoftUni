longest_intersection = []

for _ in range(int(input())):
    first_start_end_nums, second_srart_end_nums = [el.split(",") for el in input().split("-")]

    first_range = set(range(int(first_start_end_nums[0]), int(first_start_end_nums[1]) + 1))
    second_range = set(range(int(second_srart_end_nums[0]), int(second_srart_end_nums[1]) + 1))

    intersection = first_range.intersection(second_range)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(
    f"Longest intersection is [{', '.join(str(num) for num in longest_intersection)}]"
    f" with length {len(longest_intersection)}")
