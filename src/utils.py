from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import numpy as np

import undetected_chromedriver as uc
from selenium import webdriver

#options = webdriver.ChromeOptions()
#options.add_argument("start-maximized")
#driver = uc.Chrome(options=options)
#driver.get('https://bet365.com')

def get_driver(use_proxy=False):

    chrome_options = Options()
    chrome_options = webdriver.ChromeOptions()

    if use_proxy:
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        driver.get("https://sslproxies.org/")
        driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//th[contains(., 'IP Address')]"))))
        ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 1]")))]
        ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 2]")))]
        proxies = []
        for i in range(0, len(ips)):
            proxies.append(ips[i]+':'+ports[i])
        chrome_options = webdriver.ChromeOptions()
        i = int(np.random.randint(low=0, high=5, size=(1,)))
        chrome_options.add_argument('--proxy-server={}'.format(proxies[i]))
        chrome_options.add_argument("start-maximized")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

    #chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_options.add_argument("start-maximized")
    #chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source":
        "const newProto = navigator.__proto__;"
        "delete newProto.webdriver;"
        "navigator.__proto__ = newProto;"
    })
    #driver = uc.Chrome(options=chrome_options)

    return driver