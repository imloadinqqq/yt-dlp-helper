import subprocess
from colorama import init, Fore, Style


def ask():
    while True:
        print("Hello! Please choose from the menu")
        print(f"\n\033[4m{Fore.CYAN}YT-DLP Menu{Style.RESET_ALL}\033[0m\n")
        print("1. Download YouTube video as MP3")
        # yt-dlp -x --audio-format mp3 --audio-quality 0 --embed-metadata --embed-thumbnail "https://www.youtube.com/watch?v=VIDEO_ID"
        print("2. Download YouTube video as MP3 with metadata embedded")
        print("3. Download YouTube video as MP4")
        # yt-dlp "https://www.youtube.com/playlist?list=PLAYLIST_ID"
        print("4. Download YouTube playlist")
        # yt-dlp --playlist-items ITEM_NUM "https://www.youtube.com/playlist?list=PLAYLIST_ID"
        print("5. Download specific video in playlist")
        # yt-dlp --playlist-items 1,3,5 "https://www.youtube.com/playlist?list=PLAYLIST_ID"
        print("6. Download multiple specific videos in playlist")
        # yt-dlp --write-subs --sub-lang en "https://www.youtube.com/watch?v=VIDEO_ID"
        print("7. Download YouTube video with English subtitles")
        # yt-dlp --write-thumbnail "https://www.youtube.com/watch?v=VIDEO_ID"
        print("8. Download YouTube video with thumbnail")
        # yt-dlp -j "https://www.youtube.com/watch?v=VIDEO_ID"
        print("9. Download YouTube video metadata as JSON")
        # yt-dlp --embed-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
        print("10. Download YouTube video with metadata embedded")
        print("99. Exit")

        return input("Enter a choice: ")


def command_one():
    print("You chose: 1. Download YouTube Video as MP3")
    link = input(
        "Please enter the link(s) you would like to download (space in between links): ")

    cmd = ["yt-dlp", "--extract-audio", "--audio-format",
           "mp3", "--audio-quality", "0", link]
    print(f"The following command will run: {
          Fore.BLUE}{' '.join(cmd)}{Style.RESET_ALL}")

    try:
        subprocess.run(cmd, check=True)
        print(f"{Fore.GREEN}Download completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}An error occurred: {e}")


def command_two():
    print("You chose: 2. Download YouTube Video as MP4")
    link = input(
        "Please enter the link(s) you would like to download (space in between links): ")

    cmd = ["yt-dlp", "-f", "bestvideo+bestaudio", link]
    print(f"The following command will run: {
          Fore.BLUE}{' '.join(cmd)}{Style.RESET_ALL}")

    try:
        subprocess.run(cmd, check=True)
        print(f"{Fore.GREEN}Download completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}An error occurred: {e}")


def command_three():
    print("You chose: 3. Download YouTube video as MP4")
    link = input(
        "Please enter the link(s) you would like to download (space in between links): ")


def print_choice(answer):
    menu_choices = [
        "1. Download YouTube video as MP3",
        "2. Download YouTube video as MP3 with metadata embedded",
        "3. Download YouTube video as MP4",
        "4. Download YouTube playlist",
        "5. Download specific video in playlist",
        "6. Download multiple specific videos in playlist",
        "7. Download YouTube video with English subtitles",
        "8. Download YouTube video with thumbnail",
        "9. Download YouTube video metadata as JSON",
        "10. Download YouTube video with metadata embedded",
        "99. Exit"
    ]

    if int(answer) != 99:
        print(f"You chose {menu_choices[answer+1]}")


def process_response(answer):
    print(f"Resonse: {answer}")
    match answer:
        case 1:
            command_one()
        case 2:
            pass
        case 3:
            pass
        case 99:
            pass
        case _:
            print(f"{Fore.RED}Invalid number: {answer}")


def main():
    while True:
        answer = (int(ask()))
        if answer == 99:
            print("Goodbye!")
            break
        process_response(answer)


if __name__ == "__main__":
    main()
