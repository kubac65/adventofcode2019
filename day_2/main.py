
with open('input.txt', 'r') as file:
    ints = [int(i) for i in file.read().replace('\n', '').strip().split(',')]

    idx = 0

    ints[1] = 12
    ints[2] = 2
    while True:
        op = ints[idx]
        if op == 99:
            break

        a = ints[ints[idx+1]]
        b = ints[ints[idx+2]]
        res_pos = ints[idx+3]

        if op == 1:
            ints[res_pos] = a + b
        elif op == 2:
            ints[res_pos] = a * b
        else:
            print("This ain't working")
            print(f"Opcode: {op}\nIndex: {idx}")
            break

        idx += 4

    print(ints[0])
