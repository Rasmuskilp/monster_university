from monster_workshop import *
from monster_students import *
from monster_lecture_theathre import *
def clerk_functions():
    # add_workshop = input('Enter the workshop:')
    # Monster_workshop.workshop_list.append(add_workshop)
    add_workshop_id = input('What is the workshops id?')
    add_location = input('what is the location?')
    add_staff = input('who is the professor?')
    add_subject = input('What do they study?')
    add_workshop_true = Monster_workshop(add_workshop_id, add_location, add_staff, add_subject, 0)
    # add_name = input('what is the name of the student?')
    # add_student = input('Enter the student_id:')
    # add_skills = input('What is their skill?')
    # add_grade = input('What is their grade')
    # # Monster_students.add_grade(add_name,add_name,add_grade)
    # add_name = Monster_students(f'{add_name}', add_skills, add_student, add_grade)
    # Monster_workshop.add_student_workshop().append(add_student)
    workshops.append(add_workshop_true)
    # monsters.append(add_name)
from run_uni import *
while True:
    print('1 - create a monster')
    print('2 - list all workshops')
    print('3 - add students to monster list + workshop')
    print('4 - see students grade')
    print('5 - print a students full information')
    print('6 - search for a student by name')
    print('7 - add new workshop')
    print('8 - add student to workshop')
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
    elif '7' in interface:
            clerk_functions()
    elif '8' in interface:
        for woks in workshops:
            print(woks.workshop_id)
        choice = input('which workshop do you wish to add the student to, from the list of workshop id"s?')
        for workshop in workshops:
            if  choice == workshop.workshop_id:
                workshop.add_student_workshop(int(add_id))
                print(workshop.list_of_students)
        # workshop.add_student_workshop(int(add_id))
    else:
        print('Sorry but you did not enter a number, do you wish to exit, then press y')
        exits = input('press y if you want to exit')
        if 'y' in exits:
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
