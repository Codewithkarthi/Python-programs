#give the current date and say whether it is morning or afternoon or evening or night 

import datetime

time = datetime.datetime.now().hour

if 5 <= time < 12:

print("Good morning")

elif 12 <= time < 16:

print("Good afternoon")

elif 16 <= time < 21:

print("Good evening")

else:

print("Good night")
