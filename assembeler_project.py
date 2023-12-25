#                                             ASSEMBELER PROJECT FOR COMPUTER ARCHITECTURE
#                                                  MOHAMMAD-MAHDI KHANI    40021973142
from prettytable import PrettyTable
import os
def assemble(assembly_program):
    address=0
    for line in assembly_program:
        tokens=line.split()
        if tokens[0]=="ORG":
            org_number=int(tokens[1])
            address=hex_number(org_number)
        elif tokens[0]=="END":
            break
# ---------------------------------------------------------MEMORY INSTRUCTIONS-----------------------------------------------------
        elif tokens[0]=="AND":
            address=hex_number(address)
            hex_location.append(address)
            if  len(tokens)==2:   
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("AND"+" "+operand_address)
                instruction_2.append("0"+operand_address)
            elif len(tokens)==3:
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("AND"+" "+operand_address)
                if tokens[2]=="I":
                    instruction_2.append("8"+operand_address)    
            else:
                instruction_1.append("AND")

        elif tokens[0]=="ADD":
            address=hex_number(address)
            hex_location.append(address)
            if  len(tokens)==2:   
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("ADD"+" "+operand_address)
                instruction_2.append("1"+operand_address)
            elif len(tokens)==3:
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("ADD"+" "+operand_address)
                if tokens[2]=="I":
                    instruction_2.append("9"+operand_address)    
            else:
                instruction_1.append("ADD")
                
        elif tokens[0]=="LDA":
            address=hex_number(address)
            hex_location.append(address)
            if  len(tokens)==2:   
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("LDA"+" "+operand_address)
                instruction_2.append("2"+operand_address)
            elif len(tokens)==3:
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("LDA"+" "+operand_address)
                if tokens[2]=="I":
                    instruction_2.append("a"+operand_address)    
            else:
                instruction_1.append("LDA")

        elif tokens[0]=="STA":
            address=hex_number(address)
            hex_location.append(address)
            if  len(tokens)==2:   
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("STA"+" "+operand_address)
                instruction_2.append("3"+operand_address)
            elif len(tokens)==3:
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("STA"+" "+operand_address)
                if tokens[2]=="I":
                    instruction_2.append("b"+operand_address)    
            else:
                instruction_1.append("STA")
        
        elif tokens[0]=="BUN":
            address=hex_number(address)
            hex_location.append(address)
            if  len(tokens)==2:   
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("BUN"+" "+operand_address)
                instruction_2.append("4"+operand_address)
            elif len(tokens)==3:
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("BUN"+" "+operand_address)
                if tokens[2]=="I":
                    instruction_2.append("c"+operand_address)    
            else:
                instruction_1.append("BUN")

        elif tokens[0]=="BSA":
            address=hex_number(address)
            hex_location.append(address)
            if  len(tokens)==2:   
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("BSA"+" "+operand_address)
                instruction_2.append("5"+operand_address)
            elif len(tokens)==3:
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("BSA"+" "+operand_address)
                if tokens[2]=="I":
                    instruction_2.append("d"+operand_address)    
            else:
                instruction_1.append("BSA") 

        elif tokens[0]=="ISZ":
            address=hex_number(address)
            hex_location.append(address)
            if  len(tokens)==2:   
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("ISZ"+" "+operand_address)
                instruction_2.append("6"+operand_address)
            elif len(tokens)==3:
                operands_counter=0
                for i in operands:
                    if operands[operands_counter]["operand"]==tokens[1]:
                        operand_number=operands[operands_counter]["location"]
                        break
                    operands_counter+=1
                operand_address=+operand_number
                operand_address=hex_number(operand_address)
                instruction_1.append("ISZ"+" "+operand_address)
                if tokens[2]=="I":
                    instruction_2.append("e"+operand_address)    
            else:
                instruction_1.append("ISZ")
# -----------------------------------------REGISTER INSTRUCTIONS---------------------------------------------------------------
        elif tokens[0]=="CLA":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("CLA")
            instruction_2.append("7800")

        elif tokens[0]=="CLE":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("CLE")
            instruction_2.append("7400")

        elif tokens[0]=="CMA":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("CMA")
            instruction_2.append("7200")            

        elif tokens[0]=="CME":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("CME")
            instruction_2.append("7100")  

        elif tokens[0]=="CIR":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("CIR")
            instruction_2.append("7080")

        elif tokens[0]=="CIL":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("CIL")
            instruction_2.append("7040")    

        elif tokens[0]=="INC":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("INC")
            instruction_2.append("7020")  

        elif tokens[0]=="SPA":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("SPA")
            instruction_2.append("7010")  

        elif tokens[0]=="SNA":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("SNA")
            instruction_2.append("7008")

        elif tokens[0]=="SZA":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("SZA")
            instruction_2.append("7004")    

        elif tokens[0]=="SZE":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("SZE")
            instruction_2.append("7002")  

        elif tokens[0]=="HLT":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("HLT")
            instruction_2.append("7001")  
# ------------------------------------------------INPUT OUTPUT INSTRUCTIONS---------------------------------------------------

        elif tokens[0]=="INP":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("INP")
            instruction_2.append("f800")  

        elif tokens[0]=="OUT":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("OUT")
            instruction_2.append("f400")  

        elif tokens[0]=="SKI":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("SKI")
            instruction_2.append("f200")

        elif tokens[0]=="SKO":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("SKO")
            instruction_2.append("f100")    

        elif tokens[0]=="ION":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("ION")
            instruction_2.append("f080")  

        elif tokens[0]=="IOF":
            address=hex_number(address)
            hex_location.append(address)
            instruction_1.append("IOF")
            instruction_2.append("f040")  
# ----------------------------------------------------OTHER---------------------------------------------------
        
        else :
            operand_finder2(tokens)
            new_token=""
            for i in tokens[0]:
                if i==",":
                    break
                new_token=new_token+i
            tokens[0]=new_token    
            operands_counter=0
            for i in operands:
                if tokens[0] == operands[operands_counter]["operand"]:
                    address=hex_number(address)
                    hex_location.append(address)
                    break
                operands_counter+=1

        address=int(address)
        if tokens[0]!="ORG":
            address+=1
# ---------------------------------------------------FUNCTIONS----------------------------------------------------------

def operand_finder(assembly_program):
    line_counter=0
    for line in assembly_program:
            tokens=line.split()
            if tokens[0]=="ORG":
                line_counter=int(tokens[1])
            if "DEC" in tokens:
                hex_line=line_counter
                operand=""
                for i in tokens[0]:
                    if i == ",":
                        break
                    operand=operand+i
                operands.append({
                    "location":hex_line,
                    "operand":operand
                })
            if "HEX" in tokens:
                hex_line=line_counter
                operand=""
                for i in tokens[0]:
                    if i == ",":
                        break
                    operand=operand+i
                operands.append({
                    "location":hex_line,
                    "operand":operand
                })
            if tokens[0]!="ORG" and tokens[0]!="END":    
                line_counter+=1
                
def operand_finder2(tokens):
    if "DEC" in tokens:
        instruction=decimal_to_hexadecimal(int(tokens[2]))
        instruction_1.append(instruction)
        instruction_2.append(instruction)
    if "HEX" in tokens:
        instruction=hex_to_4bit_hex(int(tokens[2]))
        instruction_1.append(instruction)
        instruction_2.append(instruction)
         
def decimal_to_hexadecimal(decimal_number):
    hex_number = hex(decimal_number & 0xFFFFFFF)[-4:]
    hex_number = format(int(hex_number, 16), '04X')
    return hex_number

def hexadecimal_to_binary(hexadecimal_number):
    binary_number = bin(int(hexadecimal_number, 16))[2:]
    return binary_number

def hexadecimal_to_binary_16_bits(hexadecimal_number):
    binary_number = format(int(hexadecimal_number, 16), '016b')
    return binary_number

def hex_number(decimal_number):  
    hex_number = str(decimal_number)
    if len(hex_number) < 2:
        hex_number = '00' + hex_number
    if len(hex_number) == 2:
        hex_number = '0' + hex_number
    return hex_number    

def hex_to_4bit_hex(hex_number):
    hex_4bit=str(hex_number)
    if len(hex_4bit) == 1:
        hex_4bit='000'+hex_4bit
    elif len(hex_4bit) == 2:
        hex_4bit='00'+hex_4bit 
    elif len(hex_4bit) == 3:
        hex_4bit='0'+hex_4bit    
    return hex_4bit
# -------------------------------------------------------INPUT STRING-------------------------------------------
assembly_program = [
    "ORG 0",
    "LDA A",
    "ADD B",
    "STA C",
    "HLT",
    "A, DEC 83",
    "B, DEC -23",
    "C, DEC 0",
    "END",
]
# -----------------------------------------------------------TOOLS-----------------------------------------------
hex_location=[]
instruction_1=[]
instruction_2=[]
operands=[]
instruction_1=[]
instruction_code=[]
final_location=[]
program_with_symbolic_opcode=PrettyTable(["Location" , "instruction"])
hexa_program=PrettyTable(["Location" , "instruction"])
binary_program=PrettyTable(["Location" , "instruction code"])
# --------------------------------------------------------DISPLAY OUT--------------------------------------------
operand_finder(assembly_program)
assemble(assembly_program)
os.system("cls")
print("PROGRAM WITH SYMBOLIC OP_CODE")
for i in range(len(instruction_1)):
    program_with_symbolic_opcode.add_row([hex_location[i] , instruction_1[i]])
print(program_with_symbolic_opcode)

print("\n")
print("HEXA PROGRAM")
for i in range(len(instruction_2)):
    hexa_program.add_row([hex_location[i] , instruction_2[i]])
print(hexa_program)    

print("\n")
print("BINARY PROGRAM")
for i in range(len(instruction_2)):
    final_location.append(hexadecimal_to_binary(hex_location[i]))
    instruction_code.append(hexadecimal_to_binary_16_bits(instruction_2[i]))
    binary_program.add_row([final_location[i] , instruction_code[i]])
print(binary_program)
    # -----------------------------------------------FINISH----------------------------------------------------