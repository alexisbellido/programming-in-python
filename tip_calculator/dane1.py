import sys
parameters = sys.argv


#meal = float(raw_input("Enter price of meal: "))
#tax = float(raw_input("Enter the tax rate: "))
#tip = float(raw_input("Enter your tip as percent of bill (decimal): "))

meal = float(parameters[1])
tax = float(parameters[2])
tip = float(parameters[3])
 
tax_value = meal * tax
meal_with_tax = tax_value + meal
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value
  
print "The cost of your meal is ${0:.2f}.".format(meal)
print "You need to pay tax of: ${0:.2f}.".format(tax_value)
print "You should provide a tip of ${1:.2f}.".format(int(100*tax), tax_value)
print "The total for the meal is ${0:.2f}.".format(total)
