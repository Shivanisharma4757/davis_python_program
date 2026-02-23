# Program Name: Temperature Monitoring System

temps = [38, 42, 45, 47, 39, 41, 44]

# Find hottest and coldest
hottest = max(temps)
coldest = min(temps)

# Replace temps above 45°C with "Heat Alert"
updated_temps = []
extreme_days = 0

for t in temps:
    if t > 45:
        updated_temps.append("Heat Alert")
    else:
        updated_temps.append(t)
    
    if t > 40:
        extreme_days += 1

print("Hottest Day:", hottest)
print("Coldest Day:", coldest)
print("Updated Temperatures:", updated_temps)
print("Extreme Days (>40°C):", extreme_days)

# Output:
# Hottest Day: 47
# Coldest Day: 38
# Updated Temperatures: [38, 42, 45, 'Heat Alert', 39, 41, 44]
# Extreme Days (>40°C): 5
