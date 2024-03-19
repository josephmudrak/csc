import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha

load_dotenv()

driver = webdriver.Firefox()
driver.get(
    "https://checkout.stripe.com/c/pay/cs_live_b19TZt9OIzuarR5xhTnmSO3l38qy52el4XhYK0FaoyUazo0FDHUODZxmE3#fidkdWxOYHwnPyd1blppbHNgWjA0SldJUndGb1QyPXRpRHJTc05cV1M8cmhtdzBmb2JNUGpQPGtCbTJtTjxWTWZHdmddXHV%2FTjdmRHNkUDNtMWs3d0EyZ1dCXzVEa3RcM1BxbmRHaDFASFB1NTVBaWNNNGRdaCcpJ2hsYXYnP34nYnBsYSc%2FJ2c8PTQ8MjRmKGA3MmEoMWQwZyhkPT01KGczMGdkMzY2N2c1NTw3YzcxZicpJ2hwbGEnPydkZGYzNTFjPCgzMj08KDFhNmYoPGBmNChjNTAyMDY0Y2Y2YzM0NDw3NzcnKSd2bGEnPydgNDIxZDM0PChgZzY3KDFkZzAoZDQyZyg8NmE8Y2E9NTU8YWQxPTdjMGQneCknZ2BxZHYnP15YKSdpZHxqcHFRfHVgJz8naHBpcWxabHFgaCcpJ3dgY2B3d2B3SndsYmxrJz8nbXFxdXY%2FKip3ZGFsZGtxZm1gZHF2K2tgcSd4JSUl"
)

file = open("./cards.txt", "r")

solver = TwoCaptcha(os.environ.get("TWOCAPTCHA_API_KEY"))

start = True

for line in file.readlines():
    global cc

    cc = line.split("|")

    for i in range(4):
        cc[i - 1] = cc[i - 1].replace("\n", "")  # Remove line breaks

    number = cc[0]
    expiry = cc[1] + cc[2][len(cc[2]) - 2 :]  # Convert MM, YYYY to MMYY
    cvc = cc[3]

    if start:
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys(
            number
        )
        driver.find_element(By.XPATH, "//input[@id='cardExpiry']").send_keys(
            expiry
        )
        driver.find_element(By.XPATH, "//input[@id='cardCvc']").send_keys(cvc)
        driver.find_element(By.XPATH, "//input[@id='billingName']").send_keys(
            "Elliot Rodger"
        )
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        start = False
