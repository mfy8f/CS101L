lst_test = []
lst_work = []
weight_test = 0.6
homework_weight = 0.4
menu = """Grade Menu
1 - Add Test
2 - Remove Test
3 - Clear Test
4 - Add Assignment
5 - Remove Assignment
6 - Clear Assignment
D - Display Scores
Q - Quit
==>  """

choice = ['1', '2', '3', '4', '5', '6', 'd', 'q', 'D', 'Q']

def prompt(a):
    #program prompt for a choice in menu
    c = input(a)
    if c in a:
        return c

def delete_score(a):
    #deleting score 
    c = float(input('Please select the value of the test/assignment you want to remove  '))
    #search a for c
    if c not in a:
        print(c, " not found")
    else:
        a.remove(c)

def display_results(a, b):
    #display on screen and use other functions 
    c = avg(a)
    d = avg(b)
    print("{:<5} {:>5} {:>5} {:>5} {:>5} {:>5}".format("Type", "#", "min", "max", "avg", "std"))
    print("="*70)
    #call math_score to print off and do the math of the middle section of the display
    math_score(a, "Tests")
    math_score(b, "Programs")
    e = c * weight_test + d * homework_weight
    #print the final weighted score
    print("The weighted scores is {:5.2f}".format(e))

def scores(b):
    while True:
        try:
            #input for score number
            a = float(input(b))
            if a < 0:
                print('Please input a number greater than or equal to 0')
                a = float(input(b))
            if a > 100:
                print('Please input a number less than or equal to 100')
            if a >= 0 and a <= 100:
                break
        except:
            print('Please enter a valid option')
    return a

def calc(a, b):
    c = 0
    for score in a:
        c += (b - score) ** 2
    d = (c / len(a)) ** 0.5
    return d

def math_score(a, b):
    #function will run twice when called in the display function
    z = len(a)
    #option if user had no score
    if len(a) == 0:
        print("{:<5} {:>5} {:>5} {:>5} {:>5} {:>5}".format(b, '0', 'n/a', 'n/a', 'n/a', 'n/a'))
    #if user has scores, runs this section
    if len(a) > 0:
        c = avg(a)
        d = calc(a, c)
        e = min(a)
        f = max(a)
        print("{:<5} {:>5} {:>5.2f} {:>5.2f} {:>5.2f} {:>5.2f}".format(b, z, e, f, c, d))

def avg(a):
    #function to find the average
        return sum(a) / len(a)

def quit():
    #function to quit
        return False

#main, where program is actually starting
play = True
while play:
    choice = prompt(menu)
    if choice == '1':  
        score = scores('Enter the new Test score 0-100 ==>  ')
        lst_test.append(score)
        print(lst_test)
    if choice == '2':  
        delete_score(lst_test)
    if choice == '3':  
        lst_test.clear()
    if choice == '4':  
        score = scores('Enter the new Assignment score 0-100 ==>  ')
        lst_work.append(score)
        print(lst_work)
    if choice == '5':
        delete_score(lst_work)
    if choice == '6':  
        lst_work.clear()
    if choice == 'D': 
        display_results(lst_test,lst_work)
    if choice == 'Q':
        play = quit()
        
