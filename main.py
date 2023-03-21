import os
def newgame():
    guess_bitch=[]
    correct_guess_bitch=0
    question_num=1
    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input('enter your option boi').upper()
        guess_bitch.append(guess)
        correct_guess_bitch+=checkanswer(questions.get(key),guess)
        question_num+=1
    displayscore(correct_guess_bitch,guess_bitch)


def checkanswer(answer,guess):
    if answer==guess:
        print("CORRECT")
        return 1
    else:
        print("INCORRECT")
        return 0



def displayscore(correct_guess_bitch,guess_bitch):
    print('RESULTS')
    for key in questions:
        print(questions.get(key),end=" ")
    print()

    print("GUESSES BITCH")
    for i in guess_bitch:
        print(i,end=" ")
    print()

    final_score=int(correct_guess_bitch/len(questions)*100)
    print("FINAL SCORE YOU MORON:",final_score,"%")


def playagain():

    choice=input("enter you choice moron:(yes/no)").upper()
    if choice=="YES":
        return True
    else:
        return False



questions={'who fucked ur mom?':'B','where did he fuck her?':"C",'how did he fuck her?':'C',
           'rate the sex':'D'}
options=[['A.jonny','B.dylan','C.mac','D.jason'],['A.bedroom','B.kitchen','C.bathroom','D.hall'],['A.tits','B.pussy','C.ass','D.oral'],[
   'A.7','B.10','C.9','D.8']]

newgame()
while playagain():
    newgame()
print("BYE ASSHOLE")


