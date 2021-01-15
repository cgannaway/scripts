from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


site = "https://distrokid.com/spotlight/quollectorsedition/vote/"

def main():
    init()
    vote()
    driver.quit()
    print('Webdriver Stopped')

def init():
    global driver
    options = Options()
    options.add_argument("--headless")
    driver = Chrome(chrome_options=options)
    driver.implicitly_wait(20)

def vote():
    driver.get(site)
    i = 0
    while True:
        try:
            i+=1
            button = driver.find_element_by_xpath('//*[@id="distroListContainer"]/div[3]/div[3]/div[1]/div[1]/div[2]/div[2]/a[1]')
            button.click()
            print(f'Vote Successful. Iteration {i}. Press Ctrl-C to stop')
            driver.refresh()
        except KeyboardInterrupt:
            print("Ctrl+C Pressed, loop stopped.")
            break


if __name__ == "__main__":
    main()