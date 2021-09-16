
# Need to calculate weighted grades and generate errors if input is over 100 and below 0 and set them to 100 or 0

name = input('Who are we calculating grades for?')
labs = float(input('Enter the Labs grade?'))
if labs > 100:
    print('Warning, the grade has to be 100 or less. The lab grade has been set to 100')
    labs = 100
elif labs < 0:
    print('Warning, the grade has to be 0 or more. The lab grade has been set to 0')
    labs = 0
exams = float(input('Enter the Exams grade?'))
if exams > 100:
    print('Warning, the grade has to be 100 or less. The exam grade has been set to 100')
    exams = 100
elif exams < 0:
    print('Warning, the grade has to be 0 or more. The exam grade has been set to 0')
    exams = 0
attendance = float(input('Enter the Attendance grade?'))
if attendance > 100:
    print('Warning, the grade has to be 100 or less. The attendance grade has been set to 100')
    attendance = 100
elif attendance < 0:
    print('Warning, the grade has to be 0 or more. The attendance grade has been set to 0')
    attendance = 0

weight_labs = labs * 0.7
weight_exams = exams * 0.2
weight_attendance = attendance * 0.1
letter_grade = ()

weight_grade = weight_labs + weight_exams + weight_attendance

if weight_grade >= 90 and weight_grade <= 100:
    letter_grade = 'A'
elif weight_grade >= 80 and weight_grade < 90:
    letter_grade = 'B'
elif weight_grade >= 70 and weight_grade < 80:
    letter_grade = 'C'
elif weight_grade >= 60 and weight_grade < 70:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print('The weighted grade for {} is {} \n{} has a letter grade of {}'.format(name, weight_grade, name, letter_grade)) 
