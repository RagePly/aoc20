
# TASK 1 =========================================================================================================================
with open("data/day8.txt", "r") as f:
    program = [(x.strip().split(" ")[0], int(x.strip().split(" ")[1][1:]), "+" in x.strip().split(" ")[1]) for x in f.readlines()]

programPointer = 0
accumulator = 0
executedOperations = []
while programPointer < len(program):
    if programPointer in executedOperations:
        print(accumulator)
        break

    executedOperations.append(programPointer)
    instruction = program[programPointer]
    opcode = instruction[0]
    value = instruction[1] if instruction[2] else - instruction[1]

    if opcode == "acc":
        accumulator += value
    elif opcode == "jmp":
        programPointer += value
        continue

    programPointer += 1
else:
    print("Oops")


# TASK 2 =========================================================================================================================
import copy

def executeProgram(program: list) -> (bool, int): # Returns true if the program executed without looping
    programPointer = 0
    accumulator = 0
    executedOperations = []
    while programPointer < len(program):
        if programPointer in executedOperations:
            return (False, accumulator)
            break

        executedOperations.append(programPointer)
        
        instruction = program[programPointer]
        opcode = instruction[0]
        value = instruction[1] if instruction[2] else - instruction[1]

        if opcode == "acc":
            accumulator += value
        elif opcode == "jmp":
            programPointer += value
            continue

        programPointer += 1
    else:
        return (True, accumulator)

with open("data/day8.txt", "r") as f:
    prog = [[x.strip().split(" ")[0], int(x.strip().split(" ")[1][1:]), "+" in x.strip().split(" ")[1]] for x in f.readlines()]

nopInstructions = [i for i in range(0,len(prog)) if prog[i][0] == "nop"]
jmpInstructions = [i for i in range(0,len(prog)) if prog[i][0] == "jmp"]

for i in nopInstructions:
    prog_cpy = copy.deepcopy(prog)
    prog_cpy[i][0] = "jmp"
    res = executeProgram(prog_cpy)
    if res[0]:
        print(res[1])
        quit()

for i in jmpInstructions:
    prog_cpy = copy.deepcopy(prog)
    prog_cpy[i][0] = "nop"
    res = executeProgram(prog_cpy)
    if res[0]:
        print(res[1])
        quit()