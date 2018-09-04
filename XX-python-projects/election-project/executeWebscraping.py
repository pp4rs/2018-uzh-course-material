# Executing the webscraping script

import webscrapeFunctions

searchterms = ["Dennis Rodman","Kim Jong Un"]

url = webscrapeFunctions.build_url('2016-11-01','2016-11-08','US',searchterms)
url

print('Starting webscraping')

driver = webscrapeFunctions.open_driver()

webscrapeFunctions.download_csv(url, driver)

driver.quit()

print('Ended webscraping')

#    https://trends.google.com/trends/explore?date=2016-11-06%202016-11-09&geo=US&q=Taylor%20Swift,Kim%20Kardashian