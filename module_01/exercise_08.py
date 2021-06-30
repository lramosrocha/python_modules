formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    'I had this thing.',
    'That you could type up right.',
    "But it didn't sing.",  # the ' would need to be escaped
    'So I said goodnight.')
)   # single quote and double quote for escaping, they escape one another automatically