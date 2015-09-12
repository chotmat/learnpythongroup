# import from sys the module argv
from sys import argv

# unpack the argv to these variable
script, filename = argv

# open a file with the function open(filename) and assign it to txt
txt = open(filename)

print("Here's your file %r:" % filename)
# read content in the file txt and print it out
print(txt.read())

txt.close()
