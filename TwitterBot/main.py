from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 200
PROMISED_UP = 10
CHROME_DRIVER_PATH = CHROMEDRIVER_ENV
TWITTER_EMAIL = ACCOUNT_ENV
TWITTER_PASSWORD = PASSWORD_ENV
TWITTER_USERNAME = "PythHar"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.CLASS_NAME, "start-button").click()
        time.sleep(40)
        self.down = float(
            self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                               '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        print(self.down)
        self.up = float(
            self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                               '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(self.up)
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/'
                                           'div/div/div[1]/div[1]/div/div[3]/div[5]/a').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                           '/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
                                 ).send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                           '/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        time.sleep(1)
        if self.driver.find_element(By.XPATH,  '//*[@id="layers"]/div[2]/div/div/div/div/div/di'
                                               'v[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/di'
                                               'v[2]/label/div/div[2]/div/input'):
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/di'
                                               'v[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/di'
                                               'v[2]/label/div/div[2]/div/input').send_keys(TWITTER_USERNAME)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/di'
                                               'v[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/d'
                                               'iv/div/div/div').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/di'
                                               'v/div/div/div[2]/div[2]/div/div/div[2]/div[2]/d'
                                               'iv[1]/div/div/div[3]/div/label/div/div[2]/div[1'
                                               ']/input').send_keys(TWITTER_PASSWORD)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                               '/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        else:
            self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/di'
                                               'v/div/div/div[2]/div[2]/div/div/div[2]/div[2]/d'
                                               'iv[1]/div/div/div[3]/div/label/div/div[2]/div[1'
                                               ']/input').send_keys(TWITTER_PASSWORD)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                               '/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div'
                                               '/div/div/div').click()
        time.sleep(5)
        tweet_entry_field = self.driver.find_element(By.CLASS_NAME, 'public-DraftEditor-content')
        tweet_text = f"Dette er en test av mine python skills. Min download-hastighet: {self.down} mbps og upload" \
                     f"-hastighet: {self.up} er lavere enn det abonomentet mitt garanterer @altibox."
        tweet_entry_field.send_keys(tweet_text)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

