from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
#load the pims page
driver.get("https://corpapp.otago.ac.nz/pims")
sleep(5) #wait for redirects
elem = driver.find_element_by_name("username")
elem.send_keys("hanan445")
elem = driver.find_element_by_name("password")
elem.send_keys("poo")
elem.send_keys(Keys.RETURN)

#keep checking the results page until Unconfirmed comes up
changed = False
while not changed:
  sleep(120)
  print "Checking"
  driver.get("https://corpapp.otago.ac.nz/apex/f?p=128:91")
  #When unconfirmed has changed exit the loop
  if "Unconfirmed" in driver.page_source:
    changed = True

driver.get("https://www.facebook.com")
elem = driver.find_element_by_name("email")
elem.send_keys("ahansen.it@gmail.com")
elem = driver.find_element_by_name("pass")
elem.send_keys("megapoo")
elem.send_keys(Keys.RETURN)
#change this to your facebook inbox
driver.get("https://www.facebook.com/messages/andy.s.hansen")
elem = driver.find_element_by_name("message_body")
elem.send_keys("Results are up")
elem.send_keys(Keys.RETURN)

driver.close()
