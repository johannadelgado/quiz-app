# 1. organize questions in a list of dictionaries
#[{Question: ,Options: ,Answer },{Question},{},{},{}]

# 2. shuffle questions in a different order each time (random module)
# 3. show one question at a time (loop maybe)
# 4. user input, user picks answer by enterina a number (input)
# 5. check answer with feedback (right or wrong)
# 6. score keeping, keep track of questions answered correctly
# 7. final result w/ score

# once you finish all of this you can change it a bit by starting the game by 
# showing the player all the different options of games and then having the 
# player enter what game they want and then starting the game with that

import csv
import random

def read_file(csv_file):
    info_list = []
    infile = open(csv_file)
    csvreader = csv.reader(infile)
    for line in csvreader:
        if line[0][0] != "#":
            q_dict = {"Question": line[0], "Options": line[1:5], "Answer": line[5]}
            info_list.append(q_dict)
    return info_list


def shuffle_questions(info_list):
    random.shuffle(info_list)
    return info_list


def send_questions(info_list):
    score = 0
    q_count = 0
    for dicts in info_list:
        print(dicts["Question"])
        options = dicts["Options"]
        print("1: "+options[0])
        print("2: "+options[1])
        print("3: "+options[2])
        print("4: "+options[3])
        user_answer = int(input("Pick Number: "))
        while user_answer > 4 or user_answer < 1:
            user_answer = int(input("Not an option, try again: "))
        if options[user_answer-1] == dicts["Answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect")
        q_count += 1
    print("Final Score: " + str(score) + "/" +  str(q_count))


def main():
    info_list = read_file("italyquiz.csv")
    new_info_list = shuffle_questions(info_list)
    send_questions(new_info_list)

main()