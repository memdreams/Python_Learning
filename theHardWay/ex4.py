# Assign cars number
cars = 100
# Assign space value in the car
space_in_a_car = 4.0
# Assign drivers number
drivers = 30
# Assign passengers number
passengers = 90
# Calculate the number of cars not driven
cars_not_driven = cars - drivers
# Calculate the number of driven cars
cars_driven = drivers
# Calculate the amount capacity of the carpool
carpool_capacity = cars_driven * space_in_a_car
# Calculate the average number of passengers in each car
average_passengers_per_car = carpool_capacity / passengers

print "There are", cars, "cars available."
print "There are %s cars available." % cars
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We can transport %5d people today." % carpool_capacity
print "We have", passengers, "to carpool today."
print "We have {0:#b} to carpool today.".format(passengers)
print "We need to put about", average_passengers_per_car, "in each car."
print "We need to put about %.5g in each car." % average_passengers_per_car
