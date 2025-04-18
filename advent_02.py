# opcode 1 adds together nums read from two positions and stores result in a third position 
# ex: 1, 10, 20, 30
# This example should read index 10 and 20 and overwrite index 30

# opcode 2 is exactly the same, except it is multiplying

# once one opcode is done, move forward 4 indicies to the next opcode

# if opcode 99 is reached, break


# addition + overwrite element at pos_3
def opcode_1(a, current_pos):
    pos_1 = current_pos + 1 
    pos_2 = current_pos + 2 
    x = a[pos_1]
    y = a[pos_2]
    sum = a[x] + a[y]
    pos_3 = current_pos + 3
    z = a[pos_3]
    a[z] = sum


# multiplication + overwrite element at pos_3
def opcode_2(a, current_pos):
    pos_1 = current_pos + 1
    pos_2 = current_pos + 2
    x = a[pos_1]
    y = a[pos_2]
    product = a[x] * a[y]
    pos_3 = current_pos + 3
    z = a[pos_3]
    a[z] = product


def main():
    current_pos = 0
    a = []
    with open("advent_input02.txt", "r") as file:
        for line in file:
            nums = line.split(",")
            for num in nums:
                a.append(int(num))

    updated_list = a.copy()

    updated_list[1] = 12
    updated_list[2] = 2
    
    while current_pos < len(updated_list):
        if updated_list[current_pos] == 1:
            print("opcode_1 running")
            opcode_1(updated_list, current_pos)
            current_pos += 4
        elif updated_list[current_pos] == 2:
            print("opcode_2 running")
            opcode_2(updated_list, current_pos)
            current_pos += 4
        elif updated_list[current_pos] == 99:
            print("opcode_99 running")
            break
        else:
            current_pos += 1

    print("Original List:", a)
    print("Updated List:", updated_list)

    
if __name__ == "__main__":
    main()