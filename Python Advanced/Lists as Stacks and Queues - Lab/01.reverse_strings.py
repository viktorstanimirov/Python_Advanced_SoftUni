string = (input())

reversed_string = list(string)


while reversed_string:
    removed_chars = reversed_string.pop()
    print(removed_chars, end='')