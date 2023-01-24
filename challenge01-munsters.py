#!/usr/bin/python3

"""Alta3 Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dictionary

# print the value assoc with "endDate" key from the dict
#print(munsters["endDate"])  # should display 1966
print(munsters.get("endDate")) # does the same thing as line above, EXCEPT
                               # upon not finding a key, returns NONE instead
                               # of an ERROR

# print the value assoc with "startDate" key from the dict
#print("The Munsters began airing on:", munsters["startDate"])
print("The Munsters began airing on:", munsters.get("startDate"))

# print all names from the 3rd key
print("Characters on the Munsters include:", munsters.get("names"))

# Break down the data with a "loop"
# define a new "list" named "names" for the purposes of teaching a simple loop
names = ['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']

# create a simple for loop
for x in names:   # if a line ends in a colon the next line WILL be indented
    print(x, "is a character on the Munsters")
    # print("---")  # print 3 dashes on the screen each time through the loop

# Add to the munsters
munsters["episodes"] = 70
print(munsters)
