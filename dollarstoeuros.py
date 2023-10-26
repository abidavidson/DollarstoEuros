print("Program: Dollar to Euro Converter (v1)")
print("This program will ask users for a dollar amount and then convert it to euros. They can continue to convert as long as they want to.") 

user_conversion=input("Would you like to convert dollars to euros? ")
while user_conversion == "yes":
    dollar=float(input("Enter dollar amount to be converted: "))
    euro = dollar * .94540
    print("€" + str(euro))
    user_conversion=input("Would you like to convert dollars to euros? ")
