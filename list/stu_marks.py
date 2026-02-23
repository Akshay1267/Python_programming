marks = [95, 102, 76, -5, 88, 67, 95]

# Remove invalid marks
marks = [m for m in marks if 0 <= m <= 100]

# Calculate average
avg = sum(marks) / len(marks)

# Find topper(s)
top_score = max(marks)
toppers = [m for m in marks if m == top_score]

# Display grade
if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 50:
    grade = "C"
else:
    grade = "D"

print("Average:", avg)
print("Topper Marks:", toppers)
print("Grade:", grade)