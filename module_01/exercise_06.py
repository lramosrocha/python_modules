# declarating and initializing variables with formatted string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those wo know %s and those who %s." % (binary, do_not)

# printing the "joke"
print(x)
print(y)

# printing the joke explanation
print("I said: %r." % x)
print("I also said: '%s'." % y)

# asking, if the joke is funny, by using the boolean variable "hilarious"
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# printing the question above
print(joke_evaluation % hilarious)

# combining two strings in a print
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)