class Monster_workshop():

    def __init__(self, workshop_id,location,staff,subject,list_of_students = 0):
        self.location = location
        self.staff = staff
        self.subject = subject
        self.workshop_id = workshop_id
        self.list_of_students = []
       # self.workshop_list = []
   # workshop_list = []
    #workshop_list = workshop_list.append(workshop_id)
    def workshop_list(self,workshop_id):
         list_workshop = []
         return list(list_workshop.append(workshop_id))

    def get_location(self,location):
        return 'workshop takes place at:' +' '+ location

    def add_student_workshop(self, uni_id):
        #workshop_id =
        num = 1
        #student_number = [num]
        # student_number = scary_studies.list_of_students.append
        # student_number = student_number.append((num+1))
        # uni_id = charlie.uni_id
        #for num in student_number:
        # if scary_studies.get_uni_id(charlie.uni_id) == 0:
        #student_workshop_list = []

        # check uni_id in self.list_students
        if uni_id not in self.list_of_students:
            self.list_of_students.append(uni_id)
            return 'student added:'+ str(uni_id)
        else :
            return 'student exists'

        # student_workshop_dict = {}
        # student_workshop_dict = student_workshop_dict.update({num: uni_id})
        # return student_workshop_dict
   # def add_student_grade(self,grade):
     #   return self.
    #
    # def clerk_functions(self):
    #     add_workshop = input('Enter the workshop:')
    #     Monster_workshop.workshop_list.append(add_workshop)
    #     add_workshop_id = input('What is the workshops id?')
    #     add_location = input('what is the location?')
    #     add_staff = input('who is the professor?')
    #     add_subject = input('What do they study?')
    #     add_workshop = Monster_workshop(add_workshop_id, add_location, add_staff, add_subject, 0)
    #     add_name = input('what is the name of the student?')
    #     add_student = input('Enter the student_id:')
    #     add_skills = input('What is their skill?')
    #     add_grade = input('What is their grade')
    #     add_name = Monster_student(f'{add_name}',add_skills,add_student,add_grade)
    #     Monster_workshop.add_student_workshop().append(add_student)
    #
    #     return
