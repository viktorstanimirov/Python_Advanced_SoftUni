from string import punctuation

with open("../File_Handling/text.txt", "r") as file:
    text = file.readlines()

output_file = open("../File_Handling/output.txt", "w")

for el in range(len(text)):

    letters, marks = 0, 0

    for symbol in text[el]:

        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {el + 1}: {''.join(text[el][:-1])} ({letters})({marks})\n")

output_file.close()