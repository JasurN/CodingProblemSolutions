def checkIsAlphaNum(s):
    for i in s:
        if i.isalnum() == True:
            print("True")
            return 0
    print("False")

def checkIsAlpha(s):
    for i in s:
        if i.isalpha() == True:
            print("True")
            return 0
    print("False")

def checkIsDigit(s):
    for i in s:
        if i.isdigit() == True:
            print("True")
            return 0
    print("False")

def checkIsLower(s):
    for i in s:
        if i.islower() == True:
            print("True")
            return 0
    print("False")

def checkIsUpper(s):
    for i in s:
        if i.isupper() == True:
            print("True")
            return 0
    print("False")

if __name__ == '__main__':
    s = input()
    checkIsAlphaNum(s)
    checkIsAlpha(s)
    checkIsDigit(s)
    checkIsLower(s)
    checkIsUpper(s)