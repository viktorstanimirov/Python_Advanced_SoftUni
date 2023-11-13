from collections import deque

tool_element = deque((int(x) for x in input().split()))
substance_element = deque((int(x) for x in input().split()))
sequence = input().split()

while True:

    if not sequence:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

    elif not tool_element or not substance_element:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break

    tool = tool_element.popleft()
    substance = substance_element.pop()
    seq_to_remove = str(tool * substance)

    if seq_to_remove in sequence:
        sequence.remove(seq_to_remove)

    else:
        tool += 1
        tool_element.append(tool)

        substance -= 1

        if substance > 0:
            substance_element.append(substance)

if tool_element:
    print(f"Tools: {', '.join([str(x) for x in tool_element])}")

if substance_element:
    print(f"Substances: {', '.join([str(x) for x in substance_element])}")

if sequence:
    print(f"Challenges: {', '.join([str(x) for x in sequence])}")
