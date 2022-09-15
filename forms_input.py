import os
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from random import randint

google_forms_link = "https://docs.google.com/forms/d/e/1FAIpQLScKXmbVY5FNRJxSK045GKDPpyDlXLpwtbUy1m0BUhD68_tepw/viewform?vc=0&c=0&w=1&flr=0"
orig_google_forms_link = "https://docs.google.com/forms/d/e/1FAIpQLScuyW8aJFwFWqI-tJptsoueIWezftuTvfTt5UG6gGNIWjYv0Q/viewform?usp=sf_link"
XPATH_ADDRESS = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
XPATH_PRICE = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
XPATH_LINK = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
XPATH_SUBMIT = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
XPATH_NEXT = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'


@dataclass
class AutofillForm:
    """Class designed to fill out form"""
    service = Service(executable_path="/Users/bradleythomas/Development/chromedriver")
    driver = webdriver.Chrome(service=service)

    def open_google_form_with_selenium(self):
        """Fill out google form with information inserted in each list"""
        self.driver.get(orig_google_forms_link)

        sleep(self.rand_sleep())
        self.driver.maximize_window()

    def fill_out_form(self, links_list, prices_list, addresses_list):
        """For loop, will autofill Google form"""

        for i in range(len(links_list)):

            # Find input #1 (address) and insert text
            sleep(self.rand_sleep())
            tmp_address = self.driver.find_element(By.XPATH, XPATH_ADDRESS )
            # self.bot_typing(addresses_list[i], tmp_address)
            tmp_address.send_keys(addresses_list[i])

            # Find input #2 (price) and insert text
            sleep(self.rand_sleep())
            tmp_price = self.driver.find_element(By.XPATH, XPATH_PRICE )
            self.bot_typing(prices_list[i], tmp_price)

            # Find input #3 (link) and insert text
            sleep(self.rand_sleep())
            tmp_link = self.driver.find_element(By.XPATH, XPATH_LINK)
            tmp_link.send_keys(links_list[i])

            # Click submit on each form
            sleep(self.rand_sleep())
            submit_button = self.driver.find_element(By.XPATH, XPATH_SUBMIT)
            submit_button.click()

            print(i)

            self.check_end_of_list(i, links_list)

    def check_end_of_list(self, iterator, input_list):
        """Check if end of list? If yes, quit and return to main.py.
            If no, click next to continue iterating through the list."""
        if iterator >= len(input_list) - 1:
            print(f"iterator i = {iterator}")
            self.selenium_quit()
            return
        else:
            sleep(self.rand_sleep())
            # Click next to fill out next form
            self.driver.find_element(By.XPATH, XPATH_NEXT).click()

    def rand_sleep(self):
        """Creates random sleep floating point value"""
        integer = randint(3, 5)
        denominator = randint(2, 9)
        sleep_time_final = integer / denominator
        return sleep_time_final

    def sleep_time_func(self):
        """Generate random float for sleep time"""
        random_sleep_time = randint(1, 3)
        denominator = randint(1, 9)
        sleep_time_final = random_sleep_time / denominator
        print(f"Sleeping for {sleep_time_final}")
        return sleep_time_final

    def bot_typing(self, input_string, input_var):
        """Type letters with randomly generated float sleep in between typing to replicate human cadence"""
        for letter in input_string:
            # sleep(self.sleep_time_func())
            input_var.send_keys(letter)

    def selenium_quit(self):
        """Closes driver windows"""
        self.driver.quit()