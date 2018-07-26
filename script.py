import time
import getpass
from selenium import webdriver


count = input("Welcome to brickposter 3000, how many bricks would you like to post: ")

mail = raw_input("Please enter your email address: ")

password = getpass.getpass("Please enter your password: ")



driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.facebook.com/wrloading/posts/317633154975723?comment_id=1587205281327915&notif_id=1524445290539844&notif_t=feed_comment_reply&ref=notif');

email = driver.find_element_by_name('email')
email.send_keys(mail)

pw = driver.find_element_by_name('pass')
pw.send_keys(password)
pw.submit()

driver.get('https://m.facebook.com/wrloading/posts/317633154975723?comment_id=1587205281327915&notif_id=1524445290539844&notif_t=feed_comment_reply&ref=notif');


comment  = driver.find_element_by_id('composerInput')

for x in range(0, count):

    comment.send_keys("brick")
    comment.submit()
    time.sleep(2)

print("just printed" + count + "bricks")
