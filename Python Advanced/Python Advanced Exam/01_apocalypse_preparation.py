from collections import deque

textiles = deque((int(x) for x in input().split()))
medicaments = deque((int(x) for x in input().split()))

crafted_items = {}

while True:

    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
        break

    elif not textiles:
        print("Textiles are empty.")
        break

    elif not medicaments:
        print("Medicaments are empty.")
        break
    textile = textiles.popleft()
    medicament = medicaments.pop()
    resoureces_nedded = textile + medicament

    if resoureces_nedded == 30:
        healing_item = "Patch"

        if healing_item not in crafted_items:
            crafted_items[healing_item] = 1
        else:
            crafted_items[healing_item] += 1


    elif resoureces_nedded == 40:
        healing_item = "Bandage"

        if healing_item not in crafted_items:
            crafted_items[healing_item] = 1

        else:
            crafted_items[healing_item] += 1

    elif resoureces_nedded == 100:
        healing_item = "MedKit"

        if healing_item not in crafted_items:
            crafted_items[healing_item] = 1

        else:
            crafted_items[healing_item] += 1

    elif resoureces_nedded > 100:
        resoureces_nedded -= 100
        medicaments.append(resoureces_nedded)
        crafted_items["MedKit"] += 1

    else:
        medicament += 10
        medicaments.append(medicament)
        textiles.append(textile)

sorted_crafted_items = sorted(crafted_items.items(), key=lambda kvp: -kvp[1])

for key, value in sorted_crafted_items:
    print(key, value, sep= ' - ')

if medicaments:
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments][::-1])}")

elif textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles][::-1])}")
