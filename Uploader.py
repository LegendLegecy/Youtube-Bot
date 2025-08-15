

def Upload():

    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import os
    import tempfile
    import time
    import undetected_chromedriver as us
    import pyautogui

    # Get the path to chromedriver.exe in the current directory
    driver_path = os.path.join(os.getcwd(), 'chromedriver.exe')

    # Set up Chrome options
    chrome_options = Options()
    # Use a temporary user data directory for automation to avoid conflicts

    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--start-maximized')


    print('\n\nLoading Chrome driver...')
    # Start the Chrome driver with the options
    driver = us.Chrome(service=Service(driver_path), options=chrome_options)

    print('Opening Url...')
    # Open YouTube
    driver.get('https://studio.youtube.com/channel/UCrqLHwNgsaNoRKwwGKkplnQ/videos/short?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D')



    def login_if_needed():
        USERNAME = "legendslegecy1@gmail.com"
        PASSWORD = "-billionare@2008"
        time.sleep(3)
        # Check if login page is shown
        if "accounts.google.com" in driver.current_url or "ServiceLogin" in driver.current_url:
            # Enter email
            email_input = driver.find_element(By.XPATH, '//input[@type="email"]')
            email_input.send_keys(USERNAME)
            email_input.send_keys(Keys.RETURN)
            time.sleep(10)
            # Enter password
            password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
            password_input.send_keys(PASSWORD)
            password_input.send_keys(Keys.RETURN)
            time.sleep(10)


            screen_width, screen_height = pyautogui.size()
            # click on try another method
            pyautogui.moveTo(screen_width - 350, screen_height - 80, duration=1)
            pyautogui.click()
            time.sleep(10)
            # click on use your   
            pyautogui.moveTo(screen_width - 600, screen_height - 300, duration=1)
            pyautogui.click() 
            time.sleep(10)
            # click on continue
            pyautogui.moveTo(screen_width - 320, screen_height - 280, duration=1)
            pyautogui.click() 
            time.sleep(10)
            # Click on window hello
            pyautogui.moveTo(screen_width - 1000, screen_height - 700, duration=1)
            pyautogui.click() 
            time.sleep(10)
            # writing passkey        
            pyautogui.typewrite("2008\n")
            
    login_if_needed()

    # Upload bean.mp4 to YouTube Shorts
    def uploading_process(video_path):
        print("Uploading Video...")
        time.sleep(50)
        # Upload the file
        file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
        file_input.send_keys(os.path.abspath(video_path))
        time.sleep(30)
        # Click "Next" buttons
        for _ in range(3):
            next_btn = driver.find_element(By.XPATH, '//ytcp-button[@id="next-button"]')
            next_btn.click()
            time.sleep(30)
        # Set visibility to "Public"
        public_radio = driver.find_element(By.NAME, "PUBLIC")
        public_radio.click()
        time.sleep(20)
        # Click "Done"/"Publish"
        publish_btn = driver.find_element(By.XPATH, '//ytcp-button[@id="done-button"]')
        publish_btn.click()
        time.sleep(20)


    dirs= os.listdir('Splitted Videos')
    for video_name in dirs:
        video_name = os.path.join('Splitted Videos', video_name)
        print(f"Uploading {video_name}...")
        uploading_process(video_name)
        time.sleep(500)
        # Click on "Close" button after upload
        close_btn = driver.find_element(By.XPATH, '//ytcp-button[@id="close-button"]')


        close_btn.click()
        time.sleep(10)

        # Click on "Create" button (the camera icon with a plus)
        create_btn = driver.find_element(By.XPATH, '//ytcp-button[@id="create-icon"]')
        create_btn.click()
        time.sleep(10)

        # Click on "Upload videos" in the dropdown
        upload_menu_btn = driver.find_element(By.XPATH, '//tp-yt-paper-item[@test-id="upload-beta"]')
        upload_menu_btn.click()

    # Quit the driver and shutdown the system
    driver.quit()
    os.system("shutdown /s /t 1")


Upload()