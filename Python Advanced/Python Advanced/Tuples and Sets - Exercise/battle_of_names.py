input_line = int(input())

odd_numbers = set()
even_numbers = set()
sum_letters = 0

for el in range(1, input_line + 1):
    name_line = input()

    for char in name_line:
        sum_letters += ord(char)

    sum_letters = (sum_letters // el)

    if sum_letters % 2 == 0:
        even_numbers.add(sum_letters)
        sum_letters = 0

    else:
        odd_numbers.add(sum_letters)
        sum_letters = 0

if sum(odd_numbers) > sum(even_numbers):
    print(*odd_numbers.difference(even_numbers), sep=', ')

else:
    print(odd_numbers.symmetric_difference(even_numbers), sep=', ')



