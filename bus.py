#######################################################
#
# COSC 140 Homework 2, "bus trip planner" problem
#
#######################################################

hours = int(input("When does the bus depart?(HH) "))
minutes = int(input("When does the bus depart?(MM) "))
km = int(input("How far do you wish to travel?(km) "))
stops = int(input("How many stops are on your way?(stops) "))
#convert the starting time into seconds
seconds = (hours*3600)+(minutes*60)
#take the distance and number of stops and convert into time (seconds)
disttime = (km/(40/3600))+(stops*30)
#now take this time and add it into the arrival time
arrival_time = disttime + seconds
#convert this time back into hours, minutes, and seconds
arrivalh = int(arrival_time)//3600
seconds = int(arrival_time)%3600
arrivalm = int(seconds)//60
seconds = int(seconds)%60
print(f"Arrival time is {arrivalh:d}:{arrivalm:02d}:{seconds:02d}")
