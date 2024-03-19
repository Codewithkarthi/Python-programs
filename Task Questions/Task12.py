#question: pulling into the station! Input your train carriage size, and let Python work its magic, revealing positions s1 to s5 on the platform.



# Define the size of the train carriage
carriage_size = 10  # Replace 10 with your desired size

# Calculate positions s1 to s5 on the platform
positions_s1_to_s5 = [carriage_size / 5 * i for i in range(1, 6)]

# Print the positions
print("Positions s1 to s5 on the platform are:", positions_s1_to_s5)
