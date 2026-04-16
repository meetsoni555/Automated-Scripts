import os 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. CONFIGURE NORMAL VISIBLE CHROME
options = Options()

# Prevents sandbox errors on certain Linux distributions
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

print("Launching standard Chrome browser...")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30)

try:
    # MAIN LOOP: Keeps asking for songs until 'q' is pressed
    while True:
        print("\n" + "="*40)
        keywords = input("Enter the keywords for the music or type q to quit: ")

        if keywords.lower() == 'q':
            print("Exiting and cleaning up...")
            break # Breaks the infinite loop and closes the browser

        # 2. YOUTUBE AUTOMATION
        driver.get("https://youtube.com")
        print("Connecting to YouTube...")
        time.sleep(5)

        search = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div/div/ytd-masthead/div/div/yt-searchbox/div/div/form/input")))
        search.send_keys(keywords)
        print("Searching...")
        search.send_keys(Keys.RETURN)

        burger = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/div/ytd-menu-renderer/yt-icon-button/button/yt-icon/span/div")))
        burger.click()

        share = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer[2]/tp-yt-paper-item/yt-formatted-string")))
        share.click()

        copy = wait.until(EC.presence_of_element_located((By.ID, "share-url")))
        copied_url = copy.get_attribute("value")
        print(f"Captured URL: {copied_url}")
        time.sleep(1)

        # 3. DOWNLOADER AUTOMATION
        print("Switching to Y2Mate...")
        driver.get("https://y2mate.sc")
        time.sleep(2)

        def downloader_logic(): 
            delay = 0
            try:
                search_box = wait.until(EC.presence_of_element_located((By.NAME, "video")))
                search_box.send_keys(copied_url)
                print("URL pasted...")
                search_box.send_keys(Keys.RETURN)
                
                print("Processing URL... ")
                time.sleep(7)
             
                download_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Download')]")))
                download_btn.click()
                
                song_name = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div")))
                captured = song_name.text
                print("Downloading SONG: " + captured)
                time.sleep(0.3) 
                
                # Monitoring Download Folder
                path = os.path.expanduser("~/Downloads")
                os.chdir(path)
                print("Downloading...")
                
                # Give Chrome up to 5 seconds to initiate the download
                for _ in range(10):
                    if any(f.endswith(".crdownload") for f in os.listdir()) or any(captured in f for f in os.listdir()):
                        break
                    time.sleep(0.5)

                # Loop while the file is still a partial download
                while any(f.endswith(".crdownload") for f in os.listdir()):
                    time.sleep(1) 
                    delay += 1 
                
                print(f"Download completed or processed in {delay} seconds")     
                
                # Final Verification (Allowing 3 more seconds for OS file indexing)
                time.sleep(3)
                
                # 🔥 FIX: Only look for the first 15 characters of the song name
                # This stops characters like | or & from breaking the script!
                search_keyword = captured[:15]
                
                if any(search_keyword in f for f in os.listdir() if not f.endswith(".crdownload")):
                    print("Verification successful! File is in your Downloads.")
                else:
                    print("Download failed or file not found, trying again...")
                    driver.get("https://y2mate.sc") 
                    time.sleep(2)
                    downloader_logic() # Recursive fallback retry

            except Exception as e: 
                print(f"An error occurred: {e}")
                try:
                    error_btn_back = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/div/button")))
                    error_btn_back.click()
                    time.sleep(3)
                    downloader_logic()
                except:
                    pass

        downloader_logic()

finally:
    driver.quit()
    print("Browser closed. Task completed.")
