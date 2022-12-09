from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class LinkedinJob:
    def __init__(self):
        self.my_service = Service("C:/Zoo_Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.my_service)
        self.counter = 0

    def into_linkedin(self, username, password):
        self.driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3394053816&refresh=true")
        # find and click sign in button:
        sign_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
        sign_button.click()
        sleep(4)
        # enter login - password and click enter:
        username_bar = self.driver.find_element(By.ID, "username")
        username_bar.send_keys(f"{username}")
        password_bar = self.driver.find_element(By.ID, "password")
        password_bar.send_keys(f"{password}")
        password_bar.send_keys(Keys.ENTER)
        sleep(5)

    def find_jobs(self, job_title, location):
        sleep(15)
        # search bar:
        search_bar = self.driver.find_element(By.ID, "jobs-search-box-keyword-id-ember23")
        search_bar.clear()
        search_bar.send_keys(job_title)
        sleep(2)
        # concrete:
        location_bar = self.driver.find_element(By.ID, "jobs-search-box-location-id-ember23")
        location_bar.clear()
        location_bar.send_keys(location)
        location_bar.send_keys(Keys.ENTER)
        sleep(6)
        easy_button = self.driver.find_element(By.CSS_SELECTOR, "ul li .search-reusables__filter-binary-toggle button")
        easy_button.click()
        sleep(6)

    def apply_jobs(self, phone):
        sleep(2)
        # available job names:
        try:
            all_jobs = self.driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
            sleep(5)

            # apply first job:
            for my_job in all_jobs:
                my_job.click()
                sleep(4)

                easy_button = self.driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
                easy_button.click()
                sleep(4)
                try:
                    sbt_window = self.driver.find_element(By.CSS_SELECTOR, ".jobs-easy-apply-modal__content footer button")
                    if sbt_window.text == "Submit application":
                        # fill phone number:
                        field = self.driver.find_element(By.CSS_SELECTOR, ".jobs-easy-apply-modal__content .fb-single-line-text__input")
                        field.clear()
                        field.send_keys(phone)
                        sleep(4)
                        # click submit button:
                        sbt_window.click()
                        sleep(12)
                        exit_button = self.driver.find_element(By.CSS_SELECTOR, ".artdeco-modal--layer-default button")
                        exit_button.click()
                        self.counter += 1
                    else:
                        next_window = self.driver.find_element(By.CSS_SELECTOR, ".artdeco-modal--layer-default button")
                        next_window.click()
                        sleep(5)
                        confirm_window = self.driver.find_element(By.CSS_SELECTOR, ".artdeco-modal--layer-confirmation .artdeco-modal__actionbar--confirm-dialog button")
                        confirm_window.click()
                        sleep(5)
                except NoSuchElementException:
                    print("element not found")
        except NoSuchElementException:
            print("element not found")
        sleep(3)
        self.driver.quit()
        return self.counter
