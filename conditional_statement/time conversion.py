# Program to convert seconds into hours, minutes, and seconds
# 1 hour = 3600 seconds
# 1 minute = 60 seconds

# Taking input from user
seconds_input = input("Enter total seconds: ")

# Validation: Check if input is numeric
if seconds_input.isdigit():
    
    total_seconds = int(seconds_input)
    
    # Seconds should not be negative
    if total_seconds >= 0:
        
        # Calculating hours
        hours = total_seconds // 3600
        
        # Remaining seconds after removing hours
        remaining_seconds = total_seconds % 3600
        
        # Calculating minutes
        minutes = remaining_seconds // 60
        
        # Remaining seconds after removing minutes
        seconds = remaining_seconds % 60
        
        print("\n----- Time Conversion -----")
        print("Hours:", hours)
        print("Minutes:", minutes)
        print("Seconds:", seconds)
    
    else:
        print("Error: Seconds cannot be negative.")

else:
    print("Error: Please enter a valid positive integer.")

#output
#Enter total seconds: 3665

#----- Time Conversion -----
#Hours: 1
#Minutes: 1
#Seconds: 5
