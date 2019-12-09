class Monster:
    def __init__(self,name,skills):
        self.name = 'Bob'
        self.skills = ['juggling']
    def scare_attack(self):
        return 'grrrrr! Fear me puny human.'
    def eat(self,food):
        return 'nom nom'+' '+food
    def sleep(self):
        return 'zzzzzz'
    def skill_add(self,skill_add):
        return self.skills.append(skill_add)
    #def skill_list():
# CH = Monster('sf','fishing')
# print(CH.skills)