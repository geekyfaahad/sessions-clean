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
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f'Deleted {file_path}')