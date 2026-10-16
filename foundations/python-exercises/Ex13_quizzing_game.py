##############################################################################################################
#                                 Exercise Prompt
######################################################################################################
#
## Goal: a trivia game. Each round, request a new question from the Open Trivia API,
## show it to the player, and say whether their answer was correct. After every round,
## ask whether to play again, keep a running score, and stop only when the player types
## "quit".
#
#######################################################################################################
################################# First Attempt #######################################################
#
# import html
# import json
# import random
#
# import requests
#
# r = requests.get("https://opentdb.com/api.php?amount=49&category=31&difficulty=easy")
# quiz = json.loads(r.text)  # create a dictionary
# rc = 0  # variable for response_code
# incorrect = 0
# score = 0
#
# print("This is a quizzing game program. As long as you want to play, the game will continue.")
# input("Press 'Enter' to continue.")
#
# while True:
#     print('****************************************************************************')
#     print('                                  START')
#     print('****************************************************************************')
#     print(html.unescape(quiz['results'][rc]['question']))
#     answerPool = quiz['results'][rc]['incorrect_answers']
#     correctAnswer = quiz['results'][rc]['correct_answer']
#     answerPool.append(correctAnswer)
#     random.shuffle(answerPool)
#     print(html.unescape(str(answerPool)))
#     guess = input("Please type the correct answer, followed by 'Enter': ")
#
#     while True:
#         if guess.lower() == correctAnswer.lower():
#             score += 1
#             rc += 1
#             break
#         else:
#             incorrect += 1
#             guess = (input("Try again: ")).lower()
#
#     print('****************************************************************************')
#     print("\nYou are correct!\n") #\nThe answer is: " + str(quiz['results'][rc]['correct_answer']))
#     print('****************************************************************************')
#     playAgain = input("Would you like to keep playing? \n Press 'Enter' to contine or type 'Quit' to end:")
#     if playAgain == ('quit'):
#         br#eak
# print('****************************************************************************')
# print('****************************************************************************')
# print("\nThanks for playing!", "\nYour final score was: " + str(score) + " correct out of " + str(score + incorrect) + ' attempts.\n')
# print('****************************************************************************')
# print('********************************** END *************************************')
#
######################################################################################################
#                                 My Corrected Code
#################################                   ##################################################
#  Problem with initial code:
#    - It fetched 49 questions in one request instead of one per round, and crashes after 49 rounds.
#    - Nothing checked whether the request or the response had worked, so an empty or failed reply crashed the program.
#    - The correct answer was compared before its HTML codes were converted
#    - The player had to type the answer text, so a quote mark or an accent in an answer could never match.
#    - The quit check was case-sensitive, so the "Quit" the prompt asked for never worked.
#    - The player kept guessing until right, so the program could never report a wrong answer.
#    - There was no timeout on the request.
#  What I've learned in this exercise rework:
#    - HTTP in practice: requests.get with a timeout, r.status_code and r.json().
#           + r.json() and json.loads(r.text) do the same job, and r.json() is shorter when you have a response.
#    - Four levels of failure: the network, the status code, the API's response_code, and invalid JSON.
#           + A reply can have status 200 and still contain no question.
#    - Nested data: quiz["results"][0] goes down one level per [...].
#           + Naming the inner dictionary shortens everything after it.
#    - html.unescape on text before comparing or displaying it, and on each item of a list, not on the list.
#    - .append() and random.shuffle() change the list in place and return None, so never assign their result.
#    - Functions that return None on failure, and a caller that checks is None.
#    - A return placed too early makes the code after it unreachable.
#    - Two functions with separate jobs:
#           + request_question makes one attempt and reports
#           + fetch_question loops and asks retry or quit in one place.
#    - Rate limits: a countdown between requests prevents the 429.
#    - Choices to record: one guess per round, numbered answers, and a failure that offers retry or quit.

import html
import random
import time as t

import requests

score = 0
wrong = 0


def request_question(url):
    try:
        r = requests.get(url, timeout=5.0)
    except requests.exceptions.RequestException:
        print("GET Failed")
        return None
    if r.status_code != 200:
        print(f"GET Failed. Status Code: {r.status_code}")
        return None
    try:
        data = r.json()
    except ValueError:
        print("GET Failed. JSON not received.")
        return None
    if data["response_code"] != 0:
        print(f"API call unsuccessful. Response Code: {data['response_code']}")
        return None
    return data


def fetch_question(url):
    while True:
        result = request_question(url)
        if result is not None:
            return result
        again = input("Press 'Enter' to retry or type 'Quit': ").strip().lower()
        if again == "quit":
            return None


while True:
    quiz = fetch_question("https://opentdb.com/api.php?amount=1&category=31")
    if quiz is None:
        break
    desired_result = quiz["results"][0]
    clean_question = html.unescape(desired_result["question"])

    clean_answer_pool = []
    clean_correct_answer = html.unescape(desired_result["correct_answer"])
    clean_answer_pool.append(clean_correct_answer)
    for answer in desired_result["incorrect_answers"]:
        clean_answer_pool.append(html.unescape(answer))
    random.shuffle(clean_answer_pool)
    print("*************************************************************************")
    print("*************************************************************************")
    print(clean_question)
    for number, clean_answer in enumerate(clean_answer_pool, start=1):
        print(f"{number}: {clean_answer}")
    print("*************************************************************************")

    while True:
        try:
            guess = int(input("Please input the number corresponding to your answer: "))
        except ValueError:
            print("Invalid Input. Please input a valid answer using only numbers.")
            print(
                "*************************************************************************"
            )
            continue
        if guess <= 0 or guess > len(clean_answer_pool):
            print(
                "Invalid Entry. Please input a valid answer using only available numbers."
            )
            print(
                "*************************************************************************"
            )
        else:
            guess_answer = clean_answer_pool[guess - 1]
            if guess_answer == clean_correct_answer:
                score += 1
                print(f"You guessed it! The correct answer was {clean_correct_answer}.")
                print("***************************************************************")
            else:
                wrong += 1
                print(
                    f"I'm sorry, but that is the wrong answer. The correct answer is: {clean_correct_answer}"
                )
                print(
                    "****************************************************************************************"
                )
            break

    play_again = input("Type 'Quit' to end the game. \n: ").lower().strip()
    if play_again == "quit":
        break

    for seconds in range(5, 0, -1):
        print(f"Next question in: {seconds}")
        t.sleep(1)

print(f"Thank you for playing! Your score is: {score}/{score + wrong}")
