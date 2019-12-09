from monster_workshop import *
from monster_students import *
from monster_lecture_theathre import *
from run_uni import *
while True:
    print('1 - create a monster')
    print('2 - list all workshops')
    print('3 - add students to spooky workshop')
    print('4 - see students grade')
    print('5 - print a students full information')
    print('6 - search for a student by name')
    interface = input('Enter the number for the option you wish to choose')
    if '1' in interface:
        add_student = input('what is the name of the student?')
        add_id = input('Enter the student_id:')
        add_skill = input('What is their skill?')
        add_grades = input('What is their grade')
        # Monster_students.add_grade(add_name,add_name,add_grade)
        add_student_full = Monster_students(add_student, add_skill, add_id, add_grades)
    elif '2' in interface:
        for subjects in workshops:
            print(subjects.subject)
    elif '3' in interface:
        monsters.append(add_student_full)
    elif '4' in interface:
        print(add_grades)
    elif '5' in interface:
        print(add_student,add_id,add_skill,add_grades)
    elif '6' in interface:
        name_search = input('enter students name:')
        for nom in monsters:
            if str(name_search) in nom.name:
                print(nom.name, nom.uni_id,Monster_students.return_grade(nom))
                break
            else:
                print('error')
    else:
        print('Sorry but you did not enter a number, do you wish to exit, then press y')
        exits = input('press y if you want to exit')
        if 'y' in exits:
            break
            exit()


# ask for info
# evaluate info
#say which option you choose
#Create a monster --1
#list all workshops --2
#add student to spooky workshop --3
#see students grade --4
# print full information of student --5
#search for student by name -- 6
