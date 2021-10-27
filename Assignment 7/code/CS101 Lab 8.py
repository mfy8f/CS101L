import csv
a=[]

while(True):
    try:
        x = float(input("Enter the minimum mpg here "))
        if(x < 0):
            print("Fuel economy given must be greater than 0")
        if(x > 100):
            print("Fuel economy given must be less than 100")
        else:
            break
    except:
        print("Please enter an int or float number for the fuel economy")

while(True):
    try:
        b = (input("Enter the name of input vehicle file here "))
        c = open(b,'r')
        for value in c:
            a.append(value.split())
        break
    except:
        print("Could not open file" , b)

while(True):
    try:
        z=(input("Enter the name of output vehicle file  "))
        y=open(z,'w')
        break
    except:
        print("Please try a different response",z)

for value in range(len(a)):
    try:
        f = a[value][0]
        g = a[value][1] 
        h = a[value][2]
        i = a[value][7]
        if(int(i) > x):
            y.write(f"{f}{g}{h}{i:}/n")
    except:
        print(f"Could not convert value {i} for vehicle {f} {g} {h}")
