from monster_students import *
from monster_workshop import *
from monster_lecture_theathre import *
Library = Building('greenfield')
depository = lecture_theatre('greenfield',101)
scary_studies = Monster_workshop('101','room5','Dr. Evil','how to frighten 101',0)
human_studies = Monster_workshop('102','room4','Mr. Benson', 'humans 101',0)
cool_studies = Monster_workshop('103','room3','Ms. Cullins','A postmonster interpretation of cool in 21st century Britain',0)
charlie = Monster_students('Charlie','cycling',5,'B')
bob = Monster_students('Bob','swimming',6,'C')
elisabeth = Monster_students('Elisabeth','hiking',4,'A')
marco = Monster_students('Marco','fencing',3,'B')
monsters = [bob,charlie,elisabeth,marco]
workshops = [scary_studies,cool_studies,human_studies]
def clerk_functions():
    add_workshop = input('Enter the workshop:')
    #Monster_workshop.workshop_list.append(add_workshop)
    add_workshop_id = input('What is the workshops id?')
    add_location = input('what is the location?')
    add_staff = input('who is the professor?')
    add_subject = input('What do they study?')
    add_workshop = Monster_workshop(add_workshop_id, add_location, add_staff, add_subject, 0)
    add_name = input('what is the name of the student?')
    add_student = input('Enter the student_id:')
    add_skills = input('What is their skill?')
    add_grade = input('What is their grade')
   # Monster_students.add_grade(add_name,add_name,add_grade)
    add_name = Monster_students(f'{add_name}', add_skills, add_student,add_grade)
    #Monster_workshop.add_student_workshop().append(add_student)
    workshops.append(add_workshop)
    monsters.append(add_name)
#clerk_functions()
for workshop in workshops:
    for student in monsters:
        print(workshop.add_student_workshop(student.uni_id))
Monster_students.add_grade(bob,'bob','B')
print(Building.light_switch(Library))
print(lecture_theatre.light_switch(depository))
# print(scary_studies.add_student_workrshop(bob.uni_id))
# print(scary_studies.add_student_workshop(bob.uni_id))
print(charlie.uni_id)
print(workshops)
print(monsters)
#for mons in monsters:
 #   print(mons.skills)
    #for val in mons.name:
       # print (val)

# def clerk_functions(self):
#     add_workshop = input('Enter the workshop:')
#     Monster_workshop.workshop_list().append(add_workshop)
#     add_student = input('Enter the student_id:')
#     Monster_workshop.add_student_workshop().append(add_student)
#print((Monster_workshop.add_student_workshop()))
#if charlie.uni_id != 0:
 #   scary_studies.list_of_students.update(add_student_workshop(charlie.uni_id))
#print(add_student_workshop(5))
print(scary_studies.list_of_students)
#print(scary_studies.get_uni_id())

