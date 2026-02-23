# Program Name: Online Exam Result Processor

scores = [25, 34, 40, 55, 30, 80, 20]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Count passed students (>=40)
passed = len([s for s in scores if s >= 40])

print("Updated Scores:", scores)
print("Passed Students:", passed)

# Output:
# Updated Scores: [35,39,40, 55, 35, 80]
# Passed Students: 3
