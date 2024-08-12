import os,subprocess,sys
from time import sleep
def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

def check_and_kill_chrome():
    try:
        # Check if Chrome is running
        result = subprocess.run("tasklist /fi \"imagename eq chrome.exe\"", capture_output=True, text=True, shell=True)
        
        if "chrome.exe" in result.stdout:

            print ('Chrome is running, so killing it')
        
            subprocess.run("taskkill /im chrome.exe /f", shell=True)

            print("Chrome has been closed.")
        else:
            # Chrome is not running
            print("Chrome is not currently running.")
            sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")

def get_chrome_username():
    return os.path.basename(os.path.expanduser('~'))