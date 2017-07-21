name = 'Barrett Y. Li'
age = 26 # not a lie
height = 68 # inches
weight = 160 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches (%d centermeters) tall." % (height, height * 2.54)
print "He's %d pounds (%d kilograms) heavy." % (weight, weight * 0.45)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
