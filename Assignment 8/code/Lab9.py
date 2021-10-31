lst_test = []
lst_work = []
weight_test = 0.6
homework_weight = 0.4
menu = """
Grade Menu
1 - Add Test
2 - Remove Test
3 - Clear Test
4 - Add Assignment
5 - Remove Assignment
6 - Clear Assignment
D - Display Scores
Q - Quit
==>"""

choice = ['1', '2', '3', '4', '5', '6', 'D', 'Q']

def prompt(a, b):
    c = input(a).upper()
    while c not in choice:
        c = input(a).upper()
    return c

def delete_score(a, b):
    c = a(b)
    if c not in a:
        print(c, " not found")
    else:
        a.remove(c)

def display_results(a, b):
    test_avg = avg(a)
    assignment_avg = avg(b)
    print("{:<10} {:>10} {:>10} {:>10} {:>10} {:>10}".format( "Type", "#", "min", "max", "avg", "std"))
    print("="*70)
    math_score(a, "Tests")
    math_score(b, "Programs")
    weighted = test_avg * weight_test + assignment_avg * homework_weight
    print("The weighted scores is {:5.2f}".format(weighted))

def scores(b):
    while True:
        try:
            a = float(input(b))
            if a < 0:
                print('Please input a number greater than or equal to 0')
                a = float(input(b))
            if a > 100:
                print('Please input a number less than or equal to 100')
            if a > 0 and a < 100:
                break
        except:
            pass
    return a

def calc(a, b):
    squared = 0
    for score in a:
        squared += (b - score) ** 2
    c = (squared / len(a)) ** 0.5
    return c

def math_score(a, b):
    if len(a) == 0:
        print("{:<10} {:>10} {:>10} {:>10} {:>10} {:>10}".format( b, "0", "n/a", "n/a", "n/a", "n/a"))
    else:
        c = sum(a) / len(a)
        d = calc(a, c)
        e = min(a)
        f = max(a)
        print("{:<10} {:>10d} {:>10.2f} {:>10.2f} {:>10.2f} {:>10.2f}".format( prompt, len(scores), e, f, c, d))

def avg(a):
    if len(a) == 0:
        return 0
    else:
        return sum(a) / len(a)

play = True
while play:
    choice = prompt(menu, choice)
    if choice == '1':  
        score = scores('Enter the new Test score 0-100 ==> ')
        lst_test.append(score)
    if choice == '2':  
        delete_score(lst_test, 'Enter the Test score to remove 0-100 ==> ')
    if choice == '3':  
        lst_test.clear()
    if choice == '4':  
        score = scores('Enter the new Assignment score 0-100 ==> ')
        lst_work.append(score)
    if choice == '5':
        delete_score(lst_work, 'Enter the Assignment to remove 0-100 ==> ')
    if choice == '6':  
        lst_work.clear()
    if choice == 'D':  
        display_results(lst_test, lst_work)
    if choice == 'Q':
        play = False