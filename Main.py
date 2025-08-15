from yt_dlp import YoutubeDL
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import json
def download_video(video_url):
    tries = 0
    downloaded_file = None
    while tries < 3:
        tries += 1
        try:
            options = {
                'format': 'mp4/best',  # Prefer mp4 to avoid merging
                'outtmpl': '%(title)s.%(ext)s',
                'noplaylist': False,
                'quiet': False,
                'ignoreerrors': False,
                'merge_output_format': None,  # Don't force merging
            }
            with YoutubeDL(options) as ydl:
                info = ydl.extract_info(video_url, download=True)
                if info is not None:
                    downloaded_file = ydl.prepare_filename(info)
                    print("Download completed!")
                    break
                else:
                    print(f"Attempt {tries}: No info extracted, retrying...")
        except Exception as e:
            print(f"Attempt {tries}: Error occurred - {e}")
    return downloaded_file




def split_video_into_chunks(video_path, output_dir, chunk_duration=60):
    try:
        # Load the video file
        video = VideoFileClip(video_path)
        video_duration = int(video.duration)
        video_name = os.path.basename(video_path).rsplit('.', 1)[0]

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Split video into chunks
        for start_time in range(0, video_duration, chunk_duration):
            end_time = min(start_time + chunk_duration, video_duration)
            chunk = video.subclipped(start_time, end_time)
            chunk_filename = os.path.join(output_dir, f"{video_name}_part_{start_time // chunk_duration + 1}.mp4")
            
            print(f"Creating: {chunk_filename}")
            chunk.write_videofile(chunk_filename, codec="libx264", audio_codec="aac")
        
        print("Video splitting completed!")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_file(file_path):
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            os.remove(file_path)  # Delete the file
        else:
            pass
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")




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
        time.sleep(10)
        # Click "Next" buttons
        for _ in range(3):
            next_btn = driver.find_element(By.XPATH, '//ytcp-button[@id="next-button"]')
            next_btn.click()
            time.sleep(2)
        # Set visibility to "Public"
        public_radio = driver.find_element(By.NAME, "PUBLIC")
        public_radio.click()
        time.sleep(1)
        # Click "Done"/"Publish"
        publish_btn = driver.find_element(By.XPATH, '//ytcp-button[@id="done-button"]')
        publish_btn.click()
        time.sleep(10)


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




# Read video URLs from config.json
with open('config.json', 'r') as f:
    config = json.load(f)
    video_urls = config.get('video_urls', [])

for video_url in video_urls:
    print(f"Downloading url: {video_url}")
    video_path = download_video(video_url) 
    if not video_path or not os.path.exists(video_path):
        print(f"No video was downloaded or file does not exist for {video_url}. Skipping.")
        continue
    
    # Output directory
    output_dir = 'Splitted Videos'
    
    # Split the video
    print(f"Splitting video: {video_path}")
    split_video_into_chunks(video_path, output_dir)

# Upload the videos
Upload()
    