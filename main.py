from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

promised_download = 200
promised_upload = 5
driver_path = "C:/Users/haile/Documents/Python DAY 1/chromedriver_win32/chromedriver.exe"


class SpeedBot():
    def __init__(self, driver_p):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_speeds(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(10)
        self.driver.find_element_by_css_selector(".start-text").click()
        sleep(60)
        self.down = float(
            self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up = float(
            self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

    def make_tweet(self):
        self.driver.get("https://twitter.com/")
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span').click()
        self.driver.find_element_by_css_selector(".nsm7Bb-HzV7m-LgbsSe-BPrWId").click()
        twitter_page = self.driver.window_handles[0]
        login_page = self.driver.window_handles[1]
        self.driver.switch_to.window(login_page)
        self.driver.find_elements_by_css_selector(".whsOnd zHQkBf").send_keys("EMAIL")
        self.driver.find_elements_by_css_selector(".whsOnd zHQkBf").send_keys(Keys.ENTER)
        self.driver.find_elements_by_css_selector(".whsOnd zHtrcf").send_keys("PASSWORD")
        self.driver.find_elements_by_css_selector(".whsOnd zHtrcf").send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="credentials-picker"]/div[1]/div[1]/div[3]/div[1]').click()
        sleep(10)
        self.driver.switch_to.window(twitter_page)
        self.driver.find_element_by_css_selector(".public-DraftStyleDefault-block public-DraftStyleDefault-ltr").send_keys(
            f"Hey @Xfinity, why is my internet speed {self.down} down/{self.up} up when I pay $50 for {promised_download} down/{promised_upload} up??"
        )
        self.driver.find_element_by_css_selector(".css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0").click()
        sleep(10)
        self.driver.quit()


bot = SpeedBot(driver_path)
bot.get_speeds()
if bot.down < promised_download or bot.up < promised_upload:
    bot.make_tweet()
