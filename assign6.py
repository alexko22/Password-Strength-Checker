# Task 1: Input the Password
user = str(input("Enter your password: "))

# Task 2: Evaluate the Password
# Placeholder boolean
valid = True
# Check if the length is correct
if (len(user) < 8):
    valid = False
# Other Checks In a Loop...
# Initializing some booleans to be altered
upperC = False
lowerC = False
digitC = False
specialC = False
if (valid == True):
    for i in range(len(user)):
        if (user[i].isupper()):
            upperC = True
        elif (user[i].islower()):
            lowerC = True
        elif (user[i].isdigit()):
            digitC = True
        elif (user[i] == "@"):
            specialC = True
        elif (user[i] == "#"):
            specialC = True
        elif (user[i] == "$"):
            specialC = True
        # We can expand this for other special characters if needed...
        else:
            continue
# Check the results:
if (valid == True and upperC == True and lowerC == True and digitC == True and specialC == True):
    print("Your password is strong!")
else:
    print("Your password doesn't meet some requirements!")

# Bonus Challenge (5 Criteria Two Points Each)
count = 0
if (valid == True):
    count += 2
if (upperC == True):
    count += 2
if (lowerC == True):
    count += 2
if (digitC == True):
    count += 2
if (specialC == True):
    count += 2
print("This password has a score of:", count)













