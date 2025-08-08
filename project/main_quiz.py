import requests
import csv
#import html

#def get_trivia(amount,category,difficulty):

def choose_quiz():
    cat_str = "\n" + "9:General Knowledge" + "\n"
    cat_str += "10:Entertainment" + "\n"
    cat_str += "17:Science and Nature"
    cat_str += "21:Sports" + "\n"
    cat_str += "22:Geography" + "\n"
    cat_str += "23:History" + "\n"
    cat_str += "24:Politics" + "\n"
    cat_str += "25:Art" + "\n"
    cat_str += "27:Animals" + "\n"
    cat_str += "28:Vehicles" + "\n"
    category = input("Choose your category (Enter the number for category):" + cat_str)
    difficulty = input("Choose your difficulty:" + "\n" + "easy" + "\n" + "medium" + "\n" + "hard" + "\n")
    response = requests.get("https://opentdb.com/api.php?amount=12&category=" + category + "&difficulty=" + difficulty + "&type=multiple")
    quizjson = response.json()
    return quizjson
#response = requests.get("https://opentdb.com/api.php?amount=18&type=multiple")


#do option1,option2,option3,option4/answer

def create_info_list(quizjson):
    quizdata = []
    for quiz_dict in quizjson['results']:
        info = [quiz_dict['question'],quiz_dict['incorrect_answers'][0],quiz_dict['incorrect_answers'][1],quiz_dict['incorrect_answers'][2],quiz_dict['correct_answer']]
        quizdata.append(info)
    return quizdata


def write_csv(quizdata):
    csv_header = ['#QUESTION','CHOICE1','CHOICE2','CHOICE3','CHOICE4/ANSWER']
    csv_file = open('quiz.csv','w',encoding='UTF8',newline='')
    writer = csv.writer(csv_file)
    writer.writerow(csv_header)
    writer.writerows(quizdata)
    csv_file.close()
    print("done")
    return 'quiz.csv'



#def get_trivia(amount,category,difficulty):
    
