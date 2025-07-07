import subprocess
import logging
import os
from colorama import init, Fore, Style

cookie_path = None
download_path = "./output"

init(autoreset=True)

# Logging config
logging.basicConfig(
    filename='app.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

menu_choices = [
    "1. Download YouTube video as MP3",
    "2. Download YouTube video as MP3 with metadata embedded",
    "3. Download YouTube video as MP4",
    "4. Download YouTube playlist",
    "5. Download specific video in playlist",
    "6. Download multiple specific videos in playlist",
    "7. Download YouTube video with English subtitles",
    "8. Download YouTube video with thumbnail (separate)",
    "9. Download YouTube video with thumbnail (embedded)",
    "10. Download YouTube video metadata as JSON",
    "11. Download YouTube video with metadata embedded",
    "98. Change cookie path",
    "99. Exit"
]


def ask():
    print(f"\n\033[4m{Fore.CYAN}YT-DLP Menu\033[0m\n")
    for choice in menu_choices:
        print(choice)
    return input("Enter a choice: ")


def command_one():
    link = input("Enter link(s): ")
    cmd = ["yt-dlp", "--extract-audio", "--audio-format",
           "mp3", "--audio-quality", "0", link]
    print_command(cmd)
    run_process(cmd)


def command_two():
    link = input("Enter link(s): ")
    cmd = ["yt-dlp", "--extract-audio", "--audio-format",
           "mp3", "--audio-quality", "0", "--embed-metadata", link]
    print_command(cmd)
    run_process(cmd)


def command_three():
    link = input("Enter link(s): ")
    cmd = ["yt-dlp", "-f", "bestvideo+bestaudio", link]
    print_command(cmd)
    run_process(cmd)


def command_four():
    link = input("Enter playlist link: ")
    cmd = ["yt-dlp", link]
    print_command(cmd)
    run_process(cmd)


def command_five():
    link = input("Enter playlist link: ")
    num = input("Enter video index: ")
    cmd = ["yt-dlp", "--playlist-items", num, link]
    print_command(cmd)
    run_process(cmd)


def command_six():
    link = input("Enter playlist link: ")
    nums = input("Enter video indices (comma separated): ")
    cmd = ["yt-dlp", "--playlist-items", nums, link]
    print_command(cmd)
    run_process(cmd)


def command_seven():
    subtitle_languages = [
        "en", "es", "fr", "de", "pt", "ru", "zh-Hans",
        "zh-Hant", "ar", "ja", "ko", "hi", "it"
    ]
    link = input("Enter video link: ")
    print("Supported subtitle languages:", ", ".join(subtitle_languages))
    lang = input("Enter subtitle language: ").strip()

    if lang in subtitle_languages:
        cmd = ["yt-dlp", "--write-subs", "--sub-lang", lang, link]
        print_command(cmd)
        run_process(cmd)
    else:
        print(f"{Fore.RED}{lang} is not supported.")


def command_eight():
    link = input("Enter video link: ")
    cmd = ["yt-dlp", "--write-thumbnail", link]
    print_command(cmd)
    run_process(cmd)


def command_nine():
    link = input("Enter video link: ")
    cmd = ["yt-dlp", "--write-thumbnail", "--embed-thumbnail", link]
    print_command(cmd)
    run_process(cmd)


def command_ten():
    link = input("Enter video link: ")
    cmd = ["yt-dlp", "-j", link]
    print_command(cmd)
    run_process(cmd)


def command_eleven():
    link = input("Enter video link: ")
    cmd = ["yt-dlp", "--embed-metadata", link]
    print_command(cmd)
    run_process(cmd)


def print_choice(answer):
    if int(answer) != 99:
        print(f"You chose: {Fore.BLUE}{menu_choices[int(answer) - 1]}")


def process_response(answer):
    match answer:
        case 1: command_one()
        case 2: command_two()
        case 3: command_three()
        case 4: command_four()
        case 5: command_five()
        case 6: command_six()
        case 7: command_seven()
        case 8: command_eight()
        case 9: command_nine()
        case 10: command_ten()
        case 11: command_eleven()
        case 99: pass
        case _: print(f"{Fore.RED}Invalid number: {answer}")


def run_process(cmd):
    global cookie_path, download_path
    try:
        final_cmd = cmd[:]
        subdir = determine_subdir_by_cmd(cmd)
        output_dir = os.path.join(download_path, subdir)
        os.makedirs(output_dir, exist_ok=True)

        if cookie_path:
            final_cmd = ["yt-dlp", "--cookies", cookie_path] + final_cmd[1:]

        final_cmd = final_cmd[:1] + ["-P", output_dir] + final_cmd[1:]

        logging.info(f"Running command: {' '.join(final_cmd)}")
        subprocess.run(final_cmd, check=True)
        print(f"{Fore.GREEN}Download completed successfully to {output_dir}.")
        logging.info("Download completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}An error occurred: {e}")
        logging.error(f"An error occurred: {e}")


def print_command(cmd):
    print(f"The following command will run: {Fore.BLUE}{' '.join(cmd)}")


def change_cookie_path():
    global cookie_path
    print(f"Your current cookie path is: {Fore.BLUE}{cookie_path}")
    path = input("Enter new cookie path: ").strip()
    if os.path.exists(path):
        cookie_path = path
        print(f"New cookie path set to: {Fore.BLUE}{cookie_path}")
    else:
        print(f"{Fore.RED}File does not exist.")


def ask_download_path():
    global download_path
    while True:
        path = input("Enter download directory: ").strip()
        if path == "":
            print(f"{Fore.RED}You must provide a download directory!")
            continue
        elif os.path.exists(path):
            download_path = path
            print(f"Download path set to: {Fore.BLUE}{download_path}")
            break
        else:
            try:
                os.makedirs(path)
                download_path = path
                print(f"{Fore.YELLOW}Directory created. Path set to: {
                      Fore.BLUE}{download_path}")
                break
            except Exception as e:
                print(f"{Fore.RED}Failed to create directory: {e}")


def determine_subdir_by_cmd(cmd):
    if "-j" in cmd:
        return "json"
    elif "--extract-audio" in cmd:
        if "--embed-metadata" in cmd:
            return "audio_with_metadata"
        return "audio"
    elif "--write-thumbnail" in cmd and "--embed-thumbnail" not in cmd:
        return "thumbnails"
    elif "--write-thumbnail" in cmd and "--embed-thumbnail" in cmd:
        return "videos_with_embedded_thumbnails"
    elif "--embed-metadata" in cmd:
        return "videos_with_metadata"
    elif "--write-subs" in cmd:
        return "videos_with_subtitles"
    elif "-f" in cmd or "bestvideo+bestaudio" in cmd:
        return "videos"
    elif "--playlist-items" in cmd:
        return "playlist_items"
    else:
        return "others"


def main():
    global cookie_path

    while True:
        path = input("Enter path to your cookies.txt file: ").strip()
        if path == "":
            print(f"{Fore.RED}You must provide a cookie file!")
            continue
        elif os.path.exists(path):
            cookie_path = path
            print(f"Cookie path set to: {Fore.BLUE}{cookie_path}")
            break
        else:
            print(f"{Fore.RED}File does not exist. Please try again.")

    print("Hello! Please choose from the menu")

    while True:
        try:
            answer = int(ask())
            if answer == 98:
                change_cookie_path()
                continue
            elif answer == 99:
                print("Goodbye!")
                break
            elif answer < 1 or answer > len(menu_choices):
                print(f"{Fore.RED}Invalid choice!")
                continue

            print_choice(answer)
            process_response(answer)
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.")


if __name__ == "__main__":
    main()
