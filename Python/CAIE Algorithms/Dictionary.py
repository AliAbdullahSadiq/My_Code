# creating a dictionary
country_capitals = {"United States": "Washington D.C.", "Italy": "Rome", "England": "London"}

# printing the dictionary
print(country_capitals)

# printing the value
print(country_capitals["United States"]) # Washington D.C.
print(country_capitals["England"]) # London

# change the value of "Italy" key to "ABC"
country_capitals["Italy"] = "ABC"

# add an item with "Germany" as key and "Berlin" as its value
country_capitals["Germany"] = "Berlin"

# delete item having "United States" key
del country_capitals["United States"]
print(country_capitals)