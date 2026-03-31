salaries = [30000, 60000, 45000, 80000, 25000]

# Remove below minimum wage (say 25000)
salaries = [s for s in salaries if s >= 25000]

# Add 5% bonus
for i in range(len(salaries)):
    if salaries[i] > 50000:
        salaries[i] *= 1.05

# Sort descending
salaries.sort(reverse=True)

print("Top 3 Salaries:", salaries[:3])