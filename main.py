from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

chrome_drive_path = "C:\\Development\\chromedriver_win32\\chromedriver.exe"
log_in_url = "https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F%3Ftrk%3Dnav_logo&fromSignIn=true&trk=cold_join_sign_in"
PHONE = "0123456"

driver = webdriver.Chrome(executable_path=chrome_drive_path)

driver.get(log_in_url)

# Login
email = driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys("doe622134@gmail.com")

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("4453714agh")

login_button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
login_button.click()

remember_me_button = driver.find_element_by_xpath('//*[@id="remember-me-prompt__form-primary"]/button')
remember_me_button.click()

# search for python developer
time.sleep(5)
search_bar = driver.find_element_by_xpath('//*[@id="ember17"]/input')
search_bar.send_keys('Python developer')
search_bar.send_keys(Keys.ENTER)

#apply the job
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

            time.sleep(5)
            discard_button = driver.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")[0]
            discard_button.click()
            print("Complex application, skipped")
            continue
        else:
            submit_button.click()

            time.sleep(2)
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

    except NoSuchElementException:
        print("No application button, skipped")
        continue

time.sleep(5)
driver.quit()