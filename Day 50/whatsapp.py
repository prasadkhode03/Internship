import os
import time
import pyautogui
import cv2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# ---------------- CONFIG ----------------
ATTACH_ICON_PATH = "attach_icon.png"  # Path to your + icon screenshot
DEBUG_SCREEN_PATH = "debug_screen.png"
AUTO_CROP_PATH = "attach_plus_icon.png"
WAIT_TIME = 15  # Selenium element wait time
RETRY_ICON_ATTEMPTS = 5
# ----------------------------------------

def debug_print(msg):
    print(f"[*] {msg}")

def try_find(driver, selectors, timeout=WAIT_TIME, condition=EC.presence_of_element_located):
    """Try multiple XPaths until one matches."""
    for sel in selectors:
        try:
            return WebDriverWait(driver, timeout).until(condition((By.XPATH, sel)))
        except:
            continue
    raise RuntimeError(f"Element not found for selectors: {selectors}")

def auto_crop_plus_icon(screenshot_path, save_path):
    """Auto-crop + icon from screenshot."""
    img = cv2.imread(screenshot_path)
    if img is None:
        debug_print("Screenshot not found for cropping.")
        return False

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if 15 < w < 60 and 15 < h < 60:  # Likely the + icon
            cropped = img[y:y+h, x:x+w]
            cv2.imwrite(save_path, cropped)
            debug_print(f"Auto-cropped possible attach icon and saved to {save_path}")
            return True
    debug_print("No suitable contour found for + icon.")
    return False

def click_attach_icon_visual():
    """Click the attach icon via PyAutoGUI, retry if needed."""
    debug_print("Searching for attach (+) icon on screen...")
    location = None
    for attempt in range(RETRY_ICON_ATTEMPTS):
        location = pyautogui.locateCenterOnScreen(ATTACH_ICON_PATH, confidence=0.8)
        if location:
            break
        time.sleep(1)

    if not location:
        pyautogui.screenshot(DEBUG_SCREEN_PATH)
        debug_print(f"Attach icon not found. Debug screenshot saved at: {DEBUG_SCREEN_PATH}")
        if auto_crop_plus_icon(DEBUG_SCREEN_PATH, AUTO_CROP_PATH):
            for attempt in range(RETRY_ICON_ATTEMPTS):
                location = pyautogui.locateCenterOnScreen(AUTO_CROP_PATH, confidence=0.8)
                if location:
                    break
                time.sleep(1)

    if location:
        pyautogui.click(location)
        debug_print("Clicked attach icon via PyAutoGUI.")
    else:
        raise RuntimeError("Attach icon not found on screen after retries.")

def send_whatsapp_media(contact_name, caption, media_list):
    # --- Selenium setup ---
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.get("https://web.whatsapp.com")
    debug_print("Opening WhatsApp Web — waiting for login...")

    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='pane-side']"))
    )
    debug_print("WhatsApp loaded.")

    # --- Search contact ---
    search_box = try_find(driver, ["//div[@contenteditable='true'][@data-tab='3']"], condition=EC.element_to_be_clickable)
    search_box.clear()
    search_box.send_keys(contact_name)
    time.sleep(2)
    contact = try_find(driver, [f"//span[@title='{contact_name}']"], condition=EC.element_to_be_clickable)
    contact.click()
    debug_print(f"Opened chat with '{contact_name}'.")

    if media_list:
        click_attach_icon_visual()

        # Wait for file input to appear
        file_input = try_find(driver, ["//input[@type='file']"], timeout=10)
        abs_files = [os.path.abspath(p) for p in media_list if os.path.exists(p)]
        if not abs_files:
            raise RuntimeError("No valid media files found.")
        file_input.send_keys("\n".join(abs_files))
        debug_print(f"Uploaded files: {abs_files}")

        # Wait for media preview overlay (multiple possible selectors)
        try_find(driver, [
            "//div[contains(@class,'x1n2onr6')]",
            "//div[@role='dialog']//div[contains(@class,'x1hx0egp')]"
        ], timeout=15)

        # Focus caption box using JS (avoid click interception)
        caption_box = try_find(driver, ["//div[@contenteditable='true'][@data-tab='10']"], timeout=10)
        driver.execute_script("arguments[0].focus();", caption_box)
        caption_box.send_keys(caption)

        # Click send button (retry if blocked)
        for _ in range(3):
            try:
                send_btn = try_find(driver, ["//span[@data-icon='send']/ancestor::button"], timeout=10, condition=EC.element_to_be_clickable)
                send_btn.click()
                debug_print("Media message sent.")
                break
            except:
                time.sleep(1)
    else:
        # Just send a text message
        caption_box = try_find(driver, ["//div[@contenteditable='true'][@data-tab='10']"], timeout=10)
        caption_box.send_keys(caption + Keys.ENTER)
        debug_print("Text message sent.")

if __name__ == "__main__":
    send_whatsapp_media(
        contact_name="Aditya Wagh",
        caption="Hello! This is a test with media 📷",
        media_list=[r"C:\Users\prasa\OneDrive\Pictures\Screenshots\Screenshot 2025-06-13 125755.png"]
    )
