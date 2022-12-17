import os
import shutil

home = os.path.expanduser("~") + "/"
config_folder = home + ".config/"
powershell_folder = config_folder + "powershell/"
gitconfig_file = os.path.join(
    os.getcwd(), os.path.join("config", ".gitconfig"))
user_profile_file = os.path.join(
    os.getcwd(), os.path.join("config", "user_profile.ps1"))


def create_directory(path):
    os.makedirs(path)


def directory_exists(path):
    return os.path.exists(path)


def install_file(src, destiny):
    shutil.copy(src, destiny)


def install():
    if not directory_exists(config_folder):
        create_directory(config_folder)

    if not directory_exists(powershell_folder):
        create_directory(powershell_folder)

    # Git Config
    install_file(gitconfig_file, home)

    # Powershell Profile
    install_file(user_profile_file, powershell_folder)


if __name__ == "__main__":
    install()
