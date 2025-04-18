# NOTE: This AOC builds off Day 2 which includes the following opcode instructions
# opcode 1 adds together numbers read from two positoins and stores result in third position 
# ex: 1, 10, 20, 30

# opcode 2 multiplies inputs instead of adding

# two new instruction:

# opcode 3 takes in int as input and save it to the position given by its only parameter
# ex: instruction 3,50 would take an input value and store it at address 50

# opcode 4 OUTPUTS the value of its only parameter
# ex: 4,50 would output the value 50

# parameter modes:
# 0 = position mode 
# 1 = immediate mode 



# addition + overwrite element at pos_3 (now with mode consideration)
def opcode_1(a, current_pos, mode_1, mode_2):
    pos_1 = a[current_pos + 1]  
    pos_2 = a[current_pos + 2]  
    pos_3 = a[current_pos + 3] 

    if mode_1 == "0":
        x = a[pos_1]
    else:
        x = pos_1
    if mode_2 == "0":
        y = a[pos_2]
    else:
        y = pos_2

    a[pos_3] = x + y


# multiplication + overwrite element at pos_3 (now with mode consideration)
def opcode_2(a, current_pos, mode_1, mode_2):
    pos_1 = a[current_pos + 1]
    pos_2 = a[current_pos + 2] 
    pos_3 = a[current_pos + 3]

    if mode_1 == "0":
        x = a[pos_1]
    else:
        x = pos_1
    if mode_2 == "0":
        y = a[pos_2]
    else:
        y = pos_2

    a[pos_3] = x * y

# takes in integer as input and saves it to pos given by param
def opcode_3(a, x, current_pos):
    address = a[current_pos + 1]
    a[address] = x 
     
# simply outputs the val of its params 
def opcode_4(a, current_pos, mode):
    if mode == "0":
        address = a[current_pos + 1]
        print("Diagnostic Code:", a[address])
    else:
        print("Diagnostic Code:", a[current_pos + 1])

# DRY function to omit consant mode abstraction
def get_modes(instruction):
    modes = instruction // 100
    string_modes = str(modes)
    reversed_modes = string_modes[::-1].ljust(2, "0") # Fills in the rest of the zeros. ex: "1" => "100" 
    return reversed_modes

def main():
    current_pos = 0
    input_instruction = 1
    a = []
    with open("advent_input05.txt", "r") as file:
        for line in file:
            nums = line.split(",")
            for num in nums:
                a.append(int(num))

    updated_list = a.copy()
    
    while current_pos < len(updated_list):
        if updated_list[current_pos] % 100 == 1:
            modes = get_modes(updated_list[current_pos])
            opcode_1(updated_list, current_pos, modes[0], modes[1])
            current_pos += 4
        elif updated_list[current_pos] % 100 == 2:
            modes = get_modes(updated_list[current_pos])
            opcode_2(updated_list, current_pos, modes[0], modes[1])
            current_pos += 4
        elif updated_list[current_pos] % 100 == 3:
            opcode_3(updated_list, input_instruction, current_pos)
            current_pos += 2
        elif updated_list[current_pos] % 100 == 4:
            modes = get_modes(updated_list[current_pos])
            opcode_4(updated_list, current_pos, modes[0])
            current_pos += 2
        elif updated_list[current_pos] % 100 == 99:
            break
        else:
            current_pos += 1
    
if __name__ == "__main__":
    main()