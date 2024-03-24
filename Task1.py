#Ankit Upadhyay,, uankit281@gmail.com

def inches_to_cm(inches):
    return inches * 2.54

def feet_to_meters(feet):
    return feet * 0.3048

def cm_to_inches(cm):
    return cm / 2.54

def meters_to_feet(meters):
    return meters / 0.3048

def main():
    print("Welcome to the Measurement Converter")
    print("1. Inches to Centimeters")
    print("2. Feet to Meters")
    print("3. Centimeters to Inches")
    print("4. Meters to Feet")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print("You have selected option 1: Inches to Centimeters")
        value = float(input("Enter the value in inches to convert to centimeters: "))
        result = inches_to_cm(value)
        print(f"{value} inches is equal to {result} centimeters.")
    elif choice == '2':
        print("You have selected option 2: Feet to Meters")
        value = float(input("Enter the value in feet to convert to meters: "))
        result = feet_to_meters(value)
        print(f"{value} feet is equal to {result} meters.")
    elif choice == '3':
        print("You have selected option 3: Centimeters to Inches")
        value = float(input("Enter the value in centimeters to convert to inches: "))
        result = cm_to_inches(value)
        print(f"{value} centimeters is equal to {result} inches.")
    elif choice == '4':
        print("You have selected option 4: Meters to Feet")
        value = float(input("Enter the value in meters to convert to feet: "))
        result = meters_to_feet(value)
        print(f"{value} meters is equal to {result} feet.")
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
