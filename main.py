from zillow_scrape import ScrapeBot
from forms_input import AutofillForm

# Scrape info and insert in its own list
scrape_zillow = ScrapeBot()
try:
    scrape_zillow.open_google_form_with_selenium()
    scrape_zillow.get_links_prices_addresses()
    scrape_zillow.selenium_quit()
except KeyboardInterrupt:
    scrape_zillow.selenium_quit()
except:
    scrape_zillow.selenium_quit()

# Insert info in each list into google form with selenium
selenium_object = AutofillForm()
try:
    selenium_object.open_google_form_with_selenium()
    selenium_object.fill_out_form(scrape_zillow.links, scrape_zillow.prices, scrape_zillow.addresses)
except KeyboardInterrupt:
    selenium_object.selenium_quit()