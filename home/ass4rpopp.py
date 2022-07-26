# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 11:39:59 2022

@author: User
"""

from abc import ABC, abstractmethod

class Polygon(ABC):
 
  @abstractmethod
  def __init__(self):
    self.shape= 'polygon'
    #self.num_sides = None


  def  get_area(self):
       pass
  def get_dimensions(self):
       pass


class Triangle(Polygon):

	# overriding abstract methods here
	def __init__(self):
	    print("I have 3 sides")
	    Polygon.__init__(self)
	    self.num_sides = 3
     
     
	
	def get_dimensions(self):
		base = int(input("Enter Base of Triangle"))
	    height = int(input("Enter Height of Triangle"))
	    self.b= base
		self.ht= height

	def get_area(self):
		ar= 0.5 * self.b * self.ht
		print("Area of Triangle = ",ar)
	

	 
from abc import ABC, abstractmethod
class Rectangle(Polygon):

	# overriding abstract methods here 
	def __init__(self):
	    print("I have 4 sides")
	    Polygon().__init__(self)
	    self.num_sides = 4
	   	 																																																			
	 
	def get_dimensions(self):
		l = int(input("Enter Length of Rectangle"))
	    b = int(input("Enter Breadth of Rectangle"))
	    self.length = l 
		self.breadth = b


	def get_area(self):
		ar= self.length * self.breadth
		print("Area of Recctangle = ",ar)
	




# Driver code
t = Triangle()
t.get_dimensions()
t.get_area()


window = Rectangle()
window.get_dimensions()
window.get_area()

