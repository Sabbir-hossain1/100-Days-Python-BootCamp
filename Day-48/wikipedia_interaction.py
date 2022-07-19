from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element("css selector", "#articlecount a")
# # article_count.click()
#
# donate_button = driver.find_element("link text", "Donate")
# # donate_button.click()
#
# search = driver.find_element("name", "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element("name", "fName")
first_name.send_keys("Sabbir")
last_name = driver.find_element("name", "lName")
last_name.send_keys("Hossain")
email = driver.find_element("name", "email")
email.send_keys("sabbir.cse.duet@gmail.com")
sign_up = driver.find_element("xpath", "/html/body/form/button")
sign_up.click()

# driver.quit()
