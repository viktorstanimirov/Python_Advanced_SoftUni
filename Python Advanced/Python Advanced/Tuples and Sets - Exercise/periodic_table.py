number_of_elements = int(input())

chemical_elements = set()


for _ in range(number_of_elements):
    for elements in input().split():
        chemical_elements.add(elements)

print(*chemical_elements, sep="\n")
