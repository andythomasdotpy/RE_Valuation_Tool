import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from random import randint

RESULTS_PER_PAGE = 40

# zillow_link = "https://www.zillow.com/brooklyn-new-york-ny/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-74.05616135009767%2C%22east%22%3A-73.81926864990236%2C%22south%22%3A40.582594296993626%2C%22north%22%3A40.72741024741924%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A37607%2C%22regionType%22%3A17%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A509429%2C%22max%22%3A558336%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A2200%2C%22max%22%3A2400%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
zillow_link_ryan = "https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A31.893006598603296%2C%22east%22%3A-95.3275654771593%2C%22south%22%3A31.507433081588047%2C%22west%22%3A-95.80135087754992%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22max%22%3A20000%7D%2C%22mp%22%3A%7B%22max%22%3A93%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%5D%2C%22pagination%22%3A%7B%7D%2C%22mapZoom%22%3A11%7D"

class ScrapeBot:
    """Bot to scrape1"""
    def __init__(self):
        self.service = Service(executable_path="/Users/bradleythomas/Development/chromedriver")
        self.results_per_page = 40
        self.no_of_listings = 0
        self.cap_search_results = 40
        self.pages = self.no_of_listings / RESULTS_PER_PAGE
        self.current_pg = 1
        self.ctr = 0
        self.links = []
        self.prices = []
        self.addresses = []

    def open_google_form_with_selenium(self):
        """Fill out google form with information inserted in each list"""
        sleep(self.rand_sleep())
        self.driver = webdriver.Chrome(service=self.service)
        sleep(2)
        self.driver.get(zillow_link_ryan)
        sleep(2)
        self.no_of_listings = int(self.driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div/div[1]/div[1]/div[1]/div/span'))
        print(f"number of listings = {self.no_of_listings}")
        y = input("pausing...")

        # ******THIS WILL CAP SEARCH RESULTS AT 40********
        if self.no_of_listings > self.cap_search_results:
            self.no_of_listings = self.cap_search_results

        print(self.no_of_listings)
        sleep(self.rand_sleep())
        self.driver.maximize_window()

    def get_links_prices_addresses(self):
        "Obtains links, prices and addresses and places in its own list"
        while True:
            # list_links_raw = []
            self.links = []
            self.prices = []
            self.addresses = []
            self.ctr = 0
            sleep(2)
            list_links_raw = self.driver.find_elements(By.CSS_SELECTOR, ".list-card-info a")
            sleep(2)
            list_prices = self.driver.find_elements(By.CSS_SELECTOR, ".list-card-info .list-card-price")
            sleep(2)
            list_addresses = self.driver.find_elements(By.CSS_SELECTOR, ".list-card-info .list-card-addr")

            print(list_links_raw)
            print(list_prices)
            print(list_addresses)
            x = input()

            for i in range(len(list_links_raw)):
                self.ctr += 1
                print(self.ctr, list_links_raw[i].get_attribute('href'), list_prices[i].text, list_addresses[i].text)
                self.links.append(list_links_raw[i].get_attribute('href'))
                self.prices.append(list_prices[i].text)
                self.addresses.append(list_addresses[i].text)

            print(self.links)
            tmp_links_id_list = []
            tmp_links_id_list.append("zpid_" + self.links[-1].split("/")[-2].split("_")[0])
            tmp_links_id_list.append("zpid_" + self.links[-2].split("/")[-2].split("_")[0])

            if len(self.links) >= self.no_of_listings:
                print(f"checking if add'l page...links and no_of_listings = {len(self.links), self.no_of_listings}")
                # self.check_if_next_page()
                return
            else:
                print(f"scrolling... {len(self.links), self.no_of_listings}")
                self.scroll_selenium(tmp_links_id_list)

    def scroll_selenium(self, input_last_item_id_list):
        """Scroll webpage"""
        for tmp_id in input_last_item_id_list:
            try:
                element = self.driver.find_element(By.ID, tmp_id)
                sleep(2)
                ActionChains(self.driver).scroll(0, 0, 0, 650, origin=element).perform()
                break
            except:
                continue

    def check_if_next_page(self):
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Chevron Right").click()
        x = input("pausing after checking next page")

    def rand_sleep(self):
        """Creates random sleep floating point value"""
        integer = randint(3, 5)
        denominator = randint(2, 9)
        sleep_time_final = integer / denominator
        return sleep_time_final

    def selenium_quit(self):
        """Closes driver windows"""
        self.driver.quit()


