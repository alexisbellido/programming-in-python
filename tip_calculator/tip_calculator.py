"""
Tip calculator.
Original version with hardcoded values.

"""


meal = float(raw_input("How much did your meal cost?: "))
tax_rate = float(raw_input("What is the tax rate? "))
tax = tax_rate / 100.0
tip = 5
tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal * tip / 100.0
total = meal_with_tax + tip_value

print "The base cost for the meal was %0.2f" % meal
print "The tax_rate is %0.2f%%" % tax_rate
print "The tip rate is %s%% which is %0.2f" % (str(tip), tip_value)
#print "The tip rate is {}% which is {:0.2f}".format(tip, tip_value)
#print "The tip rate is {tip}% which is {tip_value:0.2f}".format(tip=tip, tip_value=tip_value)
print "Total US$ %0.2f" % total


