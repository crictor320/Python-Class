"""
Set an alarm to take a break by playing a youtube video
"""

import webbrowser
import time

def main():
    """
    Test function
    :return: nothing
    """

    video_address = "https://www.youtube.com/watch?v=0GgYLdf1ago"

    counter = 0
    while counter < 3:
        time.sleep(60*60)   #delay video 1 hour
        webbrowser.open(video_address)
        counter += 1
        print("It's time to take a break")


if __name__ == '__main__':
    main()
    exit(0)