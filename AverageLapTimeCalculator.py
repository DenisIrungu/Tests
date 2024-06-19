print("——————————————————————————————————————")
print("  1  |        4 x 400m Relay          ")
print("——————————————————————————————————————")
print("  2  |       Average Time Lap         ")
print("——————————————————————————————————————")
print("  3  |        & Overall Time          ")
print("——————————————————————————————————————")
print("  4  |          Calculator            ")
print("——————————————————————————————————————")
print("")

runners = ["Alina","Rafael","Sid","Suraya"]
times = ["1:24","1:45","1:33","1:39"]

def convert_time_to_seconds (time_str):
    munites,seconds = map (int, time_str.split(':'))
    minute_seconds = munites * 60 + seconds
    return minute_seconds

def seconds_munites (munite_seconds):
    munites = munite_seconds //60
    remaining_seconds = munite_seconds % 60
    return f"{munites}:{remaining_seconds:02d}"

new_time = [convert_time_to_seconds(time) for time in times]

overall_time_seconds = sum(new_time)

avarage_lap_time_seconds = overall_time_seconds/len(new_time)

overall_time = seconds_munites( overall_time_seconds)
avarage_lap_time = seconds_munites (int(avarage_lap_time_seconds))
print (f"The overall time is {overall_time}")
print (f"The avarage lap time is : {avarage_lap_time}")





