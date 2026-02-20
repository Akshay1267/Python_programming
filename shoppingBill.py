books = int(input("Enter the number of books you buy: "))
pens = int(input("Enter the number of pens you buy: "))
bookPrice = 45
penPrice = 20

totalBill = (books * bookPrice) + (pens * penPrice)
payment = int(input("Enter the amount you pay: "))
if(payment == totalBill):
    print("Thank you for your payment. Your bill is paid in full.")
else:
    remainingAmount = totalBill - payment
    print("Thank you for your payment. Your remaining balance is: ", remainingAmount)