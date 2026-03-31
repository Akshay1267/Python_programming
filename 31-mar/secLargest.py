arr = list(map(int, input("Enter numbers separated by space: ").split()))

first = second = float('-inf')
for x in arr:
    if x > first:
        second = first
        first = x
    elif x > second and x != first:
        second = x

if second == float('-inf'):
    print("No second largest element")
else:
    print("Second largest element:", second)