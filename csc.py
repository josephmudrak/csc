from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get(
    "https://checkout.stripe.com/c/pay/cs_live_a1AVrAnvX5XJ4j07bRSkMMUkciH5udNbVWgPzB8IpD1fkPntpKtCCzxXev#fidkdWxOYHwnPyd1blppbHNgWkBLPTNJV1ZSc39paVYxakBhPF99REI0ajU1bXF9RGhvYmQnKSdjd2poVmB3c2B3Jz9xd3BgKSdpZHxqcHFRfHVgJz8ndmxrYmlgWmxxYGgnKSdga2RnaWBVaWRmYG1qaWFgd3YnP3F3cGB4JSUl"
)

file = open("./cards.txt", "r")

card_number = driver.find_element(By.XPATH, "//input[@id='cardNumber']")
card_expiry = driver.find_element(By.XPATH, "//input[@id='cardExpiry']")
card_cvc = driver.find_element(By.XPATH, "//input[@id='cardCvc']")
billing_name = driver.find_element(By.XPATH, "//input[@id='billingName']")
button = driver.find_element(By.XPATH, "//button[@type='submit']")

for line in file.readlines():
    global cc
    cc = line.split("|")

    for i in range(4):
        cc[i - 1] = cc[i - 1].replace("\n", "")  # Remove line breaks

    number = cc[0]
    expiry = cc[1] + cc[2][len(cc[2]) - 2 :]  # Convert MM, YYYY to MMYY
    cvc = cc[3]
