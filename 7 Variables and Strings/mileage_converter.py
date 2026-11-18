# Mileage converter: Miles to Kilometers

print("--- Mileage Converter ---")

while True:
    miles = input("Enter the distance in miles: ")
    try:
        miles_float = float(miles)
        if miles_float < 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# 1 mile = 1.60934 kilometers
kilometers = miles_float * 1.60934

# Display result
print(f"That is {round(kilometers, 2)} kilometers.")
