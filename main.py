from utils.classes import *

clear()
check_and_kill_chrome()

username = get_chrome_username()
print(f"Chrome username: {username}")
sleep(2)
directories = [
    rf'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Sessions',
    rf'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Session Storage',
    rf'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Profile 1\Session Storage',
    rf'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Profile 1\Sessions',
    rf'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Profile 2\Session Storage',
    rf'C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Profile 2\Sessions'
]
for directory_path in directories:
    try:
        if os.path.exists(directory_path):  # Check if the directory exists
            for filename in os.listdir(directory_path):
                file_path = os.path.join(directory_path, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f'Deleted {file_path}')
                    sleep(0.5)
        else:
            print(f"Folder not created yet: {directory_path}")
    except Exception as e:
        print(f"Error accessing {directory_path}: {e}")
