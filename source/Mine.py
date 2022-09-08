from Unit import *

class Mine(Unit):
    def __init__(self,master,size,x,y,color):
        super().__init__(master,size,x,y,color)
        self.type = UnitType.mine

    def create(self):
        self.unit = self.master.create_polygon(self.x,
                                               self.y,
                                               self.x + self.size,
                                               self.x + (self.size/2),
                                               self.y + self.size,
                                               self.y + (self.size/2),
                                               fill = self.color,
                                               width = 0)
                                               
