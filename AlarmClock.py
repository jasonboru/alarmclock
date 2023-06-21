import datetime
import time
from playsound import playsound

now = datetime.datetime.now()  # grabs the current time
print("Current time:" )
print(now.strftime("%H:%M"))  # prints current time in HH:MM format to help user
def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up!")
            playsound("alarm_fast_A1.mp3")
            break
        time.sleep(60)  # loop runs every 60 sec tCheck every minute

def main():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
