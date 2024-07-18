from all_constants import *
from validity_checker import *
from generateBinary import returnBinary
import helpers

# taking in the input from stdin
instructions = []
while True:
    try:
        instructions.append(input())
    except EOFError:
        break

instructions = [i for i in instructions if i] # removing empty lines

#Creating output list
output = []

#variables to be used while generating the binary code
mem_addr_vars = {} #format label : instruction_number
variables = [] # variables defined at the start of the program. It will store dictionaries of format name:address
line_counter = 0

# main loop
def main():

    for j, inst in enumerate(instructions):
        #if there are more than 256 instructions, throw error

        if j > MAX_NO_OF_INSTRUCTIONS:
            print("Error: Memory overflow")
            return

        #checking if it's a variable
        isvar, name = helpers.isVar(inst, variables=variables, memory=mem_addr_vars)
        if isvar:
            variables.append({name: 0})
        else:
            if name:
                print(f"Error found in line {j+1}: {name}")
                return
            break

    line_counter = len(instructions) - j
    memory_add = line_counter+1

    #assigning memory address to variables
    for i in variables:
        key = list(i.keys())[0]
        i[key] = memory_add
        memory_add+=1

    #parsing for labels
    for index, inst in enumerate(instructions[j:]):
        
        if helpers.overflow(index+j):
            print(helpers.overflow(index+j))
            return
        
        if (weakIsLabel(inst, variables=variables, memory=mem_addr_vars))[0]:
            inst = inst.split()
            mem_addr_vars[inst[0][:-1]] = index
        else:
            instToken = inst.split()
            if (instToken[0][-1] == ":"):
                print(f"Error found in line {index+j+1}: {(weakIsLabel(inst, variables=variables, memory=mem_addr_vars))[1]}")
                return

    # main loop for generating binary code
    for index, inst in enumerate(instructions[j:]):
        
        validInst, instMessage = isValidInstr(inst, variables=variables, memory=mem_addr_vars)
        validLabel, labelMessage = isValidLabel(inst, variables=variables, memory=mem_addr_vars)

        #overflow condition
        if helpers.overflow(index+j):
            print(helpers.overflow(index+j))
            return

        # If there is some variable declaration after all the variables have been declared at the top
        if isVar(inst, variables=variables, memory=mem_addr_vars)[0]:
            print(f"Error found in line {index+j+1}: Variable definition after all variables have been declared")
            return

        # If instruction is a valid label, or a valid instruction
        if (validLabel):
            instToken = inst.split()
            tempInst = " ".join(instToken[1:])
            output.append(returnBinary(tempInst, variables=variables, memory=mem_addr_vars))

            #making sure last instruction is always hlt
            if helpers.returnType(tempInst) == "f":
                if (index+j+1) != len(instructions):
                    print(f"Error found in line {index+j+2}: Instructions after hlt are invalid")
                    return
            continue
        
        if validInst:
            output.append(returnBinary(inst, variables=variables, memory=mem_addr_vars))
            if helpers.returnType(inst) == "f":
                if (index+j+1) != len(instructions):
                    print(f"Error found in line {index+j+2}: Instructions after hlt are invalid")
                    return
            continue
        
        # If instruction is not a valid instruction, or label
        if (not validLabel):
            if (not validInst):
                print(f"Error found in line {index+j+1}: {instMessage}")
                return
            else:
                print(f"Error found in line {index+j+1}: {labelMessage}")
                return

    #checking that hlt instruction is present
    try:
        if instructions[-1] != 'hlt' and instructions[-1].split()[1] != 'hlt':
            print(f"Error in line {index+j+1}: hlt instruction missing")
            return
    except IndexError:
        if instructions[-1] != 'hlt':
            print(f"Error in line {index+j+1}: hlt instruction missing")
            return
        

    for i in output:
        print(i)


main()
    

# if Error:
#     print("Program did not compile properly\n")

# hlt or label: hlt