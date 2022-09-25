
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

inputEmail = driver.find_element(By.NAME, 'email')      # To find webcontrol whoes name is email
inputEmail.send_keys("test@gmail,com") ## to write text into textbox

inputPass = driver.find_element(By.NAME, 'pass')    ## # To find webcontrol whoes name is pass
inputPass.send_keys("pass@123@123") ## to write text into textbox

btnLogin = driver.find_element(By.NAME, 'login')    ## # To find webcontrol whoes name is login
btnLogin.click()        ## click on button