########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


import string


def character_value(z):
    Value_1 = ord(z)
    if (Value_1 >= 48 and Value_1<=57):
        return Value_1 -48
    if (Value_1 >= 65 and Value_1<=90):
        return Value_1 -65

def get_check_digit(idnumber : str) -> int:
    d = 0
    for i in range(len(idnumber)):
        num1 = character_value(idnumber[i])
        d += num1 * (i+1)
    return d % 10

def verify_check_digit(idnumber : str) -> tuple:
    if len(idnumber) != 10:
        return (False,"The length of the number given must be 10")
    for i in range(5):
        if idnumber[i] < 'A' or idnumber[i] > 'Z':
            a = "The first 5 characters must be A-Z, the invalid character is at index "+ str(i) +" is " + idnumber[i]
            return (False, a)
    for i in range(7,10):
        if idnumber[i] < '0' or idnumber[i] > '9':
            a = "The last 3 characters must be 0-9, the invalid character is at index "+ str(i) +" is " + idnumber[i]
            return (False, a)
    if (idnumber[5] != '1' and idnumber[5] != '2' and idnumber[5] != '3'):
            return (False, "The sixth character must be 1,2 or 3")
    if (idnumber[6] != '1' and idnumber[6] != '2' and idnumber[6] != '3' and idnumber[6] != '4'):
            return (False, "The seventh character must be 1,2,3 or 4")
    calc_value = get_check_digit(idnumber)
    b = int(idnumber[9])
    
    if b != calc_value:
        c = "Check digit " + str(b) + " does not match calculated value " \
               + str(calc_value)
        return (False,c)
        
    return (True,"Library card is valid.")

def get_school(idnumber : str) -> str:
        if idnumber[5] == '1':
            return "School of Computing and Engineering SCE"
        if idnumber[5] == '2':
            return "School of Law"
        if idnumber[5] == '3':
            return "College of Arts and Sciences"
        else:
            return "Invalid School"


def get_grade(idnumber : str) -> str:
    if idnumber[6] == '1':
        return "Freshman"
    if idnumber[6] == '2':
        return "Sophomore"
    if idnumber[6] == '3':
        return "Junior"    
    if idnumber[6] == '4':
        return "Senior"
    else:
        return "Invalid Grade"
   

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
        