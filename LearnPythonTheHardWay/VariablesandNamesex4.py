# number of cars set to 100
cars = 100

#space_in_a_car set to 4.0
space_in_a_car = 4.0

#number of drivers set to 30
drivers = 30

#total number of passengers
passengers = 90

#number of cars_not_driven
cars_not_driven = cars - drivers

#numbers of cars driven
cars_driven = drivers

# carpool_capacity is the total number of passengers that can be transported
carpool_capacity = cars_driven * space_in_a_car

#average number of passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars , "cars available."
print "There are only", drivers , "drivers available."
print "There will be" , cars_not_driven , "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We need to put about", average_passengers_per_car , "in each car."
