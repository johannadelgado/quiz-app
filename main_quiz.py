import requests
import csv
import html

def choose_quiz():
    '''
    The purpose of this function is to tell the player to choose a category
    and difficulty to their quiz. It requests a URL from the Open Trivia 
    Database API so that it can retreive multiple choice questions of the
    category and difficulty the player requested. 
    Parameters:
        None
    Returns:
        quizjson: a dictionary that was converted from the JSON format.
    '''
    # cat_str is short for category string
    cat_str = "\n" + "9:General Knowledge" + "\n"
    cat_str += "10:Entertainment" + "\n"
    cat_str += "17:Science and Nature" + "\n"
    cat_str += "21:Sports" + "\n"
    cat_str += "22:Geography" + "\n"
    cat_str += "23:History" + "\n"
    cat_str += "27:Animals" + "\n"
    cat_str += "28:Vehicles" + "\n"
    category = input("Choose your category (Enter the number for category):" +\
                                                                     cat_str)
    print(category)
    difficulty = input("Choose your difficulty:" + "\n" + "easy" + "\n" + \
                                            "medium" + "\n" + "hard" + "\n")
    # requests a URL from Open Trivia Database API with players inputs
    response = requests.get("https://opentdb.com/api.php?amount=12&category="\
                 + category + "&difficulty=" + difficulty + "&type=multiple")
    # converts the response from previous line from JSON format to a dictionary
    quizjson = response.json()
    return quizjson


def create_info_list(quizjson):
    '''
    The purpose of this function is to iterate through the dictionaries in the
    result section of the quizjson dictionary and organize the quiz question, 
    options, and answer into a list. It then appends that list to quizdata.
    Parameters:
        quizjson: a dictionary that was converted from the JSON format. It
        contains the quiz information requested from the open database api.
    Returns:
        quizdata: a list of lists which each sublist containing a question, 
        the questions four options, and the correct answer.
    '''
    quizdata = []
    quiz_results = quizjson['results']
    # organizes the question, options, and answers into a list
    for quiz_dict in quiz_results:
        # html.unescape converts HTML identities back to readable characters
        question = html.unescape(quiz_dict['question'])
        choice1 = html.unescape(quiz_dict['incorrect_answers'][0])
        choice2 = html.unescape(quiz_dict['incorrect_answers'][1])
        choice3 = html.unescape(quiz_dict['incorrect_answers'][2])
        choice4_answer = html.unescape(quiz_dict['correct_answer'])
        info = [question,choice1,choice2,choice3,choice4_answer]
        quizdata.append(info)
    return quizdata


def write_csv(quizdata):
    csv_header = ['#QUESTION','CHOICE1','CHOICE2','CHOICE3','CHOICE4/ANSWER']
    csv_file = open('quiz.csv','w',encoding='UTF8',newline='')
    writer = csv.writer(csv_file)
    writer.writerow(csv_header)
    writer.writerows(quizdata)
    csv_file.close()
    return 'quiz.csv'