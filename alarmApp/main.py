# import 
import time
from playsound import playsound  # to play the mp3 file

# CONSTANTS
CLEAR = "\033[2J"               # CLEAR SCREEN
CLEAR_AND_RETURN = "\033[H"     # CLEAR AND GET THE CURSOR TO THE TOP OF THE PAGE


def countdown(seconds):
    """
    This function takes seconds as parameter and returns remaining time after each second pass
    param: int (seconds)
    return: str (remaining time) 
    """

    print(CLEAR)

    time_elapsed = 0        # for decreament the seconds

    while seconds > time_elapsed:
        # this loop will continue until the given param (seconds) is less than time_elapsed
        
        # calculate the remaining time in seconds
        time_left = seconds - time_elapsed
        
        # to calculate remaining hour, minute and second
        hour_left = time_left // 3600  
        min_left = (time_left - hour_left * 3600) // 60
        sec_left = (time_left) - (hour_left * 3600) - (min_left * 60)

        # wait for 1 second
        time.sleep(1)

        # increase the time to decrease the seconds one by one
        time_elapsed += 1

        # after each second pass inform the user about remaining time
        print(f"{CLEAR_AND_RETURN}Alarm will ring in: {hour_left:02d}:{min_left:02d}:{sec_left:02d}")

    # after loop done ring the bell
    playsound(r"alarm.mp3")


def TakeTime():
    print(" ***** Use this format to set your alarm: hour.minute.second ***** ")

    while True:
        alarm_time = input("How much time to wait (hour.minute.second): ")

        hour, minute, second = alarm_time.strip().split(".")
        try:
            hour, minute, second = int(hour), int(minute), int(second)
        except ValueError:
            print("Please enter valid inputs to set your alarm.")
            continue
        else:
            total_secs = hour * 3600 + minute * 60 + second
            break

    """
    # Alternative input
        # Take inputs from the user (hour, minute and seconds)
    while True:
        hours = input("How many hours to wait: ")
        minutes = input("How many minutes to wait: ")
        seconds = input("How many seconds to wait: ")
        try:
            hours, minutes, seconds = hours.strip(), minutes.strip(), seconds.  strip()
            hours, minutes, seconds = int(hours), int(minutes), int(seconds)
        except ValueError:
            print("Please enter a valid input.")
        else:
            break


    # calculate the total seconds (this will be given as arg to the function)
    total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
    """
    
    # print(f"Your alarm will ring in {hour:02d} hour {minute:02d} minute {second:02d} seconds later")
    return total_secs




if __name__ == "__main__":
    secs = TakeTime()
    countdown(secs)