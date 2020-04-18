"""
Integration Project: Brain Challenger!
"""
__author__ = "Rosa Reynoso"


import time


def main():
    print("Welcome to Brain Challenger!")
    time.sleep(1)
    player_name = input("What is your name?")
    print("Hi," + player_name + "!This game will consist of 10 random "
                                "questions that will make you think.")
    time.sleep(2)

    time.sleep(1)
    begin_game = input("Enter 1 when you're ready to begin.")
    if begin_game == '1':
        print("Great! Please try your best to answer these questions "
              "mentally and without help.")
    elif begin_game != '1':
        print(input("Error. Please type 1 to begin."))
    time.sleep(2)

    score = 0

    # Question 1
    question_1 = input("1. How many sides does a pentagon have? Enter a "
                       "number. ")
    question1_answer = '5'
    if question_1 == question1_answer:
        print("Correct!")
        score += 1
    else:
        print("Sorry, a pentagon has 5 sides.")
    time.sleep(1)

    # Question 2
    question_2 = input("2. Divide 46 in half and add 12. What is the "
                       "answer? Enter a number.")
    question2_answer = '35'

    if question_2 == question2_answer:
        print("Correct!")
        score += 1
    else:
        print("Sorry,the correct answer is 35.")
    time.sleep(1)

    # Question 3
    question_3 = input("3. Johnny’s mother had three children. The "
                       "first child was named April. The second child was "
                       "named May. What was the third child’s name? Enter "
                       "one name.")
    q3_answer1 = 'johnny'
    q3_answer2 = 'Johnny'
    if question_3 == q3_answer1 or question_3 == q3_answer2:
        print("YES! Good job on paying attention!")
        score += 1
    else:
        print("The third child's name is actually Johnny.Tricky huh?")
    time.sleep(1)

    # Question 4
    print("4.")
    row = 7
    column = 6
    start = 1
    for x in range(row):
        for i in range(column):
            print(1, end=" ")
        start += 1
        print()
    time.sleep(1)

    question4a = input("4a. How many columns are there? Enter a number.")
    # first part of question 4
    question4a_answer = '6'
    time.sleep(1)

    question4b = input("4b. How many rows are there? Enter a number.")
    # second part of question 4
    question4b_answer = '7'

    if question4a == question4a_answer and question4b == question4b_answer:
        print("Correct!")
        score += 1
    else:
        print("Not quite.")
        print("There are actually 6 columns and 7 rows displayed.")
    time.sleep(2)

    # Question 5
    print("5. A square has a side that measures 4.")
    print("The perimeter of the square is", 4 * 4)
    time.sleep(2)

    question_5 = input("Is this True or False? Enter T or F.")
    q5_answer1 = 'T'
    q5_answer2 = 't'

    if question_5 == q5_answer1 or question_5 == q5_answer2:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Remember that perimeter is the sum of all sides.")
    time.sleep(1)

    # Question 6
    favorite_animal = input("6. Enter the name of your favorite animal: ")
    x = 1
    while x < 18:
        print(favorite_animal)
        x = x + 1
    question_6 = input("How many times is the word repeated? Enter a "
                       "number. Do not lean into the screen.")
    question6_answer = '17'

    if question_6 == question6_answer:
        print("Correct!")
        score += 1
    else:
        print("It was repeated 17 times. Don't worry if you got it wrong, "
              "it's easy to get lost.")
    time.sleep(1)

    # Question 7
    print("7. How many members are in the boyband BTS?")
    question_7 = int(input("Please enter a number, no letters."))
    question7_answer = 7
    if question_7 == question7_answer:
        print("YESSS!")
        score += 1
    else:
        print("There are 7 members in BTS.")
    time.sleep(1)

    # Question 8
    print("8. Sarah took 6, divided it by 2 and then squared it. Then she "
          "subtracted 3. Her final number was: ")
    print((6 / 2) ** 2 - 3)
    question_8 = input("Is this True or False? Enter T or F.")
    q8_answer1 = 'T'
    q8_answer2 = 't'

    if question_8 == q8_answer1 or question_8 == q8_answer2:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
    time.sleep(1)

    # Question 9
    question_9 = input(
        "9. A clerk at a butcher shop stands five feet ten inches tall and "
        "wears size 13 sneakers. What does he weigh?")
    q9_answer1 = 'meat'
    q9_answer2 = 'Meat'
    if question_9 == q9_answer1 or question_9 == q9_answer2:
        print("YES! Good job!")
        score += 1
    else:
        print("He weighs meat. Nice try!")
    time.sleep(1)

    # Question 10
    question_10 = input("10. What is 64 to the .5 power? Enter a number.")
    question10_answer = '8'
    if question_10 == question10_answer:
        print("Correct!")
        score += 1
    elif question_10 != question10_answer:
        print("Sorry, the correct answer is 8.")
    time.sleep(1)

    # Final Score
    print("That was the last question.")
    time.sleep(1)

    final_score = score * 10
    print("Your scored a: ")
    time.sleep(1)
    print(".......")
    time.sleep(1)
    print(final_score, "%")

    time.sleep(1)

    if score >= 8:
        print("Awesome score!! Thank you for Playing!")
    elif 7 >= score > 5:
        print("Good Job! Thank you for Playing!")
    else:
        print("Better luck next time!")
        print("Thank you for Playing!")


main()
