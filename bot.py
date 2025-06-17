from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("PORTAL_USER")
PASSWORD = os.getenv("PORTAL_PASS")

from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def send_whatsapp_message(body):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))
    message = client.messages.create(
        body=body,
        from_=os.getenv("WHATSAPP_FROM"),
        to=os.getenv("WHATSAPP_TO")
    )
    print("Message SID:", message.sid)

driver = webdriver.Chrome()

driver.get("https://webprosindia.com/vignanit/")


driver.find_element(By.ID, "txtId2").send_keys(USERNAME)
driver.find_element(By.ID, "txtPwd2").send_keys(PASSWORD)
driver.find_element(By.ID, "imgBtn2").click()

time.sleep(1)

driver.get("https://webprosindia.com/vignanit/Academics/StudentAttendance.aspx?scrid=3&showtype=SA")

time.sleep(1)

driver.find_element(By.ID, "radTillNow").click()
driver.find_element(By.ID, "btnShow").click()

time.sleep(1)

attendance_elements = driver.find_elements(By.CLASS_NAME, "cellBorder")


for elem in attendance_elements:
    print(elem.text)

driver.save_screenshot("attendance.png")

attendance_data = "\n".join([elem.text for elem in attendance_elements])
send_whatsapp_message(f"📊 Your Attendance Report:\n\n{attendance_data}")



driver.quit()
