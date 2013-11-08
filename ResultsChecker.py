from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass

username = raw_input("Enter your uni username: ")
password = getpass.getpass("Enter your uni password: ")
fbusername = raw_input("Enter your facebook email: ")
fbpassword = getpass.getpass("Enter your facebook password: ")
fbmessage = raw_input("Enter the url of your facebook inbox: ")

driver = webdriver.Firefox()
#load the pims page
driver.get("https://corpapp.otago.ac.nz/pims")
sleep(5) #wait for redirects
elem = driver.find_element_by_name("username")
elem.send_keys(username)
elem = driver.find_element_by_name("password")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

driver.get("https://corpapp.otago.ac.nz/apex/f?p=128:91")
old_text = driver.find_elements_by_class_name("t103RegionWithoutButtonsAndTitle")[1].text
#keep checking the results page until Unconfirmed comes up
changed = False
while not changed:
  driver.get("https://corpapp.otago.ac.nz/apex/f?p=128:91")
  new_text = driver.find_elements_by_class_name("t103RegionWithoutButtonsAndTitle")[1].text
  if old_text != new_text:
    changed = True
  old_text = new_text
  sleep(10)

print "The results are up"
#The code that seems a message to you on facebook
driver.get("https://www.facebook.com")
elem = driver.find_element_by_name("email")
elem.send_keys(fbusername)
elem = driver.find_element_by_name("pass")
elem.send_keys(fbpassword)
elem.send_keys(Keys.RETURN)
#change this to your facebook inbox
driver.get(fbmessage)
elem = driver.find_element_by_name("message_body")
elem.send_keys(old_text)
elem.send_keys(Keys.RETURN)

driver.close()
