def calculate_fuel(mass, total):
    fuel = int(mass / 3) - 2
    if fuel <= 0:
        return total

    total += fuel
    return calculate_fuel(fuel, total)


with open('part_one_input.txt', 'r') as file:
    total = 0

    for l in file:
        total = calculate_fuel(int(l), total)

    print(total)