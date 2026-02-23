# Program to calculate Area and Perimeter of a Circle
# With proper comments and input validation

import math   # Importing math module to use value of pi

# Taking input from user
radius_input = input("Enter the radius of the circle: ")

# Validation: Check if input is numeric
if radius_input.replace('.', '', 1).isdigit():
    
    radius = float(radius_input)  # Convert input to float
    
    # Validation: Radius must be positive
    if radius > 0:
        
        # Formula:
        # Area = π * r²
        # Perimeter (Circumference) = 2 * π * r
        
        area = math.pi * radius ** 2
        perimeter = 2 * math.pi * radius
        
        print("\n--- Circle Calculation ---")
        print("Radius:", radius)
        print("Area of Circle:", round(area, 2))
        print("Perimeter (Circumference) of Circle:", round(perimeter, 2))
    
    else:
        print("Error: Radius must be greater than 0.")

else:
    print("Error: Please enter a valid numeric value.")
    # output
    # --- Circle Calculation ---
    #Radius: 7.0
    #Area of Circle: 153.94
    #Perimeter (Circumference) of Circle: 43.98
