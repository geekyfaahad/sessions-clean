import os
from time import sleep
from utils.classes import *

clear()
check_and_kill_chrome()

username = get_chrome_username()
print(f"Chrome username detected: {username}")
sleep(1)

CHROME_USER_DATA = rf"C:\Users\{username}\AppData\Local\Google\Chrome\User Data"

SESSION_FOLDERS = {
    "Sessions",
    "Session Storage"
}

def get_chrome_profiles(base_path: str):
    """
    Returns all Chrome profile directories
    (Default, Profile 1, Profile 2, Guest Profile, etc.)
    """
    if not os.path.exists(base_path):
        raise FileNotFoundError(f"Chrome User Data not found: {base_path}")

    profiles = []
    with os.scandir(base_path) as entries:
        for entry in entries:
            if entry.is_dir() and (
                entry.name == "Default"
                or entry.name.startswith("Profile")
                or entry.name == "Guest Profile"
            ):
                profiles.append(entry.path)

    return profiles


def clear_session_data(profile_path: str):
    """
    Deletes session-related files inside a Chrome profile
    """
    for folder in SESSION_FOLDERS:
        target_dir = os.path.join(profile_path, folder)

        if not os.path.isdir(target_dir):
            continue

        try:
            with os.scandir(target_dir) as files:
                for file in files:
                    if file.is_file():
                        try:
                            os.remove(file.path)
                            print(f"Deleted: {file.path}")
                        except PermissionError:
                            print(f"Skipped (locked): {file.path}")
                        except Exception as e:
                            print(f"Failed to delete {file.path}: {e}")
        except Exception as e:
            print(f"Error accessing {target_dir}: {e}")


try:
    profiles = get_chrome_profiles(CHROME_USER_DATA)

    if not profiles:
        print("No Chrome profiles found.")
    else:
        print(f"Found {len(profiles)} Chrome profile(s).\n")

    for profile in profiles:
        print(f"Cleaning profile: {profile}")
        clear_session_data(profile)
        print("-" * 60)
        sleep(0.5)

except Exception as e:
    print(f"Critical error: {e}")
