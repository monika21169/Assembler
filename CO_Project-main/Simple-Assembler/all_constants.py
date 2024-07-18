"""Program where all the data from the json files
will be extracted and stored in python for ease of access"""

import json
import pprint
import string

validChars = set(string.ascii_letters + string.digits + "_")
# Defining the dictionaries

opcodes = {
    "type-a" : {},
    "type-b" : {},
    "type-c" : {},
    "type-d" : {},
    "type-e" : {},
    "type-f" : {}
}
terms = no_of_register = {}
unused_bits = memory_bits = {}
immediate_values = register_addr = {}

MAX_IMM_VALUE = 2**8 - 1
MAX_NO_OF_INSTRUCTIONS = 2**8


#Extracting data from them
with open("ISA_Instructions.json") as f:
    temp = json.load(f)["opcode"]

    for i in temp:
        if i[2] == "a":     opcodes["type-a"][i[0]] = i[1]
        elif i[2] == "b":   opcodes["type-b"][i[0]] = i[1]
        elif i[2] == "c":   opcodes["type-c"][i[0]] = i[1]
        elif i[2] == "d":   opcodes["type-d"][i[0]] = i[1]
        elif i[2] == "e":   opcodes["type-e"][i[0]] = i[1]
        elif i[2] == "f":   opcodes["type-f"][i[0]] = i[1]

with open("other_constants.json") as f:
    temp = json.load(f)
    terms = temp["terms"]
    no_of_register = temp["no_of_registers"]
    unused_bits = temp["unused_bits"]
    memory_bits = temp["memory_bits"]
    immediate_values = temp["immediate_values"]
    register_addr = temp["register_addr"]
    type_structure = temp["type_structure"]



# For testing
def main():
    pprint.pprint(opcodes, width=1)
    # print((opcodes.keys()))

if __name__ == "__main__":
    pprint.pprint(opcodes, width=1)
    print(opcodes)