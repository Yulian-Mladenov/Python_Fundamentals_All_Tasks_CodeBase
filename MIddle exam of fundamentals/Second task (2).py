sequence = input().split()
sequence = [int(num) for num in sequence]

while True:
    command = input()
    if command == "END":
        break

    parts = command.split()
    action = parts[0]

    if action == "add" and parts[2] == "start":
        numbers_to_add = [int(num) for num in parts[3:]]
        sequence = numbers_to_add + sequence

    elif action == "remove" and parts[1] == "greater":
        value = int(parts[3])
        sequence = [num for num in sequence if num <= value]

    elif action == "replace":
        value = int(parts[1])
        replacement = int(parts[2])
        if value in sequence:
            index = sequence.index(value)
            sequence[index] = replacement

    elif action == "remove" and parts[1] == "at":
        index = int(parts[3])
        if 0 <= index < len(sequence):
            sequence.pop(index)

    elif action == "find":
        if parts[1] == "even":
            evens = [str(num) for num in sequence if num % 2 == 0]
            print(" ".join(evens))
        elif parts[1] == "odd":
            odds = [str(num) for num in sequence if num % 2 != 0]
            print(" ".join(odds))

print(", ".join(str(num) for num in sequence))
