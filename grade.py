#!/usr/bin/env python3

import shelve
import urllib.request

chapter = "12"
exercises = ['12.1','12.2','12.3','12.4']
loadedList = []
db = shelve.open('chapter12.db', flag='c', writeback=True)
db['loaded'] = {}
if 'submitted' not in db:
    db['submitted'] = {}

try:
    import exercise121
    db['loaded']['12.1'] = True
except:
    db['loaded']['12.1'] = False
try:
    import exercise122
    db['loaded']['12.2'] = True
except:
    db['loaded']['12.2'] = False
try:
    import exercise123
    db['loaded']['12.3'] = True
except:
    db['loaded']['12.3'] = False
try:
    import exercise124
    db['loaded']['12.4'] = True
except:
    db['loaded']['12.4'] = False


db.sync()

def menu():
    while True:
        for exercise in loadedList:
            if exercise in db['submitted']:
                print('[x] Exercise ' + exercise)
            else:
                print('[ ] Exercise ' + exercise)
        print('    Enter q to exit')
        str_in = input('Exercise (e.g. 12.1): ')
        if str_in in loadedList:
            grade(str_in)
            break
        elif str_in.lower() == 'q':
            break
        else:
            print('Incorrect response. Only enter the exercise number. Example: "12.1" (no quotes).')
            
def grade(assignment):
    if assignment == '12.1':
        if exercise121.most_frequent("emma.txt")[0] == 'e' or exercise121.most_frequent("emma.txt")[0] == 'e':
            db['submitted'][assignment] = True
            submit('exercise121.py',exercise121.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise121.py',exercise121.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '12.2':
        if (['angriest', 'astringe', 'ganister', 'gantries', 'granites', 'ingrates', 'rangiest'] in exercise122.anagram_finder("words.txt") or ('angriest', 'astringe', 'ganister', 'gantries', 'granites', 'ingrates', 'rangiest') in exercise122.anagram_finder("words.txt")) and (exercise122.anagram_finder2[0] == ['angriest', 'astringe', 'ganister', 'gantries', 'granites', 'ingrates', 'rangiest'] or exercise122.anagram_finder2[0] == ('angriest', 'astringe', 'ganister', 'gantries', 'granites', 'ingrates', 'rangiest')) and exercise122.anagram_bingo == ['angriest', 'astringe', 'ganister', 'gantries', 'granites', 'ingrates', 'rangiest']:
            db['submitted'][assignment] = True
            submit('exercise122.py',exercise122.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise122.py',exercise122.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '12.3':
        if ("zaffers","zaffres") in exercise123.metathesis_pairs("words.txt"):
            db['submitted'][assignment] = True
            submit('exercise123.py',exercise123.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise123.py',exercise123.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    elif assignment == '12.4':
        if exercise124.answer == "restarting":
            db['submitted'][assignment] = True
            submit('exercise124.py',exercise124.__author__)
            str_in = input("Exercise answer correct and submitted. Would you like to submit another? (y/n): ")
            if str_in.lower() == 'y':
                menu()
        else:
            str_in = input('The exercise answer was incorrect. Did you still want to submit it? (y/n): ')
            if str_in.lower() == 'y':
                db['submitted'][assignment] = True
                submitbad('exercise124.py',exercise124.__author__)
                str_in = input("Exercise submitted. Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
            else:
                print('Assignment was not submitted')
                str_in = input("Would you like to submit another? (y/n): ")
                if str_in.lower() == 'y':
                    menu()
    else:
        print('This should not have happened. Let your instructor know.')
    db.sync()
            
def submit(file,name):
    with open(file,'rb') as fin:
        assignment = fin.read()
        url = 'https://1402-answer-repo.s3.amazonaws.com/assignments/'+name+'/'+chapter+'/'+file
        req = urllib.request.Request(url.replace(' ',''), data=assignment, method='PUT')
        urllib.request.urlopen(req)

def submitbad(file,name):
    with open(file,'rb') as fin:
        assignment = fin.read()
        url = 'https://1402-answer-repo.s3.amazonaws.com/assignments/'+name+'/'+chapter+'/incorrect/'+file
        req = urllib.request.Request(url.replace(' ',''), data=assignment, method='PUT')
        urllib.request.urlopen(req)
            
def main():
    for exercise in exercises:
        if db['loaded'][exercise]:
            loadedList.append(exercise)
    
    print('The following exercises have been loaded: ' + ', '.join(loadedList) + '. Which would you like to grade?')
    menu()


main()

db.close()