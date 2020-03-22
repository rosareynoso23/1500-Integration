# Rosa Reynoso
# Integration Project: Brain Challenger!
# It is a mini quiz that makes players think and helps to workout their brain. Simple but still makes you think.


#welcoming players to the quiz and explains what the game is for
print("Welcome to Brain Challenger!")
import time #source: geeksforgeeks.org : time functions in python
time.sleep(1)#source: geeksforgeeks.org : time functions in python
# time is used throughout my project
player_name = input("What is your name?")
print("Hi," + player_name + "!This game will consist of 10 questions, mainly about math, that will make you think.") #explains what the game is about
time.sleep(2)

#imports time to allow a couple of seconds before the next line appears
time.sleep(1) #allows 1 second before the next line appears
begin_game = int(input("Enter 1 when you're ready to begin.")) #user enters 1 to begin game
if  begin_game == 1: #when use is ready to play, rules are displayed next.
    print("Great! Please try your best to answer these questions mentally and without help.")
else:
    print(input("Error. Please type 1 to begin.")) #just in case they accidently input something else
time.sleep(2)


score = 0 #sets the score to zero; used to find the final score

# Question 1
question_1 = int(input("1. Divide 46 in half and add 12. What is the answer?")) #question and then asks for the answer
question1_answer = 35 #answer to Q1
#if and else statements to determine the output for wrong and right answers
if question_1 == question1_answer: #tells player when they are correct or wrong
    print("Correct!")
    score += 1 #each time the player answers a question correctly, 1 will be added to their 'score'
else:
    print("Sorry,the correct answer is 35.")
time.sleep(1)#allows a second before next line. So it doesn't all display so fast and jumbled up


# Question 2
question_2 = int(input("2. What is 64 to the .5 power?")) #question
question2_answer = 8 #answer
if question_2 == question2_answer: #tells them if they're right or wrong
    print("Correct!")
    score += 1 #player answers a question correctly: 1 added to their 'score'
else:
    print("Sorry, the correct answer is 8.")
time.sleep(1) #time in seconds


# Question 3
# Riddle
question_3 = input("3. Johnny’s mother had three children. The first child was named April. The second child was named May. What was the third child’s name?")#Q3
answer = 'johnny'
answer2= 'Johnny'
if question_3 == answer or question_3 == answer2: #tells them if they're right or wrong
    print("YES! Good job on paying attention!")
    score += 1 #player answers a question correctly: 1 added to their 'score'
else:
    print("The third child's name is actually Johnny.Tricky huh?")
time.sleep(1)


# Question 4
print("4.") # to ensure player knows what number they're on
row = 7
column = 6
start = 1
for x in range(row):
 #prints the columns and rows indicated
    for x in range(column):
        print(1, end=" ")
    start += 1
    print()
time.sleep(1)

question4_1 = int(input("4a. How many columns are there?")) #first part of question 4
question4_1answer = 6 #answer for part 1
time.sleep(1) # time before new question

question4_2 = int(input("4b. How many rows are there?"))# second part of question 4
question4_2answer = 7 #answer for part 2

#if and else statements to determine the output for wrong and right answers
if question4_1 == question4_1answer and question4_2 == question4_2answer:
    print("Correct!")
    score += 1 #player answers a question correctly: 1 added to their 'score'
else:
    print("Not quite.")
    print("There are actually 6 columns and 7 rows displayed.") # tells them the right answer
time.sleep(2) #seconds


# Question 5
# prints input multiple times
favorite_animal = input("5. Enter the name of your favorite animal: ")
x = 1 #set to 1 to begin
while x < 18: # as long as x is less than 18 it will keep looping and printing the input
    print(favorite_animal)
    x = x + 1
counting = int(input("How many times is the word repeated? Try not to count 1 by 1 and do not lean into the screen.")) #qurestion and rules
question_5answer = 17 #answer

#if and else statements to determine the output for wrong and right answers
if counting == question_5answer:
    print("Correct!")
    score += 1 #player answers a question correctly: 1 added to their 'score'
elif counting >= 15:
    print("So close! It was repeated 17 times. Don't worry if you got it wrong, it's easy to get lost.") #encouragement
else:
    print("It was repeated 17 times. Don't worry if you got it wrong, it's easy to get lost.") #answer and encouragement
time.sleep(1)

# Question 6
#True or false question
def main(): #functions definitions: help from pogil 13
    print("6. A square has a side that measures 4.")
    print("The perimeter of the square is", 4 * 4) #prints the perimeter: '16'

main() # call to main
time.sleep(1)

question_6 = input("Is this True or False? Enter T or F.")
answer = 'T'
answer_2 = 't'

#if and else statements to determine the output for wrong and right answers
if question_6 == answer or question_6 == answer_2 : #player might input t or T as the answer
    print("Correct!")
    score += 1 # player answers a question correctly: 1 added to their 'score'
else: 
    print("Incorrect. Remember that perimeter is the sum of all sides.") #if they get it wrong, they're reminded of perimeter
time.sleep(1)


# Question 7

print("7. Sarah took 6, divided it by 2 and then squared it. Then she subtracted 3. Her final number was: ")
print((6 / 2) ** 2 - 3) #calculates the math indicated
question_7 = input("Is this True or False? Enter T or F.")
answer = 'T'
answer_2 = 't'

#if and else statements to determine the output for wrong and right answers
if question_7 == answer or question_7 == answer_2 : #tells them if they're right or wrong
    print("Correct!")
    score += 1 # player answers a question correctly: 1 added to their 'score'
else:
    print("Incorrect.")






##### These are repeats of previous questions, I will change them. I just needed to have 10 to calcuate the score at the end.
##### I wanted to make sure the final score was correct

# Question 8
question_1 = int(input("8. Divide 46 in half and add 12. What is the answer?"))
question1_answer = 35
if question_1 == question1_answer:
    print("Correct!")
    score += 1
else:
    print("Sorry,the correct answer is 35.")
time.sleep(1)

# Question 9
question_2 = int(input("9. What is 64 to the .5 power?"))
question2_answer = 8
if question_2 == question2_answer:
    print("Correct!")
    score += 1
else:
    print("Sorry, the correct answer is 8.")
time.sleep(1)


# Question 10
question_1 = int(input("10. Divide 46 in half and add 12. What is the answer?"))
question1_answer = 35
if question_1 == question1_answer:
    print("Correct!")
    score += 1
else:
    print("Sorry,the correct answer is 35.")
time.sleep(1)






#To calcualte the final score for the player when they finish the quiz
#multiply the overall score by the amount of questions to find final score 
final_score = score * 10
print("Final Score is: ")
time.sleep(1)
print(".......")
# I put '%' to show player their percentage score at the end of the game
print(score * 10,("%"))

#farewell for finishing the game. Words of encouragement
#if and elif statements to determine the output for wrong and right answers
if score > 7: #Boolean expressions
    print("Awesome!! Thank you for Playing!")
elif score <= 6:
    print("Good Job! Thank you for Playing!")





    





    




      
