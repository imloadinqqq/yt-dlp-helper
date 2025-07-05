import subprocess
from colorama import init, Fore, Style


def ask():
    print("Hello! Please choose from the menu")
    print("\nyt-dlp Menu")
    print("1. Download YouTube Video as MP3")
    print("2. Download YouTube Video as MP4")

    answer = input()
    return answer


def command_one():
    print("You chose: 1. Download YouTube Video as MP3")
    link = input("Please enter the link you would like to download: ")

    cmd = ["yt-dlp", "--extract-audio", "--audio-format",
           "mp3", "--audio-quality", "0", link]
    print(f"The following command will run: {
          Fore.BLUE}{' '.join(cmd)}{Style.RESET_ALL}")

    try:
        subprocess.run(cmd, check=True)
        print(f"{Fore.GREEN}Download completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}An error occurred: {e}")


def process_response(answer):
    print(answer)
    match answer:
        case 1:
            command_one()
        case 2:
            pass
        case 3:
            pass
        case _:
            print(f"{Fore.RED}Invalid number: {answer}")


def main():
    answer = ask()
    process_response(int(answer))


if __name__ == "__main__":
    main()
