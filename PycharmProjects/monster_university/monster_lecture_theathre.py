from monster_building import *
class lecture_theatre(Building):
    def __init__(self,location,num_theatre):
        super().__init__(location)
        self.num_theatre = num_theatre
    def light_switch(self):
        return 'you have turned the lights off!'