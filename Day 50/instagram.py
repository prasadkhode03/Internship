# instagram.py
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_post_data():
    if len(sys.argv) < 3:
        print("Usage: python instagram.py <caption> <media_paths>")
        sys.exit(1)

    caption = sys.argv[1]
    raw_media = sys.argv[2]
    media_list = [p.strip() for p in raw_media.split(";") if p.strip()]

    return caption, media_list

def post_to_instagram(caption, media_list):
    opts = Options()
    opts.add_argument(f"user-data-dir={os.path.join(os.getcwd(), 'ig_cookies')}")  # Keep login session
    driver = webdriver.Chrome(options=opts)

    try:
        driver.get("https://www.instagram.com/")
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, "nav")))
        print("[*] Logged in to Instagram.")

        # Click on New Post (+ icon)
        new_post_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//svg[@aria-label='New post']/ancestor::button"))
        )
        new_post_btn.click()

        # File input for "Select from computer"
        file_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@accept='image/jpeg,image/png,video/mp4,video/quicktime']"))
        )
        file_input.send_keys("\n".join(media_list))
        print("[*] Media uploaded.")

        # Click Next (first time)
        next_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Next']/ancestor::button"))
        )
        next_btn.click()

        # Click Next (second time for caption screen)
        next_btn2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Next']/ancestor::button"))
        )
        next_btn2.click()

        # Insert caption
        caption_area = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )
        caption_area.clear()
        caption_area.send_keys(caption)
        print("[*] Caption inserted.")

        # Click Share
        share_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Share']/ancestor::button"))
        )
        share_btn.click()
        print("[*] Post shared successfully.")

        # Optional: wait for post confirmation
        time.sleep(5)

    except Exception as e:
        print(f"[X] Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    caption, media = get_post_data()
    post_to_instagram(caption, media)
