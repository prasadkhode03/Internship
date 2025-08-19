import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_post_data():
    """Return (caption, media_list, options). media_paths expected as semicolon-separated string."""
    if len(sys.argv) < 5:
        print("Usage: python linkedin.py <title> <text> <hashtags> <media_paths> <linkedin_option1> ...")
        sys.exit(1)

    title = sys.argv[1]
    text = sys.argv[2]
    hashtags = sys.argv[3]
    raw_media = sys.argv[4] or ""
    options = sys.argv[5:]  # e.g., ["Video Only"]

    caption = f"{title}\n\n{text}\n\n{hashtags}".strip()
    media_list = [p.strip() for p in raw_media.split(";") if p.strip()]

    return caption, media_list, options


def _find_file_input(driver, timeout=5):
    """Try to find an <input type='file'> on the page. Return element or None."""
    try:
        return WebDriverWait(driver, timeout).until(lambda d: d.find_element(By.XPATH, "//input[@type='file']"))
    except Exception:
        return None


def post_to_linkedin(caption, media_list, option):
    option = option.strip().lower()
    opts = Options()
    # use the cookies/ profile folder in current working directory
    opts.add_argument(f"user-data-dir={os.path.join(os.getcwd(), 'cookies')}")
    driver = webdriver.Chrome(options=opts)

    try:
        driver.get("https://www.linkedin.com/feed/")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "global-nav")))
        print(f"[*] Logged in - preparing post for: {option}")

        # Open "Start a post"
        start_post_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//strong[text()='Start a post']]"))
        )
        start_post_btn.click()

        # --- ONLY ARTICLE (no media) ---
        if option == "only article":
            post_area = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
            )
            post_area.click()
            post_area.send_keys(caption)
            print("[*] Caption inserted for article.")
            post_btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Post']]"))
            )
            post_btn.click()

        # --- MEDIA POSTS (upload first, then insert caption in final dialog) ---
        elif option in ("video only", "image posts"):
            allowed_exts = ('.mp4', '.mov', '.avi', '.mkv') if option == "video only" else ('.jpg', '.jpeg', '.png', '.mp4', '.mov', '.avi', '.mkv')
            valid_media = []
            for p in media_list:
                if os.path.exists(p) and p.lower().endswith(allowed_exts):
                    valid_media.append(os.path.abspath(p))
                    if len(valid_media) >= 20:
                        break
                else:
                    print(f"[!] Skipping invalid or missing file: {p}")

            if not valid_media:
                print("[!] No valid media found for this option. Aborting post.")
                driver.quit()
                return

            # Try to find a file input on the page (preferred — sending keys directly avoids system dialog)
            file_input = _find_file_input(driver, timeout=3)
            if not file_input:
                # try to reveal the input by clicking the "Add" button (use JS click)
                try:
                    add_btn = driver.find_element(By.XPATH, "//button[contains(@aria-label,'Add') or contains(@aria-label,'Add media') or contains(@aria-label,'Add a photo') or contains(@aria-label,'Add a video')]")
                    driver.execute_script("arguments[0].click();", add_btn)
                except Exception:
                    pass
                # after clicking, wait for input
                file_input = _find_file_input(driver, timeout=10)

            if not file_input:
                print("[!] Could not find file input element. The site may require interactive file dialog. Aborting.")
                driver.quit()
                return

            # upload files (send_paths as newline-separated string)
            file_input.send_keys("\n".join(valid_media))
            print(f"[*] Uploaded files: {valid_media}")

            # wait until Next becomes clickable (upload may take a few seconds)
            next_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Next')]"))
            )
            next_button.click()

            # After clicking Next, insert caption into final textbox (use the last textbox on page)
            final_textbox = WebDriverWait(driver, 30).until(
                lambda d: d.find_element(By.XPATH, "(//div[@role='textbox'])[last()]")
            )
            final_textbox.click()
            final_textbox.clear()
            final_textbox.send_keys(caption)
            print("[*] Caption inserted after media upload.")

            # Click Post
            post_btn = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Post']]"))
            )
            post_btn.click()

        else:
            print(f"[!] Unknown option: {option}")
            driver.quit()
            return

        # wait for a short confirmation (toast)
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'artdeco-toast-item__message') or contains(@class,'toast-message')]/span"))
            )
            print("[✓] Post probably successful (toast appeared).")
        except Exception:
            print("[!] Could not confirm via toast — please check LinkedIn manually.")

    except Exception as e:
        print(f"[X] Error while posting: {e}")

    finally:
        time.sleep(3)
        driver.quit()


if __name__ == "__main__":
    caption, media, options = get_post_data()
    for opt in options:
        post_to_linkedin(caption, media, opt)
