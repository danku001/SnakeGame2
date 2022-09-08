"""
Unit class that is used to represent a
element on a gridded tkinter canvas object

"""

from tkinter import *
from tkinter import ttk
from enum import Enum

class UnitType(Enum):
    """
       Assigning values or tasks to items
    """
    unit = 0
    food = 1
    mine = 2
       
class Unit:
       def __init__(self, master, size, x, y, color):
           """constructor or initializer"""
           self.x = x
           self.y = y
           self.master = master
           self.size = size
           self.color = color
           self.type = UnitType.unit

           self.create()


       def create(self):
            """ place a default element or square of default
                size on the master canvas at the specified location"""
            self.unit = self.master.create_rectangle(self.x,
                                                     self.y,
                                                     self.x + self.size,
                                                     self.y + self.size,
                                                     fill = self.color,
                                                     width = 0 )

       def move(self, location):
          """set new location
           moving the snake"""
          #setting the new location
          self.x = location[0]
          self.y = location[1]
          #delete unit at the old location
          self.master.delete(self.unit)
          #create new unit at new location
          self.unit = self.master.create_rectangle(
              self.x, self.y, self.x + self.size,
              self.y + self.size, fill = self.color,
              width = 0)

       def getPosition(self):
               return (self.x, self.y)


       def destroy(self):
             """function to destroy image"""
             self.master.delete(self.unit)
             
