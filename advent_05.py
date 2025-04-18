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
# 0 = position mode (if the param is 50, its value is the value stored at address 50 (which would be 3 in the example above))
# 1 = immediate mode (param is interpreted as a value (if param is 50, value is 50))

# NOTE: opcode is a 2 digit number based only on the ones and tens digit of a value in an instruction
# NOTE: Param modes are single digits, one per param, read right-to-left from the opcode: the first param's mode is hundredths, second param's mode if thousandths, third param mode is ten-thousands, and so on
# NOTE: any missing modes are 0

# ex: 1002, 4, 3, 4, 33
# the first instruction 1002, 4, 3, 4 is a multiply instruction
# the rightmost two digits of the first value (02) indicate opcode 2, multiplication
# then, from right to left, params nodes are 0 (hundreds), 1 (thousands), and 0 (ten-thousands (even if not present))

# this instruction multiplies the first 2 params. the first param 4 in position mode, works like it did before -
# - its value is the value stored at address 4 (33)
# the second param 3 is in immediate mode, simply has value of 3. the result is 33 * 3 (because we are multiplying)
# the third param 4 is in position mode, whic also works like it did before - 00 is written to address 4

# NOTE: instruction pointer should increase by the num of vals in instruction after instruction finish. because of this, the amount is no longer always 4
# NOTE: integers can be negative: 1101, 100, -1, 4, 0 is a valid program (find 100 + -1), store the result in position 4


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

# takes in integer as input and saves it to pos given by param
def opcode_3(a, x, address):
    a[address] = x
     

# simply outputs the val of its params 
def opcode_4(a, address):
    print("Output Instruction:", a[address]) 

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

    updated_list[1] = 12
    updated_list[2] = 2
    
    while current_pos < len(updated_list):
        str_pos = str(current_pos)
        element = updated_list[current_pos]
        if "01" in str_pos or element == 1:
            print("opcode_1 running")
            # TODO: IMPLEMENT PARAMETER MODE
            opcode_1(updated_list, current_pos)
            current_pos += 4
        elif "02" in str_pos or element == 2:
            print("opcode_2 running")
            opcode_2(updated_list, current_pos)
            current_pos += 4
        elif "03" in str_pos or element == 3:
           print("opcode_3 running")
           opcode_3(updated_list, input_instruction, current_pos)
           current_pos += 2
        elif "04" in str_pos or element == 4:
           print("opcode_4 running")
           opcode_4(updated_list, current_pos)
           current_pos += 2
        elif updated_list[current_pos] == 99:
            print("opcode_99 running")
            break
        else:
            current_pos += 1

    print("Original List:", a)
    print("Updated List:", updated_list)

    
if __name__ == "__main__":
    main()