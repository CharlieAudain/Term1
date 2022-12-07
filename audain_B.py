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
            elif iteration == 0 and s[i] == "a":
                pass
            elif iteration != 0 and s[i] == control[iteration-1]:
                    pass
            else:
                valid = False
    else:
        valid = False
if valid == True:
    print("True. Goodbye.")
else:
    print("False.")
