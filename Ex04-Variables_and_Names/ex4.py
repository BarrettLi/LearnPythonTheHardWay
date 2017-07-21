# Assign 100 to cars
cars = 100
# Assign 4.0 to space_in_a_car
space_in_a_car = 4.0
# Assign 30 to drivers
drivers = 30
# Assign 90 to passengers
passengers = 90
# Assign the result of cars - drivers to cars_not_driven
cars_not_driven = cars - drivers
# Assign the value of drivers to cars_driven
cars_driven = drivers
# Assign the result of cars_driven * space_in_a_car to carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# Assign the result of passengers / cars_driven to average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

