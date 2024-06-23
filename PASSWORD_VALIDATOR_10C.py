# github to other projects "https://github.com/altitor/code-games"
class Validator:
    def __init__(self, password):
        self.password = password
        self.requirements = []
        self.errors = []
    
    #checking length
    def minLength(self, n):
        if len(self.password) < n:
            self.errors.append("Minimum length of password must be "+str(n))
            return False
        else:
            return True
    
    #at least one small letter
    def smallLetter(self):
        letters = "abcdefghijklmnopqrstuvwxyz"
        for i in self.password:
            if i in letters:
                return True
        else:
            self.errors.append("At least one lower letter present in password")
            return False
    
    #at least one capital letter
    def capitalLetter(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in self.password:
            if i in letters:
                return True
        else:
            self.errors.append("At least one upper letter present in password")
            return False
    
    #at least one number
    def numberPresent(self):
        numbers = "0123456789"
        for i in self.password:
            if i in numbers:
                return True
        else:
            self.errors.append("At least one number present in password")
            return False
    
    #at least one special character
    def specialCharacter(self):
        chars = """%\|=[]<>{}@₹&#-+()* "':;!?_/~`$^©®"""
        for i in self.password:
            if i in chars:
                return True
        else:
            self.errors.append("At least one special character present in password")
            return False
    
    #checking if mentioned condition satisfied
    def isValid(self):
        self.requirements.append(self.minLength(10))
        self.requirements.append(self.smallLetter())
        self.requirements.append(self.capitalLetter())
        self.requirements.append(self.numberPresent())
        self.requirements.append(self.specialCharacter())
        for i in self.requirements:
            if i == False:
                return False
        else:
            return True
            
instructions = """ENTER YOUR PASSWORD HERE
THIS WILL TELL YOU WHETHER VALID OR NOT
IF NOT VALID THIS WILL TELL YOU ERRORS"""

print(instructions)
print()

def test():
    print()
    password = input(">>> ")
    validator = Validator(password)
    if validator.isValid():
        print("Valid")
    else:
        print("Not valid")
        for error in validator.errors:
            print("X", error)
    print()
    
test()