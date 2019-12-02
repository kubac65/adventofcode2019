target = 19690720

with open('input.txt', 'r') as file:
    master = [int(i) for i in file.read().replace('\n', '').strip().split(',')]

    for i in range(0, 100, 1):
        for j in range(0, 100, 1):
            ints = list(master)
            idx = 0
            ints[1] = i
            ints[2] = j
            
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

            if ints[0] == target:
                print(100 * i + j)
                break
