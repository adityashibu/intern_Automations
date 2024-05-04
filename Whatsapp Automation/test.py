from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DownloadHandler(FileSystemEventHandler):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def on_created(self, event):
        if not event.is_directory:
            # Extract sender's name from WhatsApp header
            sender_name = self.driver.find_element(By.CSS_SELECTOR, 'span[aria-label]').text

            # Create folder for sender if it doesn't exist
            sender_folder = os.path.join('downloads', sender_name)
            if not os.path.exists(sender_folder):
                os.makedirs(sender_folder)

            # Move downloaded file to sender's folder
            downloaded_file = event.src_path
            os.rename(downloaded_file, os.path.join(sender_folder, os.path.basename(downloaded_file)))

# Set up Firefox driver
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")

# Wait for user to scan QR code and login
input("Press Enter after scanning QR code...")

# Set up file system observer
event_handler = DownloadHandler(driver)
observer = Observer()
observer.schedule(event_handler, path=r"C:\Users\Aditya Uni\Downloads", recursive=False)
observer.start()

# Keep the program running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
