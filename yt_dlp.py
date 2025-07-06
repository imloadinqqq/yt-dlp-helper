import subprocess
import logging
from colorama import init, Fore, Style

init(autoreset=True)

# add logging config

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
    "99. Exit"
]


def ask():
    print(f"\n\033[4m{Fore.CYAN}YT-DLP Menu\033[0m\n")
    for choice in menu_choices:
        print(choice)

    return input("Enter a choice: ")


def command_one():
    link = input(
        "Please enter the link(s) you would like to download (space in between links): ")

    cmd = ["yt-dlp", "--extract-audio", "--audio-format",
           "mp3", "--audio-quality", "0", link]
    print_command(cmd)

    run_process(cmd)


def command_two():
    link = input(
        "Please enter the link(s) you would like to download (space in between links): ")

    cmd = ["yt-dlp", "-f", "bestvideo+bestaudio", link]
    print_command(cmd)

    run_process(cmd)


def command_three():
    link = input(
        "Please enter the link(s) you would like to download (space in between links): ")
    cmd = ["yt-dlp", "-f", "bestvideo+bestaudio", link]
    print_command(cmd)

    run_process(cmd)


def command_four():
    link = input("Please enter the playlist link you would like to download: ")
    cmd = ["yt-dlp", link]
    print_command(cmd)

    run_process(cmd)


def command_five():
    link = input("Please enter the playlist link you would like to use: ")
    num = input(
        "Please enter the index of the video you would like to download in the playlist: ")
    cmd = ["yt-dlp", "--playlist-items", num, link]
    print_command(cmd)

    run_process(cmd)


def command_six():
    link = input("Please enter the playlist link you would like to use: ")
    nums = input(
        "Please enter the indices of the videos in the playlist you would like to download (commas; ex: 1,2,3): ")
    cmd = ["yt-dlp", "--playlist-items", nums, link]
    print_command(cmd)

    run_process(cmd)


def command_seven():
    subtitle_languages = [
        "en",        # English
        "es",        # Spanish
        "fr",        # French
        "de",        # German
        "pt",        # Portuguese
        "ru",        # Russian
        "zh-Hans",   # Chinese (Simplified)
        "zh-Hant",   # Chinese (Traditional)
        "ar",        # Arabic
        "ja",        # Japanese
        "ko",        # Korean
        "hi",        # Hindi
        "it",        # Italian
    ]
    link = input(
        "Please enter the link of the video you would like to download: ")

    print("Supported subtitle languages:")
    print(", ".join(subtitle_languages))

    lang = input(
        f"Please enter the subtitle language you would like: ").strip()

    if lang in subtitle_languages:
        print(f"Selected language: {lang}")
        cmd = ["yt-dlp", "--write-subs", "--sub-lang", lang, link]
        print_command(cmd)

        run_process(cmd)
    else:
        print(f"{lang} is not in the list")


def command_eight():
    link = input(
        "Please enter the link of the video you would like to download: ")
    cmd = ["yt-dlp", "--write-thumbnail", link]
    print_command(cmd)

    run_process(cmd)


def command_nine():
    link = input(
        "Please enter the link of the video you would like to download: ")
    cmd = ["yt-dlp", "--write-thumbnail", "--embed-thumbnail", link]
    print_command(cmd)

    run_process(cmd)


def command_ten():
    link = input(
        "Please ente the link of the video you would like to download: ")
    cmd = ["yt-dlp", "-j", link]
    print_command(cmd)

    run_process(cmd)


def command_eleven():
    link = input(
        "Please enter the link of the video you would like to download: ")
    cmd = ["yt-dlp", "--embed-metadata", link]
    print_command(cmd)

    run_process(cmd)


def print_choice(answer):

    if int(answer) != 99:
        print(f"You chose: {Fore.BLUE}{
              menu_choices[int(answer) - 1]}")


def process_response(answer):
    match answer:
        case 1:
            command_one()
        case 2:
            command_two()
        case 3:
            command_three()
        case 4:
            command_four()
        case 5:
            command_five()
        case 6:
            command_six()
        case 7:
            command_seven()
        case 8:
            command_eight()
        case 9:
            command_nine()
        case 10:
            command_ten()
        case 11:
            command_eleven()
        case 99:
            pass
        case _:
            print(f"{Fore.RED}Invalid number: {answer}")


def run_process(cmd):
    try:
        subprocess.run(cmd, check=True)
        print(f"{Fore.GREEN}Download completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}An error occurred: {e}")


def print_command(cmd):
    print(f"The following command will run: {
        Fore.BLUE}{' '.join(cmd)}")


def main():
    print("Hello! Please choose from the menu")
    while True:
        answer = (int(ask()))
        if answer > len(menu_choices):
            if answer == 99:
                print("Goodbye!")
                break
            print(f"{Fore.RED}Invalid choice!")
            continue
        print_choice(answer)
        process_response(answer)


if __name__ == "__main__":
    main()
