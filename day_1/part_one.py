total = 0
with open('part_one_input.txt', 'r') as file:
    for l in file:
        module = int(l)
        fuel = int(module / 3) - 2
        total += fuel

print(total)