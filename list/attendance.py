attendance = [1, 1, 0, 0, 1, 0, 0, 0]

percentage = (sum(attendance) / len(attendance)) * 100

if percentage < 75:
    print("Below 75% Attendance")

# Replace consecutive absences with "Warning"
for i in range(len(attendance) - 1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "Warning"

print("Attendance %:", percentage)
print("Updated Attendance:", attendance)