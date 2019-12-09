from monster_class import *
class Monster_students(Monster):

    def __init__(self,name,skills,uni_id,__grade):
        super().__init__(name,skills)
        self.name = name
        self.skills = skills
        self.uni_id = uni_id
        self.__grade = 'A'
    def go_to_lecture_theatre(self,lecture_theatre):
        return 'hard at work at:' + lecture_theatre
    def add_grade(self,name,grade):
        #self.name = name
        self.__grade = grade
        return f'the {name} students new grade is : ' + grade
    def return_grade(self):
        r_grade = self.__grade
        return r_grade
