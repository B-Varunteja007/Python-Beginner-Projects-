from datetime import datetime
from playsound import playsound

def validate_time(alarm_time):
    if len(alarm_time)!=11:
        return "Invalid time format!Please try again.."
    else:
        if int(alarm_time[0:2])>12:
            return "Invalid Hour format..."
        elif int(alarm_time[3:5])>59:
            return "Invalid minute format..."
        elif int(alarm_time[6:8])>59:
            return "Invalid second format..."
        else:
            return "ok"
while True:
    alarm_time=input("ENTER THE ALARM IN HH:MM:SS AM/PM FORMAT")
    validate=validate_time(alarm_time.lower())
    if validate!="ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break
alarm_hour=alarm_time[0:2]
alarm_min=alarm_time[3:5]
alarm_sec=alarm_time[6:8]
alarm_period=alarm_time[9:].upper()
while True:
    now=datetime.now()
    current_hour=now.strftime("%I")
    current_min=now.strftime("%M")
    current_sec=now.strftime("%S")
    current_period=now.strftime("%p")
    if alarm_hour==current_hour:
        if alarm_min==current_min:
            if alarm_sec==current_sec:
                print("WAKE UP TO REALITY..")
                #playsound(r'C:\Users\Varun Teja\OneDrive\Desktop\PYTHON\MINI PROJECTS\ALARM_CLOCK\Alarm Clock_alarm.wav')
                playsound(r"C:\Users\Varun Teja\OneDrive\Desktop\PYTHON\MINI PROJECTS\ALARM_CLOCK\Perfect ! Ed Sheeran Acoustic.wav")
                break

