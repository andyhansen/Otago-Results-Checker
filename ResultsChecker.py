from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass
from time import strftime, localtime

"""
Sends the provided message to the given facebook inbox. The
message will be sent from the account whos login details are provided.
"""
def sendFacebookMessage(username, password, inboxUrl, message):
  driver.get("https://www.facebook.com")
  elem = driver.find_element_by_name("email")
  elem.send_keys(username)
  elem = driver.find_element_by_name("pass")
  elem.send_keys(password)
  elem.send_keys(Keys.RETURN)
  driver.get(inboxUrl)
  elem = driver.find_element_by_name("message_body")
  elem.send_keys(message)
  elem.send_keys(Keys.RETURN)

username = raw_input("Enter your pims username: ")
password = getpass.getpass("Enter your pims password: ")
fbusername = raw_input("Enter your facebook email: ")
fbpassword = getpass.getpass("Enter your facebook password: ")
fbmessage = raw_input("Enter the url for your facebook inbox: ")

driver = webdriver.Firefox()
print "This is a basic program which checks your pims every two minutes."
print "If your results have been updated then it sends the changed results"
print "as a Facebook message to the Facebook inbox you choose."
print

#log into pims
driver.get("https://corpapp.otago.ac.nz/pims")
sleep(5) #wait for redirects
elem = driver.find_element_by_name("username")
elem.send_keys(username)
elem = driver.find_element_by_name("password")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

#takes you to your results page on pims then takes the text inside the
#results box and prints it to the terminal
driver.get("https://corpapp.otago.ac.nz/apex/f?p=128:91")
old_text = driver.find_elements_by_class_name("t103RegionWithoutButtonsAndTitle")[1].text
print old_text + "\n"

"""
Reloads the page and checks the results every two minutes.
If the results are up then it sends a message to the facebook
inbox specified from the account whos log in details are provided.
"""
while True:
  driver.get("https://corpapp.otago.ac.nz/apex/f?p=128:91")
  new_text = driver.find_elements_by_class_name("t103RegionWithoutButtonsAndTitle")[1].text
  # If the results have changed then send the facebook message
  if old_text != new_text:
    sendFacebookMessage(fbusername, fbpassword, fbmessage, old_text)
    break
  old_text = new_text
  print "Last checked at:", strftime("%a, %d %b %Y %H:%M", localtime())
  sleep(120)

driver.close()
