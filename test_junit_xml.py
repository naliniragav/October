'''
Created on 31-Oct-2018

@author: Integra
'''
import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from xmlrunner import XMLTestRunner

class OpenGoogle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Ie("C:\\drivers\\IEDriverServer.exe")
        cls.driver.get("https://google.com")
        
    def test_googleSearch(self):
        #Am acessing the local varible elm1 into another test method by declaring it as global
        global elm1
        elm1 = self.driver.find_element_by_xpath("//input[@name='q']")  

class OpenGoogleToEnterText(unittest.TestCase):    
    def test_googleSearch2(self):     
        elm1.click()
        elm1.send_keys("integra micro systems")
        

if __name__ == "__main__":
    #Am using unittest.main to run the test, usually used to run from command line
    #unittest.main(verbosity=2)
    
    
    #Alternate way to run the test, not required to run from the command line
    loader1 = unittest.TestLoader().loadTestsFromTestCase(OpenGoogle)
    loader2 = unittest.TestLoader().loadTestsFromTestCase(OpenGoogleToEnterText)
    suite = unittest.TestSuite([loader1,loader2])
    #unittest.TextTestRunner(verbosity=2).run(suite)
    
    outfile = file('google.xml','w')
    #outfile = open('google.html','w')
    '''runner = HTMLTestRunner(stream=outfile,
                            verbosity=2,
                            title="Google page test",
                            description="Google seach text entry page")
    runner.run(suite)'''
    
    runner = XMLTestRunner(output = outfile,failfast=False, buffer=False)
    
    runner.run(suite)
    
    
    
    
    


