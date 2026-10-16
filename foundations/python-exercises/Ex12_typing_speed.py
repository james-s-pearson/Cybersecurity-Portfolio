#############################################################################################################
#                                 Exercise Prompt
######################################################################################################
#
## Goal: help the user type faster. Show a word and have them type it five times,
## timing each round in seconds. At the end, report how many incorrect submissions were made and
## draw a chart of the typing time across the five rounds.
#
#######################################################################################################
################################# First Attempt #######################################################
#
# import time as t
#
# import matplotlib.pyplot as plt
#
# print("This is a program to help the user type faster. It measure typing speed across five attempts and reports on time, mistakes, and change over time.")
#
# time = []
# errors = 0
#
# while len(time) < 5:
#     start = t.time()
#     word = input("Type the word: ")
#     end = t.time()
#     typing_time = end - start
#
#     time.append(typing_time)
#
#     if (word.lower() != "programming"):
#         errors += 1
#
# print("You made " + str(errors) + " errors")
#
# x = [1,2,3,4,5]
# y = time
#
# plt.plot(x,y)
# plt.ylabel("Time")
# plt.xlabel("Attempts")
# plt.title("Typing Speed Chart")
# plt.show()
#
######################################################################################################
#                                 My Corrected Code
#################################                   ##################################################
#  Problem with initial code:
#    - The player was never told which word to type.
#    - "programming" and 5 were written in more than one place, so changing one meant remembering the others.
#    - Case and spaces affected what counted as a mistake without being decided.
#    - The chart's x-values were hard-coded, and the y-axis had no unit.
#    - The list of durations was named time, which looked like the module.
#    - A blank submission counted as a round, with a near-zero time that distorted the chart.
#  What I've learned in this exercise rework:
#    - Variables for repeated values: task_word and rounds each live in one place and feed the message, the check and the chart.
#    - range(start, stop): it excludes stop, so the last number of range(1, rounds + 1) is rounds.
#    - list() versus brackets: brackets list items you type yourself, list() builds a list from something else.
#    - Reading an error: "locations (3), labels (5)" named both numbers that disagreed. The cause was a hard-coded list that didn't follow rounds.
#    - Test by changing the variable: setting rounds = 3 exposed a bug that rounds = 5 hid.
#    - Remove what isn't needed: plt.xticks(x) replaced xticks(x, legend), so the whole legend list could go.
#    - time.perf_counter() for elapsed time: it's designed for timing and isn't affected by clock changes, unlike time.time().
#    - Where the timer starts matters: start sits inside the validation loop, so a rejected blank restarts the clock, and only the real attempt is timed.
#    - Clean input once: .lower().strip() on the input() line means the later comparison needs no extra cleaning.

import time as t

import matplotlib.pyplot as plt

durations = []
errors = 0
task_word = "programming"
rounds = 5

print("This is a program to help the user type faster.")
print(
    f"It measures typing speed across {rounds} rounds and reports on time, rounds containing mistakes, and change over time."
)
input("Press 'Enter' to begin the typing speed test: ")

while len(durations) < rounds:
    while True:
        start = t.perf_counter()
        user_word = input(f"Type the word {task_word}: ").lower().strip()
        if user_word == "":
            print("Invalid Input. Blank submissions not accepted.")
        else:
            break
    end = t.perf_counter()
    typing_time = end - start
    durations.append(typing_time)
    if user_word != task_word:
        errors += 1

print(f"Number of rounds containing an error: {errors}")

x = list(range(1, rounds + 1))
y = durations

plt.plot(x, y)
plt.xticks(x)
plt.ylabel("Time in seconds")
plt.xlabel("Attempts")
plt.title("Typing Speed Chart")
plt.show()
