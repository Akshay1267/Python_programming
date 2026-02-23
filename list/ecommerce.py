prices = [1200, 2500, 1200, 800, 3000]

# Remove duplicates
prices = list(set(prices))

total = sum(prices)

# Apply discount
if total > 5000:
    total *= 0.9   # 10% discount

# Add GST 18%
total *= 1.18

print("Final Payable Amount:", total)