import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json 
from win10toast import ToastNotifier
import requests

def send(text):
    url = "https://discord.com/api/webhooks/1349542649866223616/D71F_MlzyzychFHUY8QQ2Qx8n9-cYgA3W8L_9ORwjaN60SHnFlIwO-5sUL7ROzaAI8Oa"
    embed_data = {
        "title": "A train",
        "description": "Get details from Emails as fast as A train",
        "color": 0x313338,
        "fields": [
            {
                "name": "📧 Email:",
                "value": f"```{text}```<@everyone>",
            }
        ],
        "footer": {
            "text": "Wait For Next Email ..."
        }
    }

    payload = {
        "embeds": [embed_data]
    }

    response = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

    if response.status_code == 204:
        print("Embed sent successfully")
    else:
        print(f"Failed to send embed. Status code: {response.status_code}")
        print(response.text)

def sender(text):
    n = ToastNotifier()
    n.show_toast("1337", "Notification body", duration = 1, icon_path ="s.ico")
    while(True):
        time.sleep(1)
        send(text)




def loger(wait, driver, email, password):
    driver.get("https://admission.1337.ma/en/users/sign_in")
    email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id=":r4:-form-item"]/input')))
    email_field.send_keys(str(email))
    email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id=":r5:-form-item"]/input')))
    email_field.send_keys(str(password))
    next_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/form/div[3]/button')))
    next_button.click()
    time.sleep(1)
    while(driver.title == "Loading..."):
        time.sleep(1)

def checker(email, password):
    driver =  uc.Chrome()
    wait = WebDriverWait(driver, 100)
    driver.set_window_size(900, 700)
    try:
        while(True):
            driver.get("https://admission.1337.ma/candidature/check-in")
            while(driver.title == "Loading..."):
                time.sleep(1)
            if(driver.current_url == "https://admission.1337.ma/candidature/check-in"):
                time.sleep(2)
                try:
                    checking = driver.find_element(By.XPATH, '//p[@class="font-[400]"]')
                    time.sleep(5)
                    if(checking.get_attribute('innerHTML') != "Any available Check-ins will appear here"):
                        sender("checking dkhoul in3al rabk")
                    else:
                        print("[*]NO CHECKING")
                        time.sleep(5)
                        pass
                except Exception as e:
                    print("[*]NO CHECKING")
                    loger(wait, driver, email, password)
            else:
                print("[*]NO CHECKING")
                loger(wait, driver, email, password)
    except Exception as e:
        checker(email, password)

checker(input('[+] Email: '), input("[+] Password: "))
