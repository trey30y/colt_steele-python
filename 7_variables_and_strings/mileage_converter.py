# Mileage converter: Miles to Kilometers

print("--- Mileage Converter ---")

while True:
    km = input("Enter the distance in km: ")
    try:
        km_float = float(km)
        if km_float < 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# 1 mile = 1.60934 kilometers
miles = km_float * 0.621371


# Display result
print(f"That is {round(miles, 2)} miles.")
