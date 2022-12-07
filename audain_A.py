s = input("Please enter the string to be checked:")
valid = True
length = len(s)
control = "cauda"
iteration = 0
if length == 0:
    valid = False
else:
    if s[0] == "c":        
        for i in range(0, length):
            if s[i] == control[iteration]:
                iteration += 1
                if iteration == 5:
                    iteration = 0
                continue
            else:
                valid = False
    elif s[0] == "a" and length != 1 and s[1] == "u":
        iteration = 1
        for i in range(0, length):
            if s[i] == control[iteration]:
                iteration += 1
                if iteration == 5:
                    iteration = 0
                continue
            else:
                valid = False
    elif s[0] == "a" and length != 1 and s[1] == "c":
        iteration = 4
        for i in range(0, length):
            if s[i] == control[iteration]:
                iteration += 1
                if iteration == 5:
                    iteration = 0
                continue
            else:
                valid = False
    elif s[0] == "a" and length == 1:
        valid = True
    elif s[0] == "u":
        iteration = 2
        for i in range(0, length):
            if s[i] == control[iteration]:
                iteration += 1
                if iteration == 5:
                    iteration = 0
                continue
            else:
                valid = False
    elif s[0] == "d":
        iteration = 3
        for i in range(0, length):
            if s[i] == control[iteration]:
                iteration += 1
                if iteration == 5:
                    iteration = 0
                continue
            else:
                valid = False

    else:
        valid = False
if valid == True:
    print("True. Goodbye.")
else:
    print("False.")
