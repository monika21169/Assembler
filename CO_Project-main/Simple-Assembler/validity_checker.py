from all_constants import *
from helpers import *
from math import log2, floor

def isValidInstr(inst: str, variables: list, memory:dict) -> tuple:
    """Return True if the instruction is a valid instruction, else returns false
    
    Parameter
    -------
    inst : str
        The instruction to be evaluated
    variables : list
        list of variables that have been added already
    memory : dict
        list of labels defined in the program
    """
    
    instToken = inst.split()
    validIns = isInstruction(instToken[0])
    if not (validIns): # Returning false if Instruction is not a valid instruction
        return False, "Instruction given is not a valid instruction"

    type = returnType(inst)

    type_struct = type_structure[type]

    #iterating through all the elements of the instruction and making sure all are correct
    i = 0
    for j in type_struct:
        # try:
            if j == "unused":
                continue

            if j == "opcode":
                i+=1    
                continue

            elif j == "memory":
                if type == 'd':
                    if not inVars(instToken[i], variables):
                        return False , f"'{instToken[i]}' variable not defined"
                elif type == "e":
                    if not inMemory(instToken[i], memory):
                        return False, f"'{instToken[i]}' label used is not defined"


            elif j == "immediate":
                if instToken[i][0] != "$":
                    return False, "Immediate value missing"
                
                try:
                    intVal = (int(instToken[i][1:]))
                    if intVal > MAX_IMM_VALUE:
                        return False, "Immediate value greater than memory size"
                    elif intVal < 0:
                        return False, "Immediate value less than 0"
                except ValueError:
                    return False, "Immediate value must be an integer"

            elif j == "reg":
                if not isRegister(instToken[i]):
                    return False, f"'{instToken[i]}' is not a Valid Register"
                
                if instToken[i] == 'FLAGS':
                    if (i != 1) or instToken[0] != "mov":
                        return False, "Illegal use of flag"
            i+=1
        # except:
        #     return False, "Something went terribly wrong. Should check up on that"

    return True, "" # returning true with an empty string if all checks pass

def weakIsLabel(inst:str, variables:list, memory:dict) -> tuple:
    """A weaker version of the isValidLabel instruction"""
    inst = inst.split()
    if (inst[0][-1] != ":"):
        return False, "Colon missing after label"

    validName = isValidName(inst[0][:-1], variables, memory=memory)
    if not validName:
        return False, "Label name cannot be an instruction, an already existing variable name or memory address or empty"
    return True, ""


def isValidLabel(inst: str, variables: list, memory: dict) -> tuple:
    """Returns True if it's a valid label, and returns false otherwise
    Also returns an empty string if it's a label, and error message otherwise
    Parameter
    -------
    inst : str
        The instruction to be evaluated
    variables : list
        list of variables that have been added already
    memory : dict
        list of labels defined in the program
    """

    # inst = inst.split()
    # if (inst[0][-1] != ":"):
    #     return False, "Colon missing after label"
    inst = inst.split()
    validName = inMemory(inst[0][:-1], memory=memory)
    if not validName:
        return False, "Weird unexpected behavior happened"

    temp = " ".join(inst[1:])
    temp1, temp2 = isValidInstr(temp, variables=variables, memory=memory)
    return temp1, temp2

# def notValid(inst:str, variables:list, memory:str) -> bool:
#     """Return true if an instruction is valid at all or not"""
#     pass

def main():
    """For Testing only"""
    variables = [{"abc": 10, "asdwe": 11, "asdawd":12}]
    memory = {'label': 7}
    print(isValidLabel("label: hlt", variables=variables, memory=memory))


if __name__ == "__main__":
    main()