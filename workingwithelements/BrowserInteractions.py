from selenium import webdriver
import os


# DriverLocation = /Users/mdrubel/Documents/workspace_python/lcitv1/practice/chromedriver

class BrowserInteractions():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driverLocation = "/Users/mdrubel/Documents/workspace_python/lcitv1/practice/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        titel = driver.title
        print("Titel of the page is------>: ", titel)
        CurrentUrl = driver.current_url
        print("CurrentURL is ---->", CurrentUrl)
        driver.quit()


ff = BrowserInteractions()
ff.test()
