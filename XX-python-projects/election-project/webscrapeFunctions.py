# This file contains all the functions for the webscraping of the data

def open_driver():
    """
    Function to open the chrome webdriver.
    """
    # ---
    # add your code here
    
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    
    chrome_options = Options()
    #chrome_options.add_argument("--headless") # doesn't work yet
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
    
    # ---
    print('Chrome driver is good to go!')
    return driver



def build_url(start, end, region, searchterms):
    """
    Function to construct the URL.
    """
    
    if isinstance(searchterms, list) == True:
        searchterms = ','.join(map(str, searchterms)) # the easier  ",".join(list) might not work with some symbols.
    searchterms = searchterms.replace(' ','%20')
    
    url = 'https://trends.google.com/trends/explore?hl=en&date='+start+'%20'+end+'&geo='+region+'&q='+searchterms
    
    return url

def download_csv(url, driver):
    """
    Function to download the csv file of the map.
    """
    # ---
    # add your code here
    
    import os
    import time
    print('... start download...')
    
    map_dl = '/Users/ubergmann/Downloads/geoMap.csv'
    if os.path.exists(map_dl):
        os.remove(map_dl)

    export_map = []
    while len(export_map) == 0:
        print('... ... try loading the page...')
        driver.get(url)
        time.sleep(2)
        export_map = driver.find_elements_by_xpath('//*[@class="fe-multi-heat-map-generated fe-atoms-generic-container"]')
    
    export_map[0].find_element_by_xpath('.//*[@title="CSV"]').click()
    
    while not os.path.exists(map_dl):
        time.sleep(1)
        
    del export_map # maybe not needed with the download_csv function. 
    
    print('... download complete.')
    
    # ---
    return