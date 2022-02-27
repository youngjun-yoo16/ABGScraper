from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

PATH = r"C:\Users\USER\Downloads\chromedriver_win32\chromedriver.exe"

# scrape function
def scrape_data(username):
     
    driver = webdriver.Chrome(PATH)
    URL = "https://www.instagram.com"
    driver.get(URL)
    
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.clear()
    username.send_keys("test.account0916")
    password.clear()
    password.send_keys("dbdudwns")

    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    alert = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "나중에 하기")]'))).click()
    alert2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "나중에 하기")]'))).click()
    
    account_name = "thefreshmanclub_purdue"
    driver.get("https://www.instagram.com/" + account_name + "/")
    time.sleep(5)
    
    scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    match=False
    while(match==False):
        last_count = scrolldown
        time.sleep(3)
        scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        if last_count == scrolldown:
            match=True
            
    posts = []
    links = driver.find_elements_by_tag_name('a')
    for link in links:
        post = link.get_attribute('class')
        if '_7UhW9   xLCgt      MMzan   KV-D4           se6yk       T0kll ' in post:
            posts.append(post)
    print(posts)
 
    '''
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup.find("span",{"class": "eg3Fv"})
    '''
    
# main function
if __name__=="__main__":
     
    # user name
    username = "thefreshmanclub_purdue"
     
    # calling scrape function
    data = scrape_data(username)
     
    # printing the info
    print(data)