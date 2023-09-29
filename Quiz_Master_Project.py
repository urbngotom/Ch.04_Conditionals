'''
QUIZ MASTER PROJECT  (4pts)
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
answer = "" #keeps track of the input of the user
score = 0 #keep track of how many questions the user gets right
question_num = 0 #keep track of how many questions there are

print("Are You Smarter Than a Fifth Grader?")
print("A. Yes")
print("B. No")
answer = input("Type answer here (A, B): ")

if answer.lower() == "a" or answer.lower() == "yes":
    print("We'll see...")
elif answer.lower() == "b" or answer.lower() == "no":
    print(":(")
    exit()  #If user is not confident, terminate program because they aren't ready to take the quiz
else:
    print("That isn't an option. You failed.")
    exit() #if user enters a value that is not an option, terminate program because they don't know how to read

print("")
question_num += 1
print("Q1: Who invented the lightbulb?")
print("A. Benjamin Franklin")
print("B. Thomas Edison")
print("C. Marc Hermon")
print("D. Albert Einstein")

answer = input("Type answer here (A, B, C, D): ")

if answer.lower() == "b" or answer.lower() == "thomas edison" or answer.lower() == "edison" or answer.lower() == "thomas":
    print("\033[0;32m Correct!\033[0m") #escape code turns the text green and then back to normal
    score += 1
elif answer.lower() == "a" or answer.lower() == "c" or answer.lower() == "d":
    print("\033[0;31m Wrong!\033[0m") #escape code turns the text red and then back to normal
    print("The correct answer is B. Thomas Edison")
else:
    print("Not an option!")
    print("The correct answer is B. Thomas Edison")

print("")
question_num += 1
print("Q2: The Tropic of Capricorn lies in which hemisphere?")
print("A. Northern Hemisphere")
print("B. Southern Hemisphere")

answer = input("Type answer here (A, B): ")

if answer.lower() == "southern" or answer.lower() == "southern hemisphere" or answer.lower() == "b":
    print("\033[0;32m Correct!\033[0m")
    score += 1
elif answer.lower() == "a":
    print("\033[0;31m Wrong!\033[0m")
    print("The correct answer is B. Southern Hemisphere")
else:
    print("Not an option!")
    print("The correct answer is B. Southern Hemisphere")

print("")
question_num += 1
print("Q3: Between 1 and 100, how many multiples of 7 are odd numbers?")
answer = input("Type answer here: ")

if answer == "7" or answer.lower() == "seven":
    print("\033[0;32m Correct!\033[0m")
    score += 1
else:
    print("\033[0;31m Wrong!\033[0m")
    print("The correct answer is 7.")

print("")
if score == 3: #congratulate users who have gotten all questions right so far
    print("You're on a roll so far!")
    print("")

question_num += 1
print("Q4: What does the prefix \"un\" mean?")
answer = input("Type answer here: ")

if answer.lower() == "not":
    print("\033[0;32m Correct!\033[0m")
    score += 1
else:
    print("\033[0;31m Wrong!\033[0m")
    print("The correct answer is not.")

print("")
question_num += 1
print("Q5: This term is often used in art. It means light and dark. What term is it?")
print("A. chiaroscuro")
print("B. contrapposto")
print("C. sfumato")
print("D. impasto")
answer = input("Type answer here (A, B, C, D): ")

if answer.lower() == "chiaroscuro" or answer.lower() == "a":
    print("\033[0;32m Correct!\033[0m")
    score += 1
elif answer.lower() == "b" or answer.lower() == "c" or answer.lower() == "d":
    print("\033[0;31m Wrong!\033[0m")
    print("The correct answer is A. chiaroscuro")
else:
    print("Not an option!")
    print("The correct answer is A. chiaroscuro")

print("")
question_num += 1
print("Q6: How many feet are in 75 yards? (units are important)")
answer = input("Type answer here: ")

if answer.lower() == "225ft" or answer.lower() == "225feet" or answer.lower() == "225 feet" or answer.lower() == "225 ft":
    print("\033[0;32m Correct!\033[0m")
    score += 1
else:
    print("\033[0;31m Wrong!\033[0m")
    print("The correct answer is 225 feet.")

print("")
question_num += 1
print("Q7: Final question. What word is spelled incorrectly in every single dictionary?")
answer = input("Type answer here: ")

if answer.lower() == "incorrectly":
    print("\033[0;32m Correct!\033[0m")
    score += 1
else:
    print("\033[0;31m Wrong!\033[0m")
    print("the correct answer is incorrectly.")

percentage_grade = score/question_num*100
letter_grade = ""
if percentage_grade > 90:
    letter_grade = "A"
elif percentage_grade > 80:
    letter_grade = "B"
elif percentage_grade > 70:
    letter_grade = "C"
elif percentage_grade > 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("")
print("Congratulations! You finished the quiz! You got", score, "out of", str(question_num)+". Your final score is", str(percentage_grade)+".", "You earned a", letter_grade+"!")
if letter_grade == "F":
    print("You failed. Go back to elementary!")

