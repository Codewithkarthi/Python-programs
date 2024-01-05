#You have number of subjects when you are entering the time it should print the current subject in python 
import datetime

#Get the current time
current_time = datetime.datetime.now().time()

# Prompt the user for the number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Calculate the index of the current subject based on the current hour
current_subject_index = current_time.hour % num_subjects

# List of subjects
subjects = [f"Subject {i+1}" for i in range(num_subjects)]

# Print the current subject
print(f"At {current_time}, your current subject is: {subjects[current_subject_index]}")
