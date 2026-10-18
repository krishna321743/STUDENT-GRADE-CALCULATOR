# STUDENT-GRADE-CALCULATOR
#A beginner-friendly Python project that calculates students' total marks, percentage, and grades based on marks in five subjects using conditional statements.
maths=int(input('ENTER YOUR MATHS MARKS: '))
physics=int(input('ENTER YOUR PHYSICS MARKS: '))
chemistry=int(input('ENTER YOUR CHEMISTRY MARKS: '))
hindi=int(input('ENTER YOUR HINDI MARKS: '))
english=int(input('ENTER YOUR ENGLISH MARKS: '))
  #add all marks
total=maths+physics+chemistry+hindi+english
  #now calculate percentage
percentage=(total/500)*100
if percentage>=90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:    
    grade = "C"
elif percentage>=60:
    grade = "D"
else:
    grade = "FAIL" 
#print the output
print('TOTAL MARKS:       ',total)
print('PERCENTAGE:        ',percentage)
print('YOU ACHIEVE GRADE: ',grade)
