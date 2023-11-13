set_a_numbers, set_b_numbers = [int(x) for x in input().split()]

first_set_nums = {int(input()) for _ in range(set_a_numbers)}
second_set_nums = {int(input()) for _ in range(set_b_numbers)}


print(*first_set_nums.intersection(second_set_nums), sep="\n")
