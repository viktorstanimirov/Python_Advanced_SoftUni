symbols = ["-", ",", ".", "!", "?"]


with open("../File_Handling/text.txt") as file:
    text = file.readlines()

for el in range(0, len(text), 2):

    for symbol in symbols:
        text[el] = text[el].replace(symbol, "@")

    print(*text[el].split()[::-1], sep=" ")