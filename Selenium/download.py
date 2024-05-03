from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import os
import pickle
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from bs4 import BeautifulSoup

class DownloadHandler(FileSystemEventHandler):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            if file_path.endswith('.part'):
                # Ignore .part files
                return

            # Extract sender's name from WhatsApp header
            sender_name = self.extract_sender_name()
            if sender_name:
                # Create folder for sender if it doesn't exist
                sender_folder = os.path.join('C:\\Users\\Aditya Uni\\OneDrive - Heriot-Watt University\\Desktop\\WhatsApp Files', sender_name)
                if not os.path.exists(sender_folder):
                    os.makedirs(sender_folder)

                # Move downloaded file to sender's folder
                os.rename(file_path, os.path.join(sender_folder, os.path.basename(file_path)))

                # Extract title from WhatsApp Web
                title = self.extract_title()
                print("Title:", title)

    def extract_sender_name(self):
        try:
            # Find the element containing sender information
            sender_element = self.driver.find_element(By.CSS_SELECTOR, 'div._amig span')
            if sender_element:
                sender_name = sender_element.text
                return sender_name
        except Exception as e:
            print("Error extracting sender name:", e)
        return None

    def extract_title(self):
        try:
            # Find the element containing the title
            title_element = self.driver.find_element(By.CSS_SELECTOR, 'title')
            if title_element:
                title = title_element.get_attribute('textContent')
                return title
        except Exception as e:
            print("Error extracting title:", e)
        return None

# Set up Firefox profile to specify download directory
profile = webdriver.FirefoxProfile()
download_dir = r"C:\Users\Aditya Uni\Downloads"  # Change this to your desired download directory
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", download_dir)
profile.set_preference("browser.download.useDownloadDir", True)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

# Check if cookies file exists, load cookies if it does
cookies_file = "cookies.pkl"
if os.path.exists(cookies_file):
    with open(cookies_file, "rb") as f:
        cookies = pickle.load(f)
        profile.set_preference("network.cookie.cookieBehavior", 0)
        for cookie in cookies:
            profile.add_cookie(cookie)

# Set up Firefox driver with the specified profile
options = Options()
options.profile = profile
driver = webdriver.Firefox(options=options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for user to scan QR code and login
if not os.path.exists(cookies_file):
    input("Press Enter after scanning QR code...")

    # Save cookies for future sessions
    with open(cookies_file, "wb") as f:
        pickle.dump(driver.get_cookies(), f)

# Set up file system observer
event_handler = DownloadHandler(driver)
observer = Observer()
observer.schedule(event_handler, path=download_dir, recursive=False)
observer.start()

# Keep the program running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
