'''
    File: quiz.py
    Author: Johanna Delgado
    Date: August 7, 2025
    Description: A quiz game that allows the player to select which category and 
    difficulty they would like to play. The game tells the player each time 
    they select an answer if they got it right or wrong. At the end, it tells 
    the player their final score.
'''

import csv
import random
from main_quiz import *

def read_file(csv_file):
    '''
    The purpose of this function is to read a csv file and organize the 
    quiz information on each line into a dictionary. It then appends each
    dictionary into a list.
    Parameters:
        csv_file: a string that represents a csv file containing information
        about the game question, options and answer.
    Returns:
        info_list: a list of dictionaries, with each dictionary organizing the
        game question, options, and final answer.
    '''
    info_list = []
    infile = open(csv_file, encoding = "utf-8")
    csvreader = csv.reader(infile)
    # checks each line in the csv file and organizes data into a dictionary
    for line in csvreader:
        if line[0][0] != "#":
            q_dict = {"Question": line[0], "Options": line[1:], "Answer":\
                                                                 line[4]}
            info_list.append(q_dict)
    infile.close()
    return info_list


def shuffle_questions(info_list):
    '''
    The purpose of this function is to randomly shuffle info_list.
    Parameters:
        info_list: a list of dictionaries containing a question, options for
        answers, and the final answer.
    Returns:
        info_list: a shuffled list of dictionaries.
    '''
    random.shuffle(info_list)
    return info_list


def send_questions(info_list):
    '''
    The purpose of this function is to display the options for each question
    to the player and allow the player to choose an answer. It tells the 
    player if they were correct or incorrect. It displays the final score at the 
    end.
    Parameters:
        info_list: a list of dictionaries containing a question, options for
        answers, and the final answer.
    Returns:
        None
    '''
    score = 0
    q_count = 0
    # prints question and options each time and allows player to select answer
    for dicts in info_list:
        print(dicts["Question"])
        options = dicts["Options"]
        # shuffles options each time
        random.shuffle(options)
        print("1: "+options[0])
        print("2: "+options[1])
        print("3: "+options[2])
        print("4: "+options[3])
        user_answer = int(input("Pick Number: "))
        # if player does not answer an option, lets them try again
        while user_answer > 4 or user_answer < 1:
            user_answer = int(input("Not an option, try again: "))
        # checks if player chose right answer
        if options[user_answer-1] == dicts["Answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect")
        q_count += 1
    print("Final Score: " + str(score) + "/" +  str(q_count))


def main():
    quizjson = choose_quiz()
    quizdata = create_info_list(quizjson)
    csv_file = write_csv(quizdata)
    info_list = read_file(csv_file)
    new_info_list = shuffle_questions(info_list)
    send_questions(new_info_list)

main()
