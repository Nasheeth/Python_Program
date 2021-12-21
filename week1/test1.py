current_time = input("Enter the current time in hours: ")
alarm_hour = input("Enter the Alarm time: ")

current_time_in_second = int(current_time) * 3600
print(current_time_in_second)

alarm_hour_in_second = int(alarm_hour) * 3600
print(alarm_hour_in_second)

alarm_ringing_time = int(current_time_in_second + alarm_hour_in_second) / 3600


print("Next alarm at: ")
print(alarm_ringing_time % 24)




