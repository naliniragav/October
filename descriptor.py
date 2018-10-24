'''
Created on 24-Oct-2018

@author: Integra
'''
class Descriptor(object):
    def __init__(self):
        self.__age = 0
        
    def __get__(self,obj,Base):
        return self.__age
    
    def __set__(self,obj,value):
        if not isinstance(value,int):
            print "{} is not an integer".format(obj)
        else:    
            self.__age=value    

class Base(object):
    age = Descriptor()
    def __init__(self,age):
        self.age = age
        
    def __str__(self): 
        return "Age is: {}".format(self.age)  
    
ob = Base('20')
