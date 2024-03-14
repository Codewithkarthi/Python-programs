#Give the kilometer your bike is driventhe program should print the bike uses how much litre of petrol using python 
def calculate_petrol_usage(distance_driven, mileage):
    petrol_used = distance_driven / mileage
    return petrol_used

# Example usage:
distance_driven = float(input("Enter the distance driven in kilometers: "))
mileage = float(input("Enter the bike's mileage in kilometers per litre: "))

petrol_used = calculate_petrol_usage(distance_driven, mileage)

print(f"The bike has used {petrol_used:.2f} litres of petrol.")
