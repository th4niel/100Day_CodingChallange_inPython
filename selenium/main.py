from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.edf433e2-b6d4-408e-986d-75239a5ced10&dib=eyJ2IjoiMSJ9.uaoX7dV42SPKYOm3aRH5uO9oubke1M3AUlxnip2-qYet7VyMNlp9Q9lSNduymAx8kMuVXf-ylLVJ38QWUtsZv7b6b-uXil-7cyKh9HYuMaNXTdrKd0Avv6GhLUW69lzBh32JpweEfJSU5ABJc6srjZIMWJR1LFiiN22DRVX4_dZ8ZxGPjsyRE6lWPbKdGu5t3mIrjMmZ6qvoaYWGUpjAYZY9kds2s4oYuY_qN_dXm82hWcwbUbdFdYctt5plgOAX2PJLORys0molLaoZ9gAHNYFPXzxJw4OHLLD7dITbgik.VbuiaUvRtrzLgDlNFf8kMKuKkFfy5bZOwqfqvHfRi7w&dib_tag=se&keywords=gaming&pd_rd_r=2b7e58bd-406f-4514-958e-f5b6227ebf4e&pd_rd_w=sxUiJ&pd_rd_wg=Fyw3D&qid=1759849495&sr=8-2")
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"{price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
css_slctor = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(css_slctor.text)

xpathing = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(xpathing.text)

driver.quit()