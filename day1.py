tmp = open("../aoc20data/data1.txt", "r").readlines()
flag = False
for expense in tmp:
    for expense2 in tmp:
        sum2 = int(expense) + int(expense2)
        if sum2 == 2020:
            print("Day1: Product {}*{}={}".format(expense.strip(),expense2.strip(),int(expense)*int(expense2)))
        for expense3 in tmp:
            sum3 = int(expense) + int(expense2) + int(expense3)
            if sum3 == 2020:
                print("Day2: Product {}*{}*{}={}".format(expense.strip(),expense2.strip(),expense3.strip(),int(expense)*int(expense2)*int(expense3)))
                flag = True
                break
        if flag:
            break
    if flag:
        break
