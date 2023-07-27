import random

#A good password consists of: upper case, lowercase, symbols

Uppercase = input("Would you like the password to include Uppercase letters? Y/N\n")
Symbols = input("Would you like the password to include Symbols? Y/N\n")
Numbers = input("Would you like the password to include Numbers? Y/N\n")
Size = int(input("How many characters do you want the password to contain?\n"))

# for loop to create the password
# random to find a random number from a certain range
# the ranges correspond to whether the above options were selected
# string the password and return the password

Lcase = "abcdefghijklmnopqrstuvxyz"
sym = "£$&()*+[]@#^-_!?"
Ucase = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
nums = "123456789"
Password = ""
# If every option was ticked

for i in range(Size):
    if Uppercase == "Y" and Symbols == "Y" and Numbers == "Y":
        #vals = Ucase + sym + nums + Lcase
        var = random.randrange(1,5)
        if var == 1:
            Password += random.choice(Lcase)
        if var == 2:
            Password += random.choice(nums)
        if var == 3:
            Password += random.choice(sym)
        if var == 4:
            Password += random.choice(Ucase)
    elif Uppercase == "Y" and Symbols == "Y" and Numbers == "N":
        #vals = Ucase + sym + Lcase
        var = random.randrange(1,4)
        if var == 1:
            Password += random.choice(Lcase)
        if var == 2:
            Password += random.choice(sym)
        if var == 3:
            Password += random.choice(Ucase)
    elif Uppercase == "Y" and Symbols == "N" and Numbers == "N":
        #vals = Ucase + Lcase
        var = random.randrange(1,3)
        if var == 1:
            Password += random.choice(Lcase)
        if var == 2:
            Password += random.choice(Ucase)
    elif Uppercase == "Y" and Symbols == "N" and Numbers == "Y":
        #vals = Ucase + nums + Lcase
        var = random.randrange(1,4)
        if var == 1:
            Password += random.choice(Lcase)
        if var == 2:
            Password += random.choice(Ucase)
        if var == 3:
            Password += random.choices(nums)
    elif Uppercase == "N" and Symbols == "Y" and Numbers == "N":
        #vals = sym + Lcase
        var = random.randrange(1,3)
        if var == 1:
            Password += random.choice(Lcase)
        if var == 2:
            Password += random.choice(sym)
    elif Uppercase == "N" and Symbols == "N" and Numbers == "Y":
        #vals = nums + Lcase
        var = random.randrange(1,3)
        if var == 1:
            Password += random.choice(Lcase)
        if var == 2:
            Password += random.choice(nums)
    else:
        Password += random.choice(Lcase)

print(Password)
