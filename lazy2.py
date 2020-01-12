from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    

#TODO 
#Fix Loops
#Add comments

class codeBOT:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def genFetch(self,amount,ida,before,after,appName):
        FirstHalf = 'fetch("https://studio.code.org/milestone/{ida}/{before}/{after}"'
        Middle = ', {"credentials":"include","headers":{"accept":"application/json, text/javascript, */*; q=0.01","accept-language":"pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7","content-type":"application/x-www-form-urlencoded","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","x-newrelic-id":"UQYGVVBQGwAHXFZRAQU=","x-requested-with":"XMLHttpRequest"},"referrer":"https://studio.code.org/s/course3/stage/21/puzzle/1","referrerPolicy":"no-referrer-when-downgrade","body":"program=%3Cxml%3E%3Cblock%20type%3D%22when_run%22%20deletable%3D%22false%22%20movable%3D%22false%22%3E%3Cnext%3E%3Cblock%20type%3D%22controls_repeat%22%20deletable%3D%22false%22%20editable%3D%22false%22%3E%3Ctitle%20name%3D%22TIMES%22%3E4%3C%2Ftitle%3E%3Cstatement%20name%3D%22DO%22%3E%3Cblock%20type%3D%22draw_move_by_constant%22%3E%3Ctitle%20name%3D%22DIR%22%3EmoveForward%3C%2Ftitle%3E%3Ctitle%20name%3D%22VALUE%22%3E20%3C%2Ftitle%3E%3Cnext%3E%3Cblock%20type%3D%22draw_turn_by_constant%22%3E%3Ctitle%20name%3D%22DIR%22%3EturnRight%3C%2Ftitle%3E%3Ctitle%20name%3D%22VALUE%22%3E90%3C%2Ftitle%3E%3C%2Fblock%3E%3C%2Fnext%3E%3C%2Fblock%3E%3C%2Fstatement%3E%3C%2Fblock%3E%3C%2Fnext%3E%3C%2Fblock%3E%3C%2Fxml%3E&'
        LastHalf = 'app={appName}&level=custom&result=true&testResult=100&time={time}&lines={lines}&save_to_gallery=false&attempt={attempts}","method":"POST","mode":"cors"'
        time = random.randint(7000,30000)
        attempts = random.randint(1,9)
        lines = random.randint(3,10)
        for i in range(0,amount):
            newBefore = before + i
            newAfter = after + i
            first = FirstHalf.format(ida=ida,before=newBefore,after=newAfter)
            sec = LastHalf.format(appName=appName,time=time,lines=lines,attempts=attempts)
            return (first + Middle + str(sec) + '});')

    def sendPog(self,key):
        capabilities = DesiredCapabilities.CHROME
        capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.driver = webdriver.Chrome(desired_capabilities=capabilities)
        self.login = self.login
        self.driver.get('https://code.org/')
        self.driver.find_element_by_xpath('//*[@id="signin_button"]')\
            .click()
        sleep(6)
        self.driver.find_element_by_xpath('//*[@id="user_login"]')\
            .send_keys(self.login)
        self.driver.find_element_by_xpath('//*[@id="user_password"]')\
            .send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="signin-button"]')\
            .click()
        self.driver.execute_script(key)
        sleep(5)

a = codeBOT('login', 'password')
b = a.genFetch(5,59462700,74166,1095,'maze')
a.sendPog(b)