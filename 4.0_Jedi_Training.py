# 4.0 Jedi Training (40pts)  Name:Tommy Ngo
#Below each program list the mistakes found in comments.

  #1. Make the following program work. (3 mistakes)  (3pts)

midichlorians = float(input("Enter midichlorian count: ")) #missing a parathesis
if midichlorians > 10000: #There was no colon after 10000
    print("You have serious Jedi potential")
else: #This should be else rather than elif
    print("Jedi, you will never be.")


 # 2. Make the following program work. (3 mistakes)  (3pts)
     
x = int(input("Enter a number: ")) #needs an int function or else the input will be a string
if x == 3: #needs another equal sign to use the equal comparison operator, needs a colon after 3
    print("You entered 3")


  # 3. Make the following program work. (4 mistakes)  (4pts)
     
answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8": #uses the wrong variable, we need to change a to answer. We need to add another equal sign because the program is reading it as a assignment operator rather than a comparison operator.
    print("Correct!")
else: #needs a colon and it was indented improperly (it should align with the if statement above it)
    print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes) (4pts)
     
jedi = input("Name one of the top 3 greatest Jedi.") #we need to change the variable name from x to jedi
if jedi.lower()=="yoda" or jedi.lower()=="luke skywalker" or jedi.lower()=="obi-wan kenobi": #need to use jedi== with every value listed. There has to be quotes around values if they are strings like Yoda. We need to add lower() to every jedi variable so it does not take capitaliation into account.
    print("That is correct!") #needs paratheses around "That is correct!"



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.  (6pts)
     
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input.lower() == "a" or user_input.lower() == "jedi master":
    sensitivity = 1000
elif user_input.lower() == "b" or user_input.lower() == "sith lord":
    sensitivity = 900
elif user_input.lower() == "c" or user_input.lower() == "droid":
    sensitivity = 0
else:
    print("Not a choice!")
    sensitivity = ""

print("Sensitivity: ",sensitivity)




'''
6. NUMBER ANALYSIS PROGRAM  (10pts)
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''

user_num = int(input("Choose a number: "))

if (user_num%2) == 0:
    print("The number is even.")
else:
    print("The number is odd.")

if user_num > 0:
    print("The number is positive.")
elif user_num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if user_num >= -100 and user_num <= 100:
    print("The number is inclusive between -100 and 100.")
else:
    print("The number is exclusive from -100 through 100.")



'''
GRADING 2.0    (10pts)
-------------------
Copy your Grading 1.0 program below and then modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

semester_grade = int(input("Your semester grade: "))
final_exam = int(input("Your final exam grade: "))
exam_worth = int(input("How much was your final exam worth? "))
overall_grade = semester_grade*((100-exam_worth)/100)+final_exam*(exam_worth/100)
print("")
print("Your overall grade is", overall_grade)

if overall_grade >= 90:
    print("You have an A")
elif overall_grade >= 80:
    print("You have a B")
elif overall_grade >= 70:
    print("You have a C")
elif overall_grade >= 60:
    print("You have a D")
else:
    print("You failed. Real embarrassing. Transfer to Johnston!")



