import csv
import numpy as np

list_links_raw = ["https://www.zillow.com/homedetails/400-Long-Creek-Rd-Sunnyvale-TX-75182/2069648819_zpid/",
                  "https://www.zillow.com/homedetails/829-E-Shady-Grove-Rd-Irving-TX-75060/162814871_zpid/",
                  "https://www.zillow.com/homedetails/3012-Willow-Dr-Flower-Mound-TX-75028/299123744_zpid/",
                  "https://www.zillow.com/homedetails/829-E-Shady-Grove-Rd-Irving-TX-75060/162814871_zpid/",
                  "https://www.zillow.com/homedetails/829-E-Shady-Grove-Rd-Irving-TX-75060/162814871_zpid/",
                  "https://www.zillow.com/homedetails/829-E-Shady-Grove-Rd-Irving-TX-75060/162814871_zpid/",
                  "https://www.zillow.com/homedetails/829-E-Shady-Grove-Rd-Irving-TX-75060/162814871_zpid/",
                  "https://www.zillow.com/homedetails/829-E-Shady-Grove-Rd-Irving-TX-75060/162814871_zpid/",
                  "https://www.zillow.com/homedetails/829-E-Shady-Grove-Rd-Irving-TX-75060/162814871_zpid/",
                  "https://www.zillow.com/homedetails/829-E-Shady-Grove-Rd-Irving-TX-75060/162814871_zpid/",
                  ]

list_prices = ["$14,700", "$13,500", "$15,000", "$21,000", "$17,300", "$11,200", "$5,000", "$28,000", "9,900", "$19,000"]

list_addresses = [
    "123 Main St., Dallas, TX, 75007",
    "456 Elm St., Austin, TX, 78704",
    "789 Westheimer Rd., Houston, TX, 73837",
    "124 Main St., Dallas, TX, 75007",
    "125 Main St., Dallas, TX, 75007",
    "126 Main St., Dallas, TX, 75007",
    "127 Main St., Dallas, TX, 75007",
    "128 Main St., Dallas, TX, 75007",
    "129 Main St., Dallas, TX, 75007",
    "130 Main St., Dallas, TX, 75007",
    ]


def remove_outliers():
    pass


# Create header names
header = ["address", "price", "link"]

# Remove comma from prices and convert to integers
list_price_clean = []
for i in range(len(list_prices)):

    # Remove comma and convert string to integer
    comma_strip = list_prices[i].replace(",", "")
    sign_strip = comma_strip.replace("$", "")
    price_int = int(sign_strip)
    list_price_clean.append(price_int)

prices_length = len(list_prices)
prices_mean = np.mean(list_price_clean)
print(f"There are {prices_length} in the list with an average price of {prices_mean}")
print(list_price_clean)

# Open a csv file for writting/create if it doesn't exist
with open('re_info.csv', 'w') as file:
    writer = csv.writer(file)

    # Write the initial header row
    writer.writerow(header)

    for i in range(len(list_links_raw)):
        row = []
        print(i)

        # Add each item to temp variable called "row"
        row.append(list_links_raw[i])
        row.append(list_price_clean[i])
        row.append(list_addresses[i])

        # Add row to csv file
        writer.writerow(row)