# TASK 1 ==========================================================================================
with open("data/day18.txt", "r") as f:
    data = [x.strip().replace("(", "( ").replace(")"," )").split(" ") for x in f.readlines()]

def findMatchingPar(subtokens):
    """The subtoken starts with the opening parenthasis and contains the remainder
    of the math expression"""
    #print(subtokens)
    count = 0
    for i in range(len(subtokens)):
        c = subtokens[i]
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1
        
        if count == 0:
            return i

def rec_evaluate(expression):
    left = None
    op = ""
    i = 0
    while i < len(expression):
        token = expression[i]
        value = None
        if token == "(":
            i2 = findMatchingPar(expression[i:])
            value = rec_evaluate(expression[i+1:i+i2])
            i += i2 # The +1 will be added in end
        elif token.isnumeric():
            value = int(token)
        else:
            op = token

        if left == None:
            # This was the first round, operation is never the first token
            left = value
        elif not value == None: # The operation must have been set
            if op == "+":
                left = left + value
            else:
                left = left * value
            op = ""

        i += 1
    
    return left

results = [rec_evaluate(x) for x in data]
print(sum(results))

# TASK 2 ==========================================================================================
with open("data/day18.txt", "r") as f:
    data = [x.strip().replace("(", "( ").replace(")"," )").split(" ") for x in f.readlines()]
    
def createPrecedance(tokens):
    workingTokens = tokens.copy()
    i = 0
    while i < len(workingTokens): # altering array while iterating... 
        token = workingTokens[i]
        leftTokens = []
        rightTokens = []
        i_loffset = 0
        if token == "*":
            # Left
            if workingTokens[i-1] == "]":
                leftTokens = workingTokens.copy()[:i]
            else:
                count = 0
                flag = False
                left_i = 0 # 0 because array slices don't include the upper index
                for token2 in workingTokens[:i][::-1]: # Can't be bothered to think
                    if token2 == ")":
                        count += 1
                    elif token2 == "(":
                        count -= 1
                    
                    if count < 0:
                        flag = True
                    elif count == 0:
                        # We are evaluating the right scope
                        if token2 == "*":
                            flag = True
                    
                    if flag:
                        leftTokens = workingTokens[:i-left_i] + ["["] + workingTokens[i-left_i:i] + ["]"]
                        break

                    left_i += 1
                else:
                    leftTokens = ["["] + workingTokens[:i] + ["]"]
                
                i_loffset += 2
            
            # Right
            if workingTokens[i+1] == "[":
                rightTokens = workingTokens[i+1:]
            else:
                count = 0
                flag = False
                right_i = 1 # 1 because it starts 1 to the right
                for token2 in workingTokens[i+1:]:
                    if token2 == "(":
                        count += 1
                    elif token2 == ")":
                        count -= 1
                    
                    if count < 0:
                        flag = True
                    elif count == 0:
                        # We are evaluating the right scope
                        if token2 == "*":
                            flag = True
                    
                    if flag:
                        rightTokens = ["["] + workingTokens[i+1:i+right_i] + ["]"] + workingTokens[i+right_i:]
                        break
                    right_i += 1
                else:
                    rightTokens = ["["] + workingTokens[i+1:] + ["]"]
            
            workingTokens = leftTokens + ["*"] + rightTokens
            
        i += 1 + i_loffset
    
    for i in range(len(workingTokens)):
        if workingTokens[i] == "[":
            workingTokens[i] = "("
        elif workingTokens[i] == "]":
            workingTokens[i] = ")"

    return workingTokens

def findMatchingPar(subtokens):
    """The subtoken starts with the opening parenthasis and contains the remainder
    of the math expression"""
    count = 0
    for i in range(len(subtokens)):
        c = subtokens[i]
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1
        
        if count == 0:
            return i

def rec_evaluate(expression):
    left = None
    op = ""
    i = 0
    while i < len(expression):
        token = expression[i]
        value = None
        if token == "(":
            i2 = findMatchingPar(expression[i:])
            value = rec_evaluate(expression[i+1:i+i2])
            i += i2 # The +1 will be added in end
        elif token.isnumeric():
            value = int(token)
        else:
            op = token

        if left == None:
            # This was the first round, operation is never the first token
            left = value
        elif not value == None: # The operation must have been set
            if op == "+":
                left = left + value
            else:
                left = left * value
            op = ""

        i += 1
    
    return left

print(sum([rec_evaluate(createPrecedance(x)) for x in data]))