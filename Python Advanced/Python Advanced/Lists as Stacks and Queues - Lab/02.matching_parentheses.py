stack_parentecis = []

text = input()

for index in range(len(text)):

    if text[index] == "(":
        stack_parentecis.append(index)
    elif text[index] == ")":
        start_possition = stack_parentecis.pop()
        end_possition = index
        print(text[start_possition:end_possition + 1])
