# MIPS Instruction module

class MIPSinstruction:

    def __init__(self, inst_type, inst_name, opcode, reg1, reg2, reg3):
        self.inst_type = inst_type
        self.inst_name = inst_name
        self.opcode = opcode
        self.reg1 = reg1
        self.reg2 = reg2
        self.reg3 = reg3

    def __str__(self):
        return str(inst_name) + " " + str(reg1) + " " + str(reg2) + " " + str(reg3)
